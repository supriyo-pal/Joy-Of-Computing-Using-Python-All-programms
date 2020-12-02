# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 20:14:25 2020

@author: Supriyo
"""

def Rotate(matrix):
    if not len(matrix):
        return 
    top=0
    bottom=len(matrix)-1
    left=0
    right=len(matrix[0])-1
    
    while left<right and top<bottom:
        previous=matrix[top+1][left]
        
        for i in range(left,right+1):
            temp=matrix[top][i]
            matrix[top][i]=previous
            previous=temp
        top+=1
        
        for i in range(top,bottom+1):
            temp=matrix[i][right]
            matrix[i][right]=previous
            previous=temp
        right-=1
        for i in range(right,left-1,-1):
            temp=matrix[bottom][i]
            matrix[bottom][i]=previous
            previous=temp
            
        bottom-=1
        for i in range(bottom,top-1,-1):
            temp=matrix[i][left]
            matrix[i][left]=previous
            previous=temp
        left+=1
    return(matrix)


l=[]
ans=int(input())

for i in range(ans):
    part1=[x for x in input().split()]
    l.append(part1)
r1=[Rotate(l)]

for i in range(ans-1):
    print(' '.join(l[i]))
print(' '.join(l[ans-1]),end="")







