# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 13:03:37 2020

@author: Supriyo
"""

with open('file.txt','w') as f:
    
    f.write("I love you");
f.close()

with open('file.txt','r') as f1:
    result=f1.read()
    print(result)
f1.close()