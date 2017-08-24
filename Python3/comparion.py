#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 18:44:48 2017

@author: weiqiang
"""

num = 10
print('guess what i think?')
answer1 = input()
answer = int(answer1)

result = answer < num
print('too small')
print(result)

result = answer > num
print('too big')
print(result)

result = answer==num
print('yes equal!')
print(result)
