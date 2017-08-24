#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 15:51:28 2017

@author: camera1

线性可分数据存储于 线性可分数据.txt


"""


import numpy as np

import matplotlib.pyplot as plt

NumOfPoint = 200

ValueRange = 10

pointArray = np.random.random(size=(NumOfPoint,2))*ValueRange


upper = []

lower = []

for item in pointArray:
  
    if item[0]>(item[1]+1):
        lower.append(item)
    elif item[0]<(item[1]-1):
        upper.append(item)

m = np.array(upper)
n = np.array(lower)   

       

x = m[:,0]
y = m[:,1]

u = n[:,0]
v = n[:,1]

#x = np.random.random(200)*10
#y = np.random.random(200)*10


plt.figure(figsize=(8,8))

plt.plot(x,y,'b*',u,v,'r*',[0.0, ValueRange],[0.0,ValueRange],'g')

plt.show()