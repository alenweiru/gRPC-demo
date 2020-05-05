import grpc

import hello_pb2
import hello_pb2_grpc

# 連接到 127.0.0.1:9999
channel = grpc.insecure_channel('127.0.0.1:9999')

# 創建一個 stub (gRPC client)
stub = hello_pb2_grpc.HelloServiceStub(channel)

# 創建一個 HelloRequest 丟到 stub 去
request = hello_pb2.HelloRequest(greeting="IBDO")

# 呼叫 SayHello service，回傳 HelloResponse
response = stub.SayHello(request)

print(response.reply)