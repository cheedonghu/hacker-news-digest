
# import sys
# import os
# # 添加当前目录到 Python 路径
# sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import grpc
from concurrent import futures
import time

# 导入生成的proto文件
from . import service_pb2
from . import service_pb2_grpc
# from . import __init__ as init
from page_content_extractor import parser_factory


# 实现服务
class MyServiceServicer(service_pb2_grpc.MyServiceServicer):
    def RemoteFunction(self, request, context):
        # 在这里实现您的逻辑
        print("server has received a msg: "+request.input)
        parser = parser_factory(request.input)
        content = parser.get_content()
        response = service_pb2.ServiceResponse()
        # response.output = f"The extract content is: {request.input}"
        response.output = f"The extract content is: {content}"
        return response

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    service_pb2_grpc.add_MyServiceServicer_to_server(MyServiceServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server started on port 50051")
    try:
        while True:
            time.sleep(86400)  # 一天
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()