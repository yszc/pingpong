# 使用官方的 Go 镜像作为构建基础镜像
FROM golang:1.23 AS builder

# 设置工作目录
WORKDIR /app

# 下载依赖
RUN go env -w GO111MODULE=on && go env -w GOPROXY=https://goproxy.cn,direct 

# 将 go.mod 和 go.sum 复制到工作目录
COPY go.mod go.sum ./

RUN go mod download

# 将项目的全部代码复制到工作目录
COPY . .

# 构建 Go Zero gRPC 服务
RUN CGO_ENABLED=0 GOOS=linux go build -o service .

# 使用更轻量的镜像作为运行时基础镜像
FROM alpine:latest

# 设置时区（可选）
RUN apk --no-cache add tzdata

# 设置工作目录
WORKDIR /root/

# 从构建镜像中复制生成的二进制文件
RUN mkdir -p /root/etc
COPY --from=builder /app/service .
COPY --from=builder /app/etc ./etc

# 开放 gRPC 服务端口
EXPOSE 8080

# 运行 Go Zero gRPC 服务
CMD ["./service"]

