# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 11:10:47 2020

@author: Supriyo
"""
a = list(map(int,input("\nEnter the numbers : ").strip().split()))
def move_zero(num_list):
    a = [0 for i in range(num_list.count(0))]
    x = [ i for i in num_list if i != 0]
    x.extend(a)
    return(x)
call=move_zero(a)
print(*call,sep=' ')