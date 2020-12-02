# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 13:55:41 2020

@author: Supriyo
"""
#iterative version
def factorial(num):
    product=1
    for i in range(1,num+1):
        product=product*i
    return product

num=int(input("enter a number "))
if num<0:
    print("negetive number is not allowed")
else:
    f=factorial(num)
    print("factorial of ", num," is ",str(f))

   