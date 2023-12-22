package log

import (
	"github.com/kelseyhightower/envconfig"
)

type Configuration struct {
	TraceEnabled bool   `default:"false"`
	DebugEnabled bool   `default:"true"`
	PodName      string `envconfig:"POD_NAME"`
	PodIP        string `envconfig:"POD_IP"`
}

var config Configuration

func init() {
	envconfig.Process("log", &config)
}

func Config() *Configuration {
	return &config
}
