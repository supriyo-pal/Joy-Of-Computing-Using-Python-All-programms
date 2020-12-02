# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 11:11:40 2020

@author: Supriyo
"""
a=input()
def canMakeAllSame(a): 
    zeros = 0
    ones = 0
  
    # Traverse through given string and 
    # count numbers of 0's and 1's 
    for i in range(0, len(a)): 
        ch = a[i]; 
        if (ch == '0'): 
            zeros = zeros + 1
        else: 
            ones = ones + 1
  
    # Return true if any of the two 
    # counts is 1 
    return (zeros == 1 or ones == 1); 
  
# Driver code 
if(canMakeAllSame(a)): 
    print("Yes\n") 
else: 
    print("No\n") 