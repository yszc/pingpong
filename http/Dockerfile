# 使用官方 Python 镜像
FROM python:3.9-slim

# 安装依赖
RUN pip install Flask

# 设置工作目录
WORKDIR /app

# 复制当前目录的文件到容器中
COPY . .

# 暴露端口 5000
EXPOSE 5000

# 启动 Flask 应用
CMD ["python", "app.py"]
