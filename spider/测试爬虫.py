#!/user/bin/env python
# -*- coding:utf-8 -*-
# @Author:  blueSky
# @Time: 2019年05月16日14时08分13秒
import  urllib.request
from bs4 import BeautifulSoup
from openpyxl import workbook

# 测试爬取应届生网站
urlstart="http://my.yingjiesheng.com/index.php/personal/xjhinfo.htm/?page="
urlend="&cid=&city=0&word=&province=0&schoolid=&sdate=&hyid=0"
for i in range(1,2):
    url=urlstart+str(i)+urlend
    resp=urllib.request.urlopen(url)
    html=resp.read()
    htmlprase=BeautifulSoup(html,"html5lib",from_encoding="gbk")
    lan=htmlprase.find_all("tr",attrs={"class":"bg0"})
    tian=htmlprase.find_all("tr",attrs={"class":"bg1"})
    hu=lan+tian
    # 开始处理数据
    for list in hu:
        country=list.find("td",width="80").text
        time=list.find("td",width="120").text

