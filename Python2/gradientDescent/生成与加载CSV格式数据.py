#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 11:02:31 2017

@author: camera1
"""
import csv


#写入数据，一维数据用writerow，二维数据用writherows方法
a = [[1,2],[3,4]]
b = (5,6)

#with open('egg2.csv','wb') as csvfile:
#    spamwriter = csv.writer(csvfile, dialect='excel')
#    spamwriter.writerows(a)
    
#读取数据

with open('egg2.csv','rb') as f:
    reader = csv.reader(f)
#    print('dialect')
#    print(reader.dialect)
#    print('line num')
#    print(reader.line_num)
#    print('next()')
#    print(reader.next())
#    
#    print('reader')
#    print(reader)
    a = []
    
    for row in reader:
        a.append([float(x) for x in row])
    
    print(a)