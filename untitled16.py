# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 12:45:47 2020

@author: Supriyo
"""
l1=[1,2,3,4,5]
l2=[1,4,6,12]

l=[]
for i in l1:
    for j in l2:
        if i==j:
            l.append(i)
print(l)


import numpy as np
import random
m=np.array([[9,10,11],[19,20,21]])

print(m.T)

p=[[1,2,3],[4,5,6]]
print(np.sum(p,axis=1))
b=np.random.randint(1,5,(2,5))
print(b)

print('Chennai and Madras are same.Madras and Chennai are same.Chennai=Madras, Madras=Chennai'.replace('Madras','Chennai',2))