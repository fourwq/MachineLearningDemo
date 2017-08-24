#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 16:32:42 2017

@author: camera1
"""

import numpy as np

import matplotlib.pyplot as plt

#导入并查看数据

data = np.loadtxt('linearRegressionData.txt')

plt.plot(data[:,0],data[:,1], 'b+')

