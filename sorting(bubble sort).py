# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 20:22:52 2020

@author: Supriyo
"""

def bubble(a):
    n=len(a)#returns the length of the aray
    for i in range (n):
        for j in range(0,n-i-1):#-1 is because of the range issue , exclude the last element because last element is greater we got
            if(a[j]>a[j+1]): #compare two element
                temp=a[j]
                a[j]=a[j+1]
                a[j+1]=temp
a=[5,1,4,2,8]
bubble(a)
for i in a:
    print(i)
                
    