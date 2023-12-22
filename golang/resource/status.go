package resource

import (
	"fmt"
	"net/http"

	"github.com/obolary/obolary-core/golang/log"
)

type Status struct {
	HttpStatus  int
	Code        string
	Description string
	Uri         string
}

var (
	StatusOk             = &Status{HttpStatus: http.StatusOK, Code: "ok", Description: "OK"}
	StatusInternalServer = &Status{HttpStatus: http.StatusInternalServerError, Code: "internal_server", Description: "internal server status"}
	StatusBadRequest     = &Status{HttpStatus: http.StatusBadRequest, Code: "bad_request", Description: "bad request status"}
	StatusBadGateway     = &Status{HttpStatus: http.StatusBadGateway, Code: "bad_gateway", Description: "bad gateway status"}
	StatusNotImplemented = &Status{HttpStatus: http.StatusNotImplemented, Code: "not_implemented", Description: "endpoint not implemented"}
	StatusNotFound       = &Status{HttpStatus: http.StatusNotFound, Code: "not_found", Description: "resource not found"}
	StatusForbidden      = &Status{HttpStatus: http.StatusForbidden, Code: "forbidden", Description: "requested endpoint or resource access forbidden"}
)

func (status *Status) String() string {
	return fmt.Sprintf("%v: %v", status.Code, status.Description)
}

func (status *Status) Debug() *Status {
	log.NewLog("DEBUG", 1).Emit("%s", status)
	return status
}

func (status *Status) Info() *Status {
	log.NewLog("INFO", 1).Emit("%s", status)
	return status
}

func (status *Status) Alarm() *Status {
	log.NewLog("ALARM", 1).Emit("%s", status)
	return status
}

func (status Status) Clone(args ...interface{}) *Status {
	var clone Status = status
	if len(args) > 0 {
		clone.Description = fmt.Sprintf(args[0].(string), args[1:]...)
	}
	return &clone
}
