# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 22:17:25 2020

@author: Supriyo
"""

# Python code to remove duplicate elements 
final_list = [] 
def Remove(duplicate): 
   
    for num in duplicate: 
        if num not in final_list: 
            final_list.append(num) 
    return final_list 
      
# Driver Code 
#duplicate = []
# n=int(input("enter the elements of the list :"))
# for i in range(0,n):
#     element=int(input())
#     duplicate.append()
duplicate = list(map(int,input("\nEnter the numbers : ").strip().split()))
result=Remove(duplicate)
for i in result:
#     print(final_list[i])
    print(i," ",end="")