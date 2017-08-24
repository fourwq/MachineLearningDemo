#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 16:15:49 2017

@author: camera1
"""
def funAsParam(x, y, f):
    return f(x, y)

fun = lambda x,y,z: x+y+z

print(fun(1,2,3))

print(funAsParam(3,3, lambda x,y: x**y))