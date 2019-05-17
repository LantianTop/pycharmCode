#!/user/bin/env python
# -*- coding:utf-8 -*-
# @Author:  blueSky
# @Time: 2019年04月27日22时25分02秒


# # 查看python中所有关键字
# import  keyword
# print(keyword.kwlist)
#
# # python3中数字有四种类型:整数，布尔型，浮点型和复数
# # 使用r可以让反斜杠不转义
# print(r"this is a line with\n")
# print("this is a line with\n")

"""
python中单引号和双引号使用完全相同。
使用三引号可以指定一个多行字符串。
转义符 '\'
反斜杠可以用来转义，使用r可以让反斜杠不发生转义。。 如 r"this is a line with \n" 则\n会显示，并不是换行。
按字面意义级联字符串，如"this " "is " "string"会被自动转换为this is string。
字符串可以用 + 运算符连接在一起，用 * 运算符重复。
Python 中的字符串有两种索引方式，从左往右以 0 开始，从右往左以 -1 开始。
Python中的字符串不能改变。
Python 没有单独的字符类型，一个字符就是长度为 1 的字符串。
字符串的截取的语法格式如下：变量[头下标:尾下标:步长]
word = '字符串
"""
# str="LanTianDream"
# print(str[0:-1])
# print(str*2)

# # print输出默认是换行的，要想不换行需要在变量末尾加上 end="":
# x="a"
# y="b"
# print(x,end=" ")
# print(y,end=" ")
# print("----------------")

# python3中赋值后不可变类型：
# Number,String,Tuple()元组中元素类型可以不相同

# 可变类型:List[],Dictionary{},Set(){}
# #set数据类型测试
# student={"Tom","Jim","Mary","Tom","Jack","Rose"}
# print(student)

# 加了星号 * 的参数会以元组(tuple)的形式导入，
# 存放所有未命名的变量参数。
# def printinfo(arg1,*vartuple):
#     print("输出：")
#     print(arg1)
#     for var in vartuple:
#         printinfo(var)
#     return
# printinfo(70,50,70)
# # 加了两个**的参数会以字典的形式导入
# def printinfo(arg1,**vardivt):
#      print("输出：")
#      print(arg1)
#      print(vardivt)
# printinfo(1,a=2,b=4)
#
# # 如果单独出现星号*后的参数必须用关键字传入
# def f(a,b,*,c):
#     return a+b+c
# # print(f(1,2,3)这样输出就会报错
# print(f(1,2,c=3))
# # 当内部作用域想修改外部作用域的变量时，
# # 就要用到global和nonlocal关键字了。

num=1
def fun1():
    global num
    print(num)
    num=123
    print(num)
fun1()
print(num)