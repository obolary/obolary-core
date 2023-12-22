package resource

type Object struct {
	Identity
	State  string  `json:"state,omitempty"`
	Status *Status `json:"status,omitempty"`
}
