# -*- coding: utf-8 -*-
'''
Created on 2018年2月1日

@author: Jeff Yang
'''

import re

ma = re.match(r'{..}', '{0b}')
print(ma.group())

ma = re.match(r'{[a-zA-z0-9]}', '{8}')
print(ma.group())

ma = re.match(r'\[[\w]\]', '[8]')  # \w相当于[a-zA-z0-9]，‘[]’需要转义
print(ma.group())

ma = re.match(r'\D', 'p')  # 匹配非数字
print(ma.group())

print('\n')
ma = re.match(r'[A-Z][a-z]*', 'Dadscsd333a')
print(ma.group())  # Dadscsd
