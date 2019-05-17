#!/user/bin/env python
# -*- coding:utf-8 -*-
# @Author:  blueSky
# @Time: 2019年04月23日19时53分03秒


# 调用baiduAI的APPID AK ID
import base64
import urllib.request

APP_ID="16075483"
API_KEY="A7ff8S5vqQ63rpwTyXAcPLuF"
SECRET_KEY="DQsS497CcGwheuatwI8G5CZA0R9SGBzd"
access_token="24.207ed6d5444d1a849c37b37c3d648845.2592000.1558615104.282335-16075483"
url="https://aip.baidubce.com/rest/2.0/ocr/v1/license_plate?access_token="+access_token
# 二进制方式打开图文件
f=open(r'./297.jpg','rb')
img=base64.b64encode(f.read())
params={"image":img}
# print(params)
params=urllib.parse.urlencode(params).encode(encoding="utf-8")
# print(params)
request=urllib.request.Request(url,params)
request.add_header('Content-Type', 'application/x-www-form-urlencoded')
respose=urllib.request.urlopen(request)
content=respose.read()
# 如果不加这个decode()结果中文显示出来就是字符串，而且不能带参数，不然也是字符串，亲测
# 测试时间 2019/4/24  中午
content=content.decode()
if(content):
     print(content)
else:
     print("error!")

