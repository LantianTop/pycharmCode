#!/user/bin/env python
# -*- coding:utf-8 -*-
# @Author:  blueSky
# @Time: 2019年04月30日19时32分52秒
import  jieba
txt=open("《红楼梦》完整版.txt","r",encoding="utf-8")
words=jieba.lcut(txt.read())
counts={} #新建一个字典
for word in words:
    counts[word]=counts.get(word,0)+1
item=list(counts.items())
item.sort(key=lambda x:x[1],reverse=True)
for i in range(20):
    print("{0:<10}{1:>5}".format(item[i][0],item[i][1]))
