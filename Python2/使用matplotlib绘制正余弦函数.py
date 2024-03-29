#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 15:02:00 2017

@author: camera1
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,10,num=1000)
y = np.sin(x)
z = np.cos(x**2)


plt.figure(figsize=(10,2))
plt.plot(x,y,label='$sin(x)$',color='red',linewidth=2)
#plt.plot(x,z,"b--",label = '$cos(x^2)$')
plt.xlabel('Time(s)')
plt.ylabel('Volt')
plt.title('PyPlot First Example')
plt.ylim(-1.2,1.2)
plt.legend()




plt.show()