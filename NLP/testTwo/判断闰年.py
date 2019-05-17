#!/user/bin/env python
# -*- coding:utf-8 -*-
# @Author:  blueSky
# @Time: 2019年04月24日21时36分27秒
while True:
    year=int(input("请输入想要查询的年份(比如2008):"))
    if(year%4==0):
        if(year%100==0):
            if(year%400==0):
                print("{0}是闰年".format(year))
            else:
                print("{0}不是闰年".format(year))
        else:
            print("{0}是闰年".format(year))
    else:
        print("{0}不是闰年".format(year))


