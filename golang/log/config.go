package log

import (
	"github.com/kelseyhightower/envconfig"
)

type Config struct {
	TraceEnabled bool   `default:"false"`
	DebugEnabled bool   `default:"true"`
	PodName      string `envconfig:"POD_NAME"`
	PodIP        string `envconfig:"POD_IP"`
}

var config Config

func init() {
	envconfig.Process("log", &config)
}
