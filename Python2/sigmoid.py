#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 17:25:12 2017

@author: camera1
"""

import numpy as np

def sig(x):
    '''
    sigmoid 函数
    '''
    return 1.0/(1+np.exp(-x))

