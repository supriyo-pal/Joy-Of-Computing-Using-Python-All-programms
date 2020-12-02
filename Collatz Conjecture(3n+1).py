# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 11:40:12 2020

@author: Supriyo
"""

number=int(input("enter a number :"))
def collatz_conjecture(number):
    counter=1
    while ( number>1):
        if number%2==0:
            number=number/2
            print(number)
            counter+=1
        else:
            number=number*3+1
            print(number)
            counter+=1
            
    print(number," ",counter)

collatz_conjecture(number)