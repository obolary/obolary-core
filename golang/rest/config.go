package rest

import (
	"github.com/kelseyhightower/envconfig"
)

type Config struct {
	RestHostAndPort             string `default:":8080"`
	RestBasePath                string `default:"/obolary/1.0"`
	RestTransportMaxIdleConns   int    `default:256"`
	RestTransportMaxTries       int    `default:3"`
	RestTransportRequestTimeout int    `default:60"`
}

var config Config

func init() {
	envconfig.Process("rest", &config)
}
