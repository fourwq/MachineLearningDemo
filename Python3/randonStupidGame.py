#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 19:23:49 2017

@author: weiqiang
"""
from random import randint


num = randint(1, 100)
#print(num)
#print("guess what i think?")
#inputStr = input()
#answer = int(inputStr)
needStop = False

while not needStop:
    print("guess what i think?")
    _inputStr = input()
    answer = int(_inputStr)
    
    if answer > num:
        print("too big")
    if answer < num:
        print("too small")
    if answer == num:
        print("yes equal!")
        needStop = True