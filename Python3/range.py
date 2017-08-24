#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 09:05:52 2017

@author: weiqiang

这个文件用来介绍python中range方法的用法
"""
#################################################
print("range的基本用法：range(1,5) = ",end='')
r1 = range(1,5) #代表从1到5(不包含5)
print(list(r1))
#[1, 2, 3, 4]
#################################################
print("range的基本用法：range(1,5,2) = ",end='')
r2 = range(1,5,2) #代表从1到5，间隔2(不包含5)
print(list(r2))
#[1, 3]
#################################################
print("range的基本用法：range(5) = ",end='')
r3 = range(5) #代表从0到5(不包含5)
print(list(r3))
#[0, 1, 2, 3, 4]



