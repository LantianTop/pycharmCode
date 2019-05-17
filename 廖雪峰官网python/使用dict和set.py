#!/user/bin/env python
# -*- coding:utf-8 -*-
# @Author:  blueSky
# @Time: 2019年04月26日10时11分54秒

# 问题描述将列表中的重复元素输出为字典使得显示出每个元素的个数
# 方案1，采用get方法
# str_list = ['a', 'a', 'b', 'a', 'b', 'c']
# dic = {}
# for name in str_list:
#     result = dic.get(name, -1)
#     if result == -1:
#         dic[name] = 1
#     else:
#         dic[name] = dic[name] + 1
# print(dic)

# 方案二
str_list = ['a', 'a', 'b', 'a', 'b', 'c']
dic = {}
for i in str_list:
    if str_list.count(i) >= 1:
        dic[i] = str_list.count(i)
print(dic)