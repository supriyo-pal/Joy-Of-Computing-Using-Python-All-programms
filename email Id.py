# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 13:42:15 2020

@author: Supriyo
"""

y=input()
y=list(y)
c=""

for i in range(y.index("@")+1,y.index(".")):
    c=c+y[i]
print(c)