# pingpong

## go-zero 操作

更新API，先更新proto的API定义，再用下面命令更新代码

```
cd demo # 进入proto文件目录
goctl rpc protoc demo.proto --go_out=. --go-grpc_out=. --zrpc_out=.
```
