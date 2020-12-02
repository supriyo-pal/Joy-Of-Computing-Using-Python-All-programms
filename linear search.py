# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 20:36:27 2020

@author: Supriyo
"""
def linear_search(n,x): #x is the element to be searched
    element=[] #n is the range
    for i in range(1,n):
           element.append(i)
    flag=0
    count=0
    for i in (element):
        count+=1
        if i==x:
            print("you got it : "+str(i))
            flag=1
            break
    if flag==0:
        print("Not Found !")
    print("No of iteration :"+str(count))       
linear_search(1001,523)
#linear search is very time comsuming and it can be used when number of iteration is very less
