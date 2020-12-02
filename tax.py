# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 14:44:22 2020

@author: Supriyo
"""

m=int(input("How many numbers ?"))
a = list(map(int,input("\nEnter the numbers : ").strip().split()))[:m] 
total_bill=0
def tax():
    sum=0
    taxable=0
    for i in range(len(a)):
        sum=sum+a[i]
    if (sum>=1000):
        taxable=(sum-1000)/10
    total_bill=sum+taxable
    return total_bill
print(tax())