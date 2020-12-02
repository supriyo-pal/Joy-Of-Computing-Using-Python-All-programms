# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 21:56:06 2020

@author: Supriyo
"""
import random
import matplotlib.pyplot as mt

account=0
x=[]
y=[]
name=input("Enter your name ")
for i in range(365):
    #choice=int(input("Enetr a number between 1 to 10 "))
    x.append(i+1)
    choice=random.randint(1,10)
    lucky_draw=random.randint(1,10)
    print(choice," ",lucky_draw)    
    if lucky_draw==choice:
        account=account+900-100
        #print(name," Win","in accout ",account)
    else:
        account=account-100
        #print(name," Loss","in account",account )
    y.append(account)
print("In account ",account)
mt.plot(x,y)
mt.show()