from flask import Flask, request
import json
from datetime import datetime

app = Flask(__name__)

@app.route('/endpoint', methods=['POST'])
def receive_data():
    try:
        # 获取请求数据
        data = request.get_data()
        # json_data = json.loads(data)
        
        # 打印接收到的数据
        print(f"\n[{datetime.now()}] 收到新请求:")
        print(f"数据内容: {data}")
        # print(f"数据内容: {json.dumps(json_data, indent=2, ensure_ascii=False)}")
        
        return {
            "status": "success",
            "message": "数据已接收",
            "received_at": datetime.now().isoformat()
        }
    
    except Exception as e:
        print(f"处理请求时出错: {e}")
        return {
            "status": "error",
            "message": str(e)
        }, 500

if __name__ == '__main__':
    print("HTTP 服务器已启动，监听端口 5050...")
    app.run(host='0.0.0.0', port=5050) 