# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 11:54:38 2020

@author: Supriyo
"""
rows=int(input("enter number of rows"))

for row in range(1,rows+1):
    for column in range(1,row+1):
        print(column,end=" ")
    print(" ")
        
    
