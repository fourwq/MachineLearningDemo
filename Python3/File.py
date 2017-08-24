#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 10:09:07 2017

@author: weiqiang
"""

import os

os.mkdir("testdir2")

f = open('testdir2/StrData.txt','w')

s = input()

f.write(s)


f.close()



    