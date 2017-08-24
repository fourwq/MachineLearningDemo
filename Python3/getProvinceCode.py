#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 21:31:52 2017

@author: weiqiang
"""

from urllib import request
url = 'http://m.weather.com.cn/data5/city.xml'
content = request.urlopen(url).read()
print(content.decode("utf8"))