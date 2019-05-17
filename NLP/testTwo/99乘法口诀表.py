#!/user/bin/env python
# -*- coding:utf-8 -*-
# @Author:  blueSky
# @Time: 2019年04月25日08时10分02秒

def hello99():
    for i in range(1,10):
        for j in range(1,10):
            if(i>=j):
                print("%s*%s=%s"%(i,j,i*j),end=" ")
        print()


i=hello99()

