package resource

type Target struct {
	Identity
	Target  string `json:"target,omitempty"`
	OnOk    string `json:"on_ok,omitempty"`
	OnError string `json:"on_error,omitempty"`
}
