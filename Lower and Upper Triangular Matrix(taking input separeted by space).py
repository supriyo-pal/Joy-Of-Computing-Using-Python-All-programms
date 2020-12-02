# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 11:47:11 2020

@author: Supriyo
"""

matrix=[]
element=int(input())
row=element
col=element
for i in range (row):
    a=[]
    for j in range(1):
        #a.append(list(map(int,input("\nEnter the numbers : ").strip().split())))
        temp=[int(g) for g in input().split()]
        matrix.append(temp)
             
def lower(matrix,row,col):
    for i in range(row):
        for j in range(col):
            if i<j:
                print("0",end=" ")
            else:
                print(matrix[i][j],end=" ")
        print(" ")
def upper(matrix,row,col):
    for i in range(row):
        for j in range(col):
            if i>j:
                print("0",end=" ")
            else:
                print(matrix[i][j],end=" ")
        print(" ")
        
print("lower triangular matrix")        
lower(matrix, row, col)
print("upper triangular matrix")
upper(matrix, row, col)        