This internal package provides a unified way to extract main body from `html` and `pdf`.

### Usage

Feed a url to the `parser_factory` and you will get a page object

 ```
 page = parser_factory('https://github.com/polyrabbit/hacker-news-digest')
 ```

From the page you can get the main body via the `aritcle` attribute, the summary of body via the `get_summary` method, the illustration via the `get_illustration` method, and the favicon url via the `get_favicon_url` method.

```
>>> page.article
lots of html stuff

>>> page.get_summary(max_length=100)
u'This service extracts summaries and images from  hacker newsarticles for people who want to get the  ...'

>>> page.get_illustration()
<page_content_extractor.html.WebImage at 0x10bc28cd0>

>>> page.get_favicon_url()
'https://github.com/fluidicon.png'
```


### 额外说明

这里只使用该项目的页面提取功能，并作为rpc服务端提供给其他工程调用，也就是说只使用该模块

main.py文件作用：通过socket与其他系统通信

requirements.txt: 仅运行page_content_extractor模块所需依赖

### 独立运行步骤
~~~bash

# 创建单独虚拟环境
python3 -m venv extractor_env
source extractor_env/bin/activate 

# 仅安装页面提取所需依赖
pip install -r ./page_content_extractor/requirements.txt

# 生成grpc代码
#python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. service.proto

# 运行
python3 -m page_content_extractor.main
~~~
