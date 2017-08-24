#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 19 15:39:12 2017

@author: camera1
"""

def factorial(num):
    if num==1:
        return 1
    else:
        return num*factorial(num-1)
    
num = int(input("input a number!"))

print(factorial(num))
    