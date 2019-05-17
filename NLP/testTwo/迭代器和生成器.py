#!/user/bin/env python
# -*- coding:utf-8 -*-
# @Author:  blueSky
# @Time: 2019年04月24日21时02分58秒

# import  sys
# list=[1,2,3,4,5,6];
# it=iter(list)
#
# while True:
#     try:
#         print(next(it))
#     except StopIteration:
#         sys.exit()

#创建一个迭代器

# class MyNumbers:
#     def __iter__(self):
#         self.a=1;
#         return  self;
#     def __next__(self):
#         x=self.a;
#         self.a+=1;
#         return x;
# myclass=MyNumbers();
# myiter=iter(myclass)
# i=1;
# while i<=5:
#     print(next(myiter));
#     i+=1;
# # 生成器
"""
在 Python 中，使用了 yield 的函数被称为生成器（generator）。
跟普通函数不同的是，生成器是一个返回迭代器的函数，只能用于迭代操作，更简单点理解生成器就是一个迭代器。
在调用生成器运行的过程中，每次遇到 yield 时函数会暂停并保存当前所有的运行信息，返回 yield 的值, 
并在下一次执行 next() 方法时从当前位置继续运行。
调用一个生成器函数，返回的是一个迭代器对象
"""
import  sys
# 斐波那契数列
def fibonacci(n):
    a,b,counter=0,1,0;
    while True:
        if(counter>n):
            return
        yield a
        a,b=b,a+b
        counter+=1;
f=fibonacci(10)
while True:
    try:
        print(next(f),end=" ")
    except StopIteration:
        sys.exit()