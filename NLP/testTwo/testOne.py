#!/user/bin/env python
# -*- coding:utf-8 -*-
# @Author:  blueSky
# @Time: 2019年04月24日19时52分06秒

str1="这是一个变量"
print("变量str1都值是："+str1)
print("变量str1的地址是：%d" %(id(str1)))
str2=str1
print("变量str2都值是："+str2)
print("变量str2的地址是：%d" %(id(str2)))
str1 = "这是另一个变量"
print("变量str1的值是："+str1)
print("变量str1的地址是：%d" %(id(str1)))
print("变量str2的值是："+str2)
print("变量str2的地址是：%d" %(id(str2)))
