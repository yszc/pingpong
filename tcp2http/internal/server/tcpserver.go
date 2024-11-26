package server

import (
	"bytes"
	"fmt"
	"log"
	"net"
	"net/http"
	"tcp2http/internal/config"
)

type TCPServer struct {
	config   config.Config
	listener net.Listener
}

func NewTCPServer(c config.Config) *TCPServer {
	return &TCPServer{
		config: c,
	}
}

func (s *TCPServer) Start() error {
	listener, err := net.Listen("tcp", fmt.Sprintf(":%d", s.config.TCPServer.Port))
	if err != nil {
		return err
	}
	s.listener = listener

	for {
		conn, err := listener.Accept()
		if err != nil {
			log.Printf("接受连接错误: %v", err)
			continue
		}

		go s.handleConnection(conn)
	}
}

func (s *TCPServer) handleConnection(conn net.Conn) {
	defer conn.Close()

	buffer := make([]byte, 1024)
	n, err := conn.Read(buffer)
	if err != nil {
		log.Printf("读取数据错误: %v", err)
		return
	}

	// 转发数据到 HTTP 端点
	err = s.forwardToHTTP(buffer[:n])
	if err != nil {
		log.Printf("转发数据错误: %v", err)
	}
}

func (s *TCPServer) forwardToHTTP(data []byte) error {
	resp, err := http.Post(
		s.config.HTTPTarget.URL,
		"application/json",
		bytes.NewBuffer(data),
	)
	if err != nil {
		return err
	}
	defer resp.Body.Close()

	return nil
}
