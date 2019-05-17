#!/user/bin/env python
# -*- coding:utf-8 -*-
# @Author:  blueSky
# @Time: 2019年04月25日07时56分58秒

def n(n):
    sum=1;
    counter=1;
    while n>0:
        sum+=1/(counter*counter)
        counter+=1;
        n-=1;
    return sum
ceshi=n(int(input("请输入一个正整数")))
print(ceshi)
