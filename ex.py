# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 13:16:47 2020

@author: Supriyo
"""

import numpy
mat=numpy.array([[1,2,3],[4,5,6],[7,8,9]])

def add(mat):
    sum=0
    for i in range(2):
        for j in range(2):
            if i==j:
                sum=sum+mat[i][j]
               #print(mat[i][j])
    return sum
print(add(mat))