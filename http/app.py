import os
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({"message": "pong"}), 200

@app.route('/shutdown', methods=['POST'])
def shutdown():
    # 立即终止 Python 进程
    os._exit(0)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
