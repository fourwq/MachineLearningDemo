#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 22:19:24 2017

@author: weiqiang
"""
class MyClass:
    name = "sam"
    def sayHi(self):
        print("hello "+self.name)
        
mc = MyClass()
mc.name = "lili"
mc.sayHi();