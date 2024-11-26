package main

import (
	"flag"

	"tcp2http/internal/config"
	"tcp2http/internal/server"

	"github.com/zeromicro/go-zero/core/conf"
)

func main() {
	var configFile = flag.String("f", "etc/config.yaml", "配置文件路径")
	flag.Parse()

	var c config.Config
	conf.MustLoad(*configFile, &c)

	server := server.NewTCPServer(c)
	err := server.Start()
	if err != nil {
		panic(err)
	}
}
