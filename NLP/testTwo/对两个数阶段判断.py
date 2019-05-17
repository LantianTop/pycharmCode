#!/user/bin/env python
# -*- coding:utf-8 -*-
# @Author:  blueSky
# @Time: 2019年04月25日08时24分30秒
def dayin(a,b):
    try:
        sum = a / b
        if(b==0):
            raise ZeroDivisionError("除数为0异常")
        if(type(a)==int):
            if(type(b)==int):
                return  sum
            raise ValueError("输入的值异常")
        else:
            raise ValueError("输入的值异常")
    except ZeroDivisionError:
            print("除数不能为0哦！这样不好的")
    except ValueError:
            print("输入的应该为有效数")

ce=dayin(1,5.2)
print(ce)


