# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 11:19:06 2020

@author: Supriyo
"""

def getMissingNo(A): 
    n = len(A) 
    total = (n + 1)*(n + 2)/2
    sum_of_A = sum(A) 
    return total - sum_of_A 
  
# Driver program to test the above function 
#A = [1, 2, 4, 5, 6] 
# Below line read inputs from user using map() function  
A = list(map(int,input("\nEnter the numbers : ").strip().split()))
miss = getMissingNo(A) 
print(int(miss)) 
# This code is contributed by Pratik Chhajer 