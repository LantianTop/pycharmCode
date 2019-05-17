#!/user/bin/env python
# -*- coding:utf-8 -*-
# @Author:  blueSky
# @Time: 2019年04月25日07时41分59秒

def BMI(high,weight):
    return  weight/(high*high)
bmi=BMI(1.75,80.5)
if(bmi<18.5):
    print("过轻")
elif(18.5<=bmi<25):
    print("正常")
elif(25<=bmi<28):
    print("过重")
elif(28<=bmi<32):
    print("肥胖")
else:
    print("严重肥胖")

