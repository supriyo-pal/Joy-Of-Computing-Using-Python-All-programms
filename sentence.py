# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 13:19:51 2020

@author: Supriyo
"""

num=int(input("How Many lines to be entered :"))
getpythoncode=list()

for gpc in range(num):
    getpythoncode.append(input().upper())

for f in range(len(getpythoncode)):
    if f!=len(getpythoncode)-1:
        print(getpythoncode[f])
    else:
        print(getpythoncode[f],end="")