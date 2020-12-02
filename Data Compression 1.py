# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 00:40:54 2020

@author: Supriyo
"""

import numpy as np
x=np.array([1.0,2.0])
print(x.dtype)

y=np.array([1.0,2.0],dtype=np.int64)
print(y.dtype)

z=np.array([[1,2],[3,4]],dtype=np.float64)
z1=np.array([[5,6],[7,8]],dtype=np.float16)
print(z.dtype)
print(z1.dtype)
print(z+z1)
print(np.add(z,z1))
print(z-z1)
print(np.subtract(z,z1))
print(np.multiply(z,z1))
print(np.sqrt(z))
print(np.transpose(z))

print(np.sum(z,axis=0))
print(np.sum(z,axis=1))

