#!/user/bin/env python
# -*- coding:utf-8 -*-
# @Author:  blueSky
# @Time: 2019年05月10日13时31分35秒
from  bs4 import BeautifulSoup
# 写入Excel需要使用的库
from openpyxl import Workbook
import urllib.request
urlstart = 'http://guba.eastmoney.com/default,99_'
urlend = '.html'
download=[]
#开始爬取数据，计划爬取12页
for i in range(8,10):
    url=urlstart+str(i)+urlend
    print("正在打印："+url)
    resq=urllib.request.urlopen(url)
    html=resq.read()
    bs=BeautifulSoup(html,"html5lib",from_encoding="utf-8")
    alllist1=bs.find_all("ul",attrs={"class":"newlist"})
    li=alllist1[0].find_all("li")
    # 对数据进行处理撒选
    for contenttd in li:
        sub1href = contenttd.find('span',attrs={"class":"sub"}).find('a',attrs={"class":"balink"}).get('href')
        sub2href=contenttd.find('span',attrs={"class":"sub"}).find('a',attrs={"class":"note"}).get('href')
        if 'http' not in sub1href:
            sub1href = 'http://guba.eastmoney.com' + str(sub1href)
        if 'http' not in sub2href:
            sub2href="http://guba.eastmoney.com"+str(sub2href)
        sub1text=contenttd.find('span',attrs={"class":"sub"}).find('a',attrs={"class":"balink"}).text
        sub2text = contenttd.find('span', attrs={"class": "sub"}).find('a',attrs={"class":"note"}).text
        author = contenttd.find('cite',attrs={"class":"aut"}).find('a').text
        lastupdate = contenttd.find('cite', attrs={"class":"last"}).text
        row = [sub1text,sub1href,sub2text,sub2href,author,lastupdate]
        download.append(row)
# 现在爬取的数据都在download列表里面，现在将信息写入到excel里面
wb = Workbook()
# 设置Excel文件名
dest_filename = 'guba4.xlsx'
# 新建一个表
ws1 = wb.active
# 设置表头
titleList = ["标题吧名",'吧名链接', '标题内容', '内容链接', '作者', '更新时间']
for row in range(len(titleList)):
    c = row + 1
    ws1.cell(row=1, column=c, value=titleList[row])

# 填写表内容
for listIndex in range(len(download)):
    ws1.append(download[listIndex])

wb.save(filename=dest_filename)


