# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 21:56:43 2020

@author: Supriyo
"""

import numpy as np
import random
a=np.array([1,2,3])
print(a)
print(type(a))
print(a.shape)

b=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(b)
print(type(b))
print(b.shape)

c=np.zeros((3,3))
print(c)
print(type(c))
print(c.shape)

d=np.ones((3,3))
print(d)
print(type(d))
print(d.shape)

e=np.full((3,3),6)
print(e)
print(type(e))
print(e.shape)

f=np.random.random((3,3))
print(f)
print(type(f))
print(f.shape)