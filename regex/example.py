# -*- coding: utf-8 -*-
'''
Created on 2018年1月30日

@author: Jeff Yang
'''

import re
from urllib.request import urlopen

req = urlopen('https://www.imooc.com/course/list')
buf = req.read().decode()

urls = re.findall(r'src="(//.+\.jpg)"', buf)
i = 0
for url in urls:
    print('Downloading: https:' + url)
    with open('images\\' + str(i) + '.jpg', 'wb')as f:
        req = urlopen('https:' + url)
        buf = req.read()
        f.write(buf)
        i += 1
print('Done!')