package resource

type Label struct {
	Identity
	Name  string `json:"name,omitempty"`
	Value string `json:"value,omitempty"`
}
