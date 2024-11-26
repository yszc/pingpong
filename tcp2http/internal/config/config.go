package config

type Config struct {
	TCPServer struct {
		Port int
	}
	HTTPTarget struct {
		URL string
	}
}
