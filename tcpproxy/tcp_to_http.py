import socket
import requests
import threading

class TCPToHTTPServer:
    def __init__(self, tcp_host='0.0.0.0', tcp_port=7777, http_endpoint='http://localhost:5051/forward'):
        self.tcp_host = tcp_host
        self.tcp_port = tcp_port
        self.http_endpoint = http_endpoint
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
    def start(self):
        self.server_socket.bind((self.tcp_host, self.tcp_port))
        self.server_socket.listen(5)
        print(f"TCP 服务器正在监听 {self.tcp_host}:{self.tcp_port}")
        
        while True:
            client_socket, addr = self.server_socket.accept()
            print(f"接收到来自 {addr} 的连接")
            client_thread = threading.Thread(target=self.handle_client, args=(client_socket,))
            client_thread.start()
            
    def handle_client(self, client_socket):
        try:
            while True:
                data = client_socket.recv(1024)
                if not data:
                    break
                    
                # 将 TCP 数据转发为 HTTP 请求
                response = requests.post(
                    self.http_endpoint,
                    data=data,
                    headers={'Content-Type': 'application/octet-stream'}
                )
                print(f"HTTP 响应状态码: {response.status_code}")
                
        except Exception as e:
            print(f"处理客户端时出错: {e}")
        finally:
            client_socket.close()

if __name__ == '__main__':
    server = TCPToHTTPServer()
    server.start() 