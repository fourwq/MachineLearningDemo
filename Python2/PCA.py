#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 14:14:26 2017

@author: camera1
"""
from numpy import *

def pca(dataMat, dimen):
    meanVals = mean(dataMat, axis = 0)
    meanRemoved = dataMat - meanVals
    covMat = cov(meanRemoved, rowvar = 0)
    Vals, Vects = linalg.eig(mat(covMat))
    ValInd = argsort(Vals)
    ValInd = ValInd[:-(topNfeat+1):-1]
    redEigVects = Vects[:,ValInd]
    lowDDataMat = meanRemoved * redEigVects
    return lowDDataMat