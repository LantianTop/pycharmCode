#!/user/bin/env python
# -*- coding:utf-8 -*-
# @Author:  blueSky
# @Time: 2019年05月14日19时19分53秒
from __future__ import  division
import nltk,re,pprint
import urllib.request

url="http://bg.f4ff.cn/"
resq=urllib.request.urlopen(url)
html=resq.read()
print(html)
