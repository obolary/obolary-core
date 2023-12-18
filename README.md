## Overview

work-in-progress

## Golang

*.netrc*

```
machine github.com login your_github_id your_github_pac
```

*.gitconfig*

```
[credential]
	helper = netrc

[url "ssh://git@github.com/"]
  insteadOf = https://github.com/
```

*.ssh*

```
$ ssh-keygen -t ed25519 -C "your_email@example.com"
$ pbcopy < ~/.ssh/id_ed25519.pub
```

*environment*

```
export GOPRIVATE=github.com/obolary/*
```
