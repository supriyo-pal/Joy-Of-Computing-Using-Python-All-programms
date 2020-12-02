# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 13:11:24 2020

@author: Supriyo
"""
rotate_array=[]
def rotate(array):
    #rotated array will be stored here
    for i in range(len(array)):
        rotate_array.append([])
    for i in range(len(array)):
        for j in range(len(array)):
            rotate_array[i].insert(0,array[j].pop(0))#for clock wise
           # rotate_array[i].append(array[j].pop(-1))#for anti clockwise
    return rotate_array

# array=[[1,2,3],[4,5,6],[7,8,9]]
# print("Before rotation:\n")
# for i in array:
#     print(i)
# print("\n")
# print("After rotation\n")
# myNewArray=rotate(array)

# for i in myNewArray:
#     print(i)


a=int(input("enter the dimention"))

count=1
array = []
for i in range(1,a+1):
    l = []
    for j in range(1,a+1):
        l.append(count)
        count+=1
    array.append(l)

for i in range(a):
    for j in range(a):
        if(j==a-1):
            print(array[i][j], end="")
        else:
            print(array[i][j], end=" ")
    if(i!=a-1):
        print()
        
for i in range(a):
    for j in range(a):
        if(j==a-1):
            print(rotate_array[i][j], end="")
        else:
            print(rotate_array[i][j], end=" ")
    if(i!=a-1):
        print()
rotate(array)