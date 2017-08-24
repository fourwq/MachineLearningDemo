#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 02:05:42 2017

@author: weiqiang

这个文件用来介绍list的常用操作
"""
I = [1,2,3,5]
J = ["meat","fruit","egg"]
K = [1, False, "egg"]

#修改list中的元素
J[2]=3
print(J)

J.append(5)
print(J)

del J[2]
print(J)

print("先创建一个基础的list")
L1 = [1, 2, 5, 3, 6, 8, 4]
L1 = list(range(20))
print("list = "+str(L1))

print(" 打印list[0:]="+str(L1[0:]))
print(" 打印list[1:]="+str(L1[1:]))
print(" 打印list[:-1]="+str(L1[:-1]))
print(" 打印list[3:-2]="+str(L1[3:-2]))
print(" 打印list[::2]="+str(L1[::2]))
print(" 打印list[2::]="+str(L1[2::]))
print(" 打印list[2::2]="+str(L1[2::2]))
print(" 打印list[::-1]="+str(L1[::-1]))