#!/user/bin/env python
# -*- coding:utf-8 -*-
# @Author:  blueSky
# @Time: 2019年05月02日10时45分12秒
import  jieba
txt=open("《红楼梦》完整版.txt","r",encoding="utf-8")
extends=[ "：", "!", "、", "”", "“", "。", "？", ","]
words=jieba.lcut(txt.read())   # 调用jieba库进行精准分词,jieba需要的参数是一个字符串而不是一个文件
count={} # 创建一个字典数据类型
sum=len(words);    #统计总数值
for rword in words:
    count[rword]=count.get(rword,0)+1  #Python 字典(Dictionary) get() 函数返回指定键的值，如果值不在字典中返回默认值。
for rword in extends:
    if not count.get(rword):
         continue;
    else:
        del count[rword]
items=list(count.items())
items.sort(key=lambda x:x[1],reverse=True)
f=open("./1.txt","w")
for i in range(6000):
     print("{0:<10}{1:>5}".format(items[i][0],items[i][1]/sum))
     f.write("{0:<10}\t{1:>5}\n".format(items[i][0],items[i][1]/sum))
f.close()

