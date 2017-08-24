#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 08:39:16 2017

@author: camera1
"""

import matplotlib.pyplot as plt
import numpy as np

#3D图标必须的模块，project=‘3D'的定义

from mpl_toolkits.mplot3d import Axes3D

np.random.seed(42)

n_grids = 51

c = n_grids/2


nf = 2

#生成格点
x = np.linspace(0,1,n_grids)
y = np.linspace(0,1,n_grids)


#x和y是长度为n_grids的array
#meshgrid会把x和y组合成n_grids*g_grids的array，X和Y对应位置就是所有的格点坐标

X,Y = np.meshgrid(x,y)

#生成一个0值的傅里叶谱
spectrum = np.zeros((n_grids, n_grids),dtype=np.complex)

#生成一段噪声，长度是（2*nf+1）**2/2
noise = [np.complex(x,y) for x,y in np.random.uniform(-1, 1,((2*nf+1)**2/2,2))]

#傅里叶频谱的每一项和其共轭关于中心对称
noisy_block = np.concatenate((noise,[0j],np.conjugate(noise[::-1])))

#将生成的频谱作为低频成分
spectrum[c-nf:c+nf+1, c-nf:c+nf+1] = noisy_block.reshape((2*nf+1, 2*nf+1))


#进行反傅里叶变换
Z = np.real(np.fft.ifft2(np.fft.ifftshift(spectrum)))
#创建图表

fig = plt.figure("3D Surface &wire")

ax = fig.add_subplot(1,2,1,projection = '3d')

#alpha是定义透明度，cmap是color map
#rstride和cstride是两个方向上的采样，越小越精细，lw是线宽

ax.plot_surface(X,Y,Z,alpha=0.7, cmap='jet',rstride=1, cstride = 1, lw = 0)

ax = fig.add_subplot(1,2,2,projection='3d')

ax.plot_surface(X,Y,Z,rstride=3, cstride = 3, lw = 0.5)

plt.show()








