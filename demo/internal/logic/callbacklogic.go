package logic

import (
	"context"
	"log"

	"demo/demo"
	"demo/internal/svc"

	"github.com/zeromicro/go-zero/core/logx"
	"github.com/zeromicro/go-zero/zrpc"
	"google.golang.org/grpc"
)

type CallbackLogic struct {
	ctx    context.Context
	svcCtx *svc.ServiceContext
	logx.Logger
}

func NewCallbackLogic(ctx context.Context, svcCtx *svc.ServiceContext) *CallbackLogic {
	return &CallbackLogic{
		ctx:    ctx,
		svcCtx: svcCtx,
		Logger: logx.WithContext(ctx),
	}
}

type (
	CbRequest = demo.CbRequest
	Request   = demo.Request
	Response  = demo.Response

	Demo interface {
		Ping(ctx context.Context, in *Request, opts ...grpc.CallOption) (*Response, error)
		Callback(ctx context.Context, in *CbRequest, opts ...grpc.CallOption) (*Response, error)
	}

	defaultDemo struct {
		cli zrpc.Client
	}
)

func (l *CallbackLogic) Callback(in *demo.CbRequest) (*demo.Response, error) {
	var clientConf zrpc.RpcClientConf
	clientConf.Target = in.GetIP() + ":" + in.GetPort()
	// Add authority option to the client configuration

	conn := zrpc.MustNewClient(clientConf, zrpc.WithDialOption(grpc.WithAuthority(in.GetHost())))
	client := demo.NewDemoClient(conn.Conn())

	resp, err := client.Ping(context.Background(), &demo.Request{})
	if err != nil {
		log.Fatal(err)
		return nil, err
	}

	log.Println(resp)
	return &demo.Response{
		Pong: in.GetIP() + ":" + in.GetPort() + "(" + in.Host + ")resp: " + resp.GetPong(),
	}, nil
}
