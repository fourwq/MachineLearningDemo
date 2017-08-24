#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 12:34:44 2017

@author: weiqiang
"""

from urllib import request
import json

url = "http://www.weather.com.cn/data/cityinfo/101010100.html"
content = request.urlopen(url).read()
print(content.decode("utf8"))
data = json.loads(content)
print(type(content))
print(type(data))


result = data['weatherinfo']
print(result['city'])
