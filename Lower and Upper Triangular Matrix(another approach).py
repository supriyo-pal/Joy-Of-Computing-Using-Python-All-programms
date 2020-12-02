# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 12:36:38 2020

@author: Supriyo
"""

n=int(input()) #taking the dimention
l=[]
for i in range(n):
    for j in range(1):
        temp=[int(g) for g in input().split()] #taking the input of elements separating by space
        l.append(temp)


for i in range(n):
    for j in range(n):
        if i<j:
            if j==n-1:
                print(0,end="")
            else:
                print(0,end=" ")
        else:
            if j==n-1:
                print(l[i][j],end="")
            else:
                print(l[i][j],end=" ")
        
    if i!=n-1:
      print()