# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 20:49:11 2020

@author: Supriyo

base case or anchor case :
    point where the recursion stops
"""

def factorial(n):
    product=1
    if (n<=0):
        print("Negetive number is not allowd")
    elif n==0 or n==1:
        return product
    else:
        return n*factorial(n-1)
n=int(input("enter a number :"))
result=factorial(n)
print("factorial of ",n," is:",str(result))
