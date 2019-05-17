#!/user/bin/env python
# -*- coding:utf-8 -*-
# @Author:  blueSky
# @Time: 2019年05月15日13时52分29秒
from  bs4 import BeautifulSoup
# 写入Excel需要使用的库
from openpyxl import Workbook
import urllib.request
urlstart = 'http://my.yingjiesheng.com/index.php/personal/xjhinfo.htm/?page='
urlend = '&cid=&city=21&word=&province=0&schoolid=&sdate=&hyid=0'
download=[]
#开始爬取数据，计划爬取12页
for i in range(1,80):
    url=urlstart+str(i)+urlend
    print("正在打印："+url)
    resq=urllib.request.urlopen(url)
    html=resq.read()
    bs=BeautifulSoup(html,"html5lib",from_encoding="gbk")
    alllist1=bs.find_all("tr",attrs={"class":"bg0"})
    alllist2=bs.find_all("tr",attrs={"class":"bg1"})
    alllist=alllist1+alllist2
    # 对数据进行处理撒选
    for contenttd in alllist:
        country=contenttd.find("td",width="80").find("a").text
        month = contenttd.find('td', width='120').text
        companyweb = contenttd.find('td', width='250').find('a').get('href')
        if 'http' not in companyweb:
            companyweb = 'http://my.yingjiesheng.com/' + str(companyweb)
        companyName = contenttd.find('td', width='250').find('a').text
        school = contenttd.find('td', width='250').next_sibling.next_sibling.text
        classRoom = contenttd.find('td', width='250').next_sibling.next_sibling.next_sibling.next_sibling.text
        row = [country,month, companyweb, companyName, school, classRoom]
        download.append(row)
# 现在爬取的数据都在download列表里面，现在将信息写入到excel里面
wb = Workbook()
# 设置Excel文件名
dest_filename = 'UserInfoFile1.xlsx'
# 新建一个表
ws1 = wb.active

# 设置表头
titleList = ["城市",'时间', '网址', '招聘企业', '学校', '地址']
for row in range(len(titleList)):
    c = row + 1
    ws1.cell(row=1, column=c, value=titleList[row])

# 填写表内容
for listIndex in range(len(download)):
    ws1.append(download[listIndex])

wb.save(filename=dest_filename)