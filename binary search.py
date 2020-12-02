# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 20:34:51 2020

@author: Supriyo
"""

def binary_search(a,x):#a is the array and x is the elemet to be searched
    first_pos=0
    last_pos=len(a)-1 #returns last emenent of the array
    flag=0 #flag=0 means that element is not been found yet
    count=0
    while(first_pos<=last_pos and flag==0):
        count+=1
        mid=(first_pos+last_pos)//2 #integer division
        if x==a[mid]:
            flag=1
            print("eleemnt is presend at "+str(mid))
            print("the number of iteration "+str(count))
            return
        else:
            if x<a[mid]:
                last_pos=mid-1 #discarding the right part of the array
            else:
                first_pos=mid+1 #discarding the left part of the array
    print("element is not found ")
            
a=[i for i in range(1,1001)]
binary_search(a,520)        
    


