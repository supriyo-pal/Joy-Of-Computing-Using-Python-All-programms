# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 21:47:20 2020

@author: Supriyo
     0th fib no= 0
     1st fib no= 1
 -------------------------
     2nd fib no= 1+0=1
     3rd fib no= 1+1=2
     4th fib no= 2+1=3
     5th fib no= 3+2=5
 
"""
#to find the nth fibonacci number

def fibonacci(n):
    if n<2:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)
n=int(input("enter the number :"))
if n<0:
    print("Negetive number is not allowed")
else:
    print("fibonacci of ",n,'is',fibonacci(n))

