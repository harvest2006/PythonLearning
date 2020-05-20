from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from urllib.request import urlopen
import json
import requests
json_url = 'https://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json'
"""
response = urlopen(json_url)

# 读取数据
req = response.read()
# 将数据写入文件
with open('btc_close_2017_urllib.json', 'wb') as f:
    f.write(req)
# 加载json格式
file_urllib = json.loads(req)
print(file_urllib)
"""


#上面用Python 3.x标准库中模块urllib的函数urlopen来做；

#以下使用第三方模块requests封装了许多常用的方法，让数据下载和读取方式显得更简单；
req = requests.get(json_url)
# 将数据写入文件
with open('btc_close_2017_request.json', 'w') as f:
    f.write(req.text)
file_requests = req.json()
print(file_requests)