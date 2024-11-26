from flask import Flask, request
import socket

app = Flask(__name__)

class TCPClient:
    def __init__(self, host='192.168.50.11', port=4885):
        self.host = host
        self.port = port
        self.sock = None
        self.connect()
        
    def connect(self):
        """建立TCP连接"""
        if self.sock is None:
            try:
                self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.sock.connect((self.host, self.port))
                print("TCP连接已建立")
            except Exception as e:
                print(f"建立TCP连接时出错: {e}")
                self.sock = None
        
    def send_data(self, data):
        try:
            if self.sock is None:
                self.connect()
            if self.sock:
                self.sock.sendall(data)
                print(f"发送 {len(data)} 字节到 TCP 目标")
        except Exception as e:
            print(f"发送 TCP 数据时出错: {e}")
            self.sock = None  # 发生错误时重置连接
            self.connect()    # 尝试重新连接

tcp_client = TCPClient()

@app.route('/forward', methods=['POST'])
def forward():
    data = request.get_data()
    print(f"收到 HTTP POST 数据: {len(data)} 字节")
    
    # 转发数据到 TCP 目标
    tcp_client.send_data(data)
    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5051) 