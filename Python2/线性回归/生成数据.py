#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 15:23:50 2017

@author: camera1
"""

import numpy as np

import matplotlib.pyplot as plt

NUM_POINTS = 200

VALUE_RANGE = 10

pointArray = np.random.random(size=(NUM_POINTS,2))*10


#plt.plot(pointArray[:,0],pointArray[:,1],'b*')


filteredData = []

for item in pointArray:
  
    if not((item[0]>(item[1]*2+2)) or  (item[1]>(item[0]*2+1))):
        filteredData.append(item)
    
m = np.array(filteredData)

plt.plot(m[:,0],m[:,1],'r+')

np.savetxt('linearRegressionData.txt',m)

n = np.loadtxt('linearRegressionData.txt')

plt.plot(n[:,0],n[:,1],'b*')