from concurrent import futures
import time

import grpc
import hello_pb2
import hello_pb2_grpc


# 創建一個 HelloServiceServicer，要繼承自 hello_pb2_grpc.HelloServiceServicer
class HelloServiceServicer(hello_pb2_grpc.HelloServiceServicer):

# 由於我們 service 定義了 SayHello 這個 rpc，所以要實作 SayHello 這個 method
    def SayHello(self, request, context):
# response 是個 HelloResponse 形態的 message
        response = hello_pb2.HelloResponse()
        response.reply = f'Hello, {request.greeting}'
        return response


def serve():
    server = grpc.server(futures.ThreadPoolExecutor())

# 利用 add_HelloServiceServicer_to_server 這個 method 把上面定義的 HelloServiceServicer 加到 server 當中
    hello_pb2_grpc.add_HelloServiceServicer_to_server(HelloServiceServicer(), server)

# 讓 server 跑在 port 9999 中
    server.add_insecure_port('[::]:9999')
    server.start()
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()