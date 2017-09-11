#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 17:25:49 2017

@author: camera1
"""

import numpy as np
from numpy import mat



a = [[1,2,3],[4,5,6]]
A = np.array(a)
b = [1,2,3]
B = np.array(b)
B = B.reshape((1,3))
Bt = B.reshape((3,1))

#矩阵求逆
M = np.array([[3,4],[2,16]])

A_inverse = np.invert(M)



#矩阵转置

AT = np.transpose(A)


print np.dot(B[:,:-1],A)




