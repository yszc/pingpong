from flask import Flask, request
import socket

app = Flask(__name__)

class TCPClient:
    def __init__(self, host='localhost', port=8888):
        self.host = host
        self.port = port
        
    def send_data(self, data):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            sock.connect((self.host, self.port))
            sock.sendall(data)
            print(f"发送 {len(data)} 字节到 TCP 目标")
        except Exception as e:
            print(f"发送 TCP 数据时出错: {e}")
        finally:
            sock.close()

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