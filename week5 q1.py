# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 22:06:50 2020

@author: Supriyo
"""
def printDict():
    dictionary=dict()
    n=int(input("enter a number :"))
    for i in range(1,n+1):
        dictionary[i]=i*i
    print(dictionary)
printDict()