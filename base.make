# publish defaults
VERSION ?= v1.0.0
REGISTRY ?= ghcr.io/obolary/
REPOSITORY ?= $(shell basename -s .git `git config --get remote.origin.url`)

# clean
.PHONY: clean
clean:
	@rm -f $(IMAGE)

# build a golang based repo using the default golang container.
.PHONY: golang_build
golang_build:
	@echo "* BUILD: '"$(IMAGE)"'"
	@rm -f $(IMAGE)
	GOOS=linux GOARCH=amd64 go build -v -o $(IMAGE)
	@echo "* DONE : make golang_build"

# build a golang based repo using the default golang container
.PHONY: golang_build_scratch
golang_build_scratch:
	@echo "* BUILD: '"$(IMAGE)"'"
	@rm -f $(IMAGE)
	CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build -v -a -ldflags '-extldflags "-static"' -o $(IMAGE)
	@echo "* DONE : make golang_build"

# build a golang based repo using the given docker container
.PHONY: golang_build_golang
golang_build_golang:
	@echo "* PREPARE AS BUILDER: '"$(IMAGE)"'"
	@touch $(IMAGE)
	@docker build -t $(IMAGE) .
	@rm -f $(IMAGE)
	@echo "* BUILD: '"$(IMAGE)"'"
	GOOS=linux GOARCH=amd64 go build -v -o $(IMAGE)
	@echo "* DONE : make golang_build"

# build the given container
.PHONY: docker_build
docker_build: Dockerfile
	docker build --build-arg REPO=$(REPOSITORY) --build-arg VERSION=$(VERSION) -t $(IMAGE) .
	@echo "* DONE : make docker_build"
	@echo "* NEXT : to publish, execute 'make publish'"

# publish the given container 
.PHONY: docker_publish
docker_publish:
	docker tag $(IMAGE) $(REGISTRY)$(IMAGE):$(VERSION)
	docker push $(REGISTRY)$(IMAGE):$(VERSION)
	docker tag $(IMAGE) $(REGISTRY)$(IMAGE):latest
	docker push $(REGISTRY)$(IMAGE):latest
	@echo "* DONE : make docker_publish"

# get git version
.PHONY: version
version:
	git describe --abbrev=0 --tags
	@echo "* DONE : make version"

# bump git version
# v1.0.N to v1.0.N+1
.PHONY: patch
patch:
	./shell/bump -p v patch
	@echo "* DONE : make patch"

# v1.N.0 to v1.N+1.0
.PHONY: minor
minor:
	./shell/bump -p v minor
	@echo "* DONE : make minor"

# default publish
.PHONY: publish-default
publish-default: docker_publish
	@echo "* DONE"

%: %-default
	@true
