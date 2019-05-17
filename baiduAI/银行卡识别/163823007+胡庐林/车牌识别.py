#!/user/bin/env python
# -*- coding:utf-8 -*-
# @Author:  blueSky
# @Time: 2019年04月24日07时38分09秒

import urllib.request,base64

access_token="24.f0fc76bd7c5c1ba702de9e5ccfbd3f82.2592000.1558668542.282335-16075483"
url="https://aip.baidubce.com/rest/2.0/ocr/v1/license_plate?access_token="+access_token
# 二进制方式打开图文件
f=open(r'./timg.jpg','rb')
img=base64.b64encode(f.read())
#print(img)
params={"image":img}
params=urllib.parse.urlencode(params).encode(encoding="gbk")
print(params)
request = urllib.request.Request(url,params)
request.add_header('Content-Type', 'application/x-www-form-urlencoded')
response = urllib.request.urlopen(request)
content = response.read()
content=content.decode()
if (content):
    print(content)




