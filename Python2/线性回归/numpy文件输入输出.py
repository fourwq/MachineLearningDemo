#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 15:48:05 2017

@author: camera1
"""

import numpy as np
# 
# 
#将数据以numpy的私有格式（.npy）保存
#可以连续进行存放和读取多个数据，但是无法使用其他工具查看

a  = np.arange(8)
b  = np.add.accumulate(a)
c  = a +b

f = file('test.npy','wb')

np.save(f,a)
np.save(f,b)
np.save(f,c)

f.close()

f = file('test.npy','rb')

d = np.load(f)
e = np.load(f)
g = np.load(f)

f.close()

#保存为可查看数据,无法连续保存
#可以设置保存格式，默认为%0.18e(这个进度会比较长)
#np.savetxt('a.txt',a,fmt='%f'）

np.savetxt('a.txt',a)

k = np.loadtxt('a.txt')

print(k)

#