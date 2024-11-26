import socket
import json
import time

def send_tcp_data(host='localhost', port=7777):
    # 创建 TCP 客户端 socket
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        # 连接服务器
        client.connect((host, port))
        print(f"已连接到服务器 {host}:{port}")
        
        # 构造测试数据
        test_data = {
            "timestamp": int(time.time()),
            "message": "Hello from TCP client",
            # "data": {
            #     "sensor": "temperature",
            #     "value": 25.6,
            #     "large_data": "x" * 1200,  # 生成一个1200字节的字符串
            #     "additional_info": {
            #         "location": "传感器A区域",
            #         "device_id": "TEMP_SENSOR_001",
            #         "firmware_version": "v1.2.3",
            #         "calibration_date": "2023-01-01",
            #         "maintenance_history": [
            #             {"date": "2023-01-01", "type": "installation", "technician": "张三"},
            #             {"date": "2023-03-15", "type": "calibration", "technician": "李四"},
            #             {"date": "2023-06-30", "type": "maintenance", "technician": "王五"}
            #         ],
            #         "sensor_details": {
            #             "manufacturer": "传感器制造商",
            #             "model": "TS2000",
            #             "serial_number": "TS2000-2023-001-ABC",
            #             "specifications": {
            #                 "accuracy": "±0.1°C",
            #                 "range": "-40°C to 125°C",
            #                 "response_time": "50ms"
            #             }
            #         }
            #     }
            # }
        }
        
        # 发送数据
        # json_data = json.dumps(test_data).encode('utf-8')
        client.send(str(test_data).encode('utf-8'))
        print(f"已发送数据: {test_data}")
        
    except Exception as e:
        print(f"发送数据时出错: {e}")
    
    finally:
        client.close()
        print("连接已关闭")

if __name__ == "__main__":
    while True:
        send_tcp_data()
        time.sleep(2)  # 每2秒发送一次数据 