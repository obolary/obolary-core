package rest

import (
	"github.com/kelseyhightower/envconfig"
)

type Configuration struct {
	HostAndPort             string `default:":8080"`
	BasePath                string `default:"/obolary/1.0"`
	TransportMaxIdleConns   int    `default:"256"`
	TransportMaxTries       int    `default:"3"`
	TransportRequestTimeout int    `default:"60"`
}

var config Configuration

func init() {
	envconfig.Process("rest", &config)
}

func Config() *Configuration {
	return &config
}
