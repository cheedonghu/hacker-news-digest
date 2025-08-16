
# import sys
# import os
# # 添加当前目录到 Python 路径
# sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import grpc
from concurrent import futures
import time

# from . import __init__ as init
from page_content_extractor import parser_factory

from flask import Flask, request, jsonify
from page_content_extractor import parser_factory

app = Flask(__name__)

@app.route('/digest', methods=['GET'])
def digest():
    # 获取 GET 参数 input
    input_text = request.args.get('newsUrl', '')
    
    if not input_text:
        return "Missing 'input' parameter", 400
    
    # 调用原来的解析逻辑
    parser = parser_factory(input_text)
    content = parser.get_content()
    
    # 直接返回内容字符串
    return content

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=50051, debug=False)