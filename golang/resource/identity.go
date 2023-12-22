package resource

import (
	"encoding/base64"
	"encoding/json"
	"time"

	"github.com/obolary/obolary-core/golang/log"
)

type Identity struct {
	Kind          string                 `json:"kind,omitempty"`
	ID            string                 `json:"id,omitempty" index:"identity.id" unique:"true"`
	OwnerID       string                 `json:"owner_id,omitempty" index:"identity.ownerid"`
	LabelIDs      []string               `json:"label_ids,omitempty" index:"identity.labelids"`
	Created       *time.Time             `json:"created,omitempty"`
	Updated       *time.Time             `json:"updated,omitempty"`
	Documentation string                 `json:"documentation,omitempty"`
	Extension     map[string]interface{} `json:"-"`
}
type Blob map[string]interface{}

func (blob Blob) SetId(id string) {
	blob["id"] = id
}

func (blob Blob) SetOwnerId(id string) {
	blob["owner_id"] = id
}

func (blob Blob) SetKind(kind Kind) {
	blob["kind"] = kind.String()
}

func (blob Blob) SetCreated(on time.Time) {
	blob["created"] = on
}

func (blob Blob) SetUpdated(on time.Time) {
	blob["updated"] = on
}

func (blob Blob) GetId() (string, bool) {
	if id, exists := blob["id"]; exists {
		return id.(string), exists
	}
	return "", false
}

func (blob Blob) GetOwnerId() (string, bool) {
	if ownerId, exists := blob["owner_id"]; exists {
		return ownerId.(string), exists
	}
	return "", false
}

func (blob Blob) GetKind() (Kind, bool) {
	if kind, exists := blob["kind"]; exists {
		return Kind(kind.(string)), true
	}
	return Kind(""), false
}

type Id struct {
	E string `json:"e,omitempty"`
	K string `json:"k,omitempty"`
}

func NewId(kind Kind, internal string) *Id {
	identifier := Id{
		E: internal,
		K: kind.String(),
	}
	return &identifier
}

func (id *Id) String() string {
	data, _ := json.Marshal(id)
	return base64.StdEncoding.EncodeToString(data)
}

func NewIdFromString(encoded string) *Id {
	var id Id
	if data, goerr := base64.StdEncoding.DecodeString(encoded); goerr != nil {
		log.Debug("id malformed, %v", goerr)
		return nil
	} else {
		if goerr = json.Unmarshal(data, &id); goerr != nil {
			log.Debug("id malformed, %v", goerr)
			return nil
		}
	}
	return &id
}

func (id *Id) Kind() Kind {
	return Kind(id.K)
}

func (id *Id) Id() string {
	return id.E
}
