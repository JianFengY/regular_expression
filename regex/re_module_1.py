# -*- coding: utf-8 -*-
'''
Created on 2018年1月30日

@author: Jeff Yang
'''

import re

str1 = 'test python'

print(str1.find('ww'))  # 找不到返回-1
print(str1.find('s'))  # 返回索引

print('\n')
pa = re.compile(r'test')  # r表示元字符串，不转义
print(type(pa))  # <class '_sre.SRE_Pattern'>，一个pattern实例
ma = pa.match(str1)
print(ma.group())  # test
print(ma.span())  # (0, 4)

print('\n')
pa = re.compile(r'test', re.I)
print(pa)  # re.compile('test', re.IGNORECASE)，忽略大小写
ma = pa.match('TeSt python')
print(ma.group())  # TeSt
ma = pa.match('test python')
print(ma.group())  # test
print(ma.groups())  # ()，空元组

print('\n')
pa = re.compile(r'(test)')
ma = pa.match(str1)
print(ma.group())  # test
print(ma.groups())  # ('test',)，返回元组

print('\n')
ma = re.match(r'test', 'test python')
print(type(ma))  # <class '_sre.SRE_Match'>
print(ma.group())  # test

print('\n')
ma = re.match(r'[\w]{4,6}@(163|126).com', 'test@126.com')
print(ma.group())  # test@126.com

print('\n')
ma = re.match(r'<([\w]+>)', '<book>')
print(ma.group())  # <book>
print(ma.groups())  # ('book>',)
ma = re.match(r'<([\w]+>)\1', '<book>book>')  # 引用编号为1的分组匹配到的字符串，也就是“book>”
print(ma.group())  # <book>book>
