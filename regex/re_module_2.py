# -*- coding: utf-8 -*-
'''
Created on 2018年1月30日

@author: Jeff Yang
'''

import re

str1 = 'imooc videonum = 1000'
print(str1.find('1000'))

info = re.search(r'\d+', str1)  # 匹配数字
print(info.group())

str2 = 'c++=100, java=90, python=80'
info = re.search(r'\d+', str2)  # 只能匹配出100
print(info.group())

info = re.findall(r'\d+', str2)  # 匹配所有符合的字符
print(info)  # ['100', '90', '80']
print(sum([int(x) for x in info]))

str3 = 'imooc videonum = 1000'
info = re.sub(r'\d+', '1001', str3)  # 替换字符串中符合正则的部分
print(info)  # imooc videonum = 1001


def add1(match):
    """接收match对象给指定值加1"""
    val = match.group()
    num = int(val) + 1
    return str(num)


print('\n' + str3)
info = re.sub(r'\d+', add1, str3)
print(info)

print('\n')
str4 = 'Courses:C C++ Java Python,C#'
info = re.split(r':| |,', str4)  # 以冒号或空格或逗号分割字符串
print(info)  # ['Courses', 'C', 'C++', 'Java', 'Python', 'C#']
