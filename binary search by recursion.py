# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 21:03:53 2020

@author: Supriyo

binary search always takes sorted list as input
"""
#start=0 and end=last 
def binary_search(l,x,start,end): #l is the list and x is the searching elelment
    #base case: 1 element is in the list , start==end
    if start == end:
        if l[start]==x:
            return start
        else:
            return -1
    #more than one element present in the list
    else:
        mid=int((start+end)/2) #else use (start+end)//2
        if l[mid]==x: #if the middle is the searched element then return mid
            return mid
        elif l[mid]>x:
            #left half
            return binary_search(l,x,start,mid-1)
            #because element is not present in the right half so discard the right half
        else:
            #right half 
            return binary_search(l,x,mid+1,end)#checking after the mid point
        
l=[i for i in range(1,11)]
x=int(input("enter the element to be searched between 1 to 10 :"))    
index=binary_search(l,x,0,len(l)-1)
#print("Element ",x,"is present at:",index)
if index==-1:
    print("element is not found") 
else:
    print(x,' is found at ',index+1)