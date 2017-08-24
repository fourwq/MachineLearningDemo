#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 12:23:07 2017

@author: weiqiang
"""

from urllib import request

response = request.urlopen(r'https://www.baidu.com/')

page = response.read()
#page = page.decode('utf-8')

f = open("baidu.html",'w')
f.write(page)
f.close()