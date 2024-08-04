## 介绍
本工程仅使用[原工程:hacker-news-digest](https://github.com/polyrabbit/hacker-news-digest.git)的网页摘要功能，仅添加了gRPC以供外部工程调用

详见[readme](https://github.com/cheedonghu/hacker-news-digest/blob/master/page_content_extractor/README.md)

## 启动方式

python版本：3.11

~~~bash

git clone https://github.com/cheedonghu/hacker-news-digest.git

# 仅安装页面提取所需依赖
pip install -r ./page_content_extractor/requirements.txt

# 运行
python3 -m page_content_extractor.main
~~~