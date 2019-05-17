#!/user/bin/env python
# -*- coding:utf-8 -*-
# @Author:  blueSky
# @Time: 2019年05月01日10时04分32秒
import jieba
import  time
t1=time.time()
text="""
    卜算子·我住长江头
宋代：李之仪
我住长江头，君住长江尾。日日思君不见君，共饮长江水。
此水几时休，此恨何时已。只愿君心似我心，定不负相思意。
"""
words=jieba.lcut(text)
t2=time.time()
# print(words)
counts={} #新建一个字典
for word in words:
    if len(word)==1:
        continue
    else:
        rword=word
    counts[rword]=counts.get(rword,0)+1
item=list(counts.items())
item.sort(key=lambda x:x[1],reverse=True)
for item1 in item:
    word,count=item1
    print("{0:<10}{1:>5}".format(word,count))
