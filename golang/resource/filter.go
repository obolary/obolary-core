package resource

import (
	"time"
)

type Filter struct {
	Condition           string     `json:"condition,omitempty"`
	LimitNumber         int        `json:"limit_number,omitempty"`
	LimitOn             string     `json:"limit_on,omitempty"`
	LimitAfterInclusive *time.Time `json:"limit_after_inclusive,omitempty"`
	LimitBefore         *time.Time `json:"limit_before,omitempty"`
	Page                int        `json:"page,omitempty"`
}
