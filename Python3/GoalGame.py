#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 02:21:19 2017

@author: weiqiang
"""

from random import choice
point = [0,0]

directions = ["left","middle","right"]


def kickOnece():   
#    print("choose one side to shoot: "+str(directions))
    #    direction = input()
    direction = choice(directions)
#    print("you kick: "+direction)
    
    goalKeeper = choice(directions)
#    print("computer save direction: "+goalKeeper)
    if direction!=goalKeeper:
#        print("goal")
        point[0]+=1
        return True
    else:
#        print("oops")   
        point[1]+=1
        return False



for i in range(100000):
   kickOnece()
   
        
print("result you get: %d, Keeper get %d."%(point[0], point[1]))

