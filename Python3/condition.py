#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 19:02:23 2017

@author: weiqiang
"""

num = 50
print("guess what i think?")
inputStr = input()
answer = int(inputStr)

if answer > num:
    print("too big")
if answer < num:
    print("too small")
if answer == num:
    print("yes equal!")