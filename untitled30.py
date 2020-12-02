# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 13:48:26 2020

@author: Supriyo
"""

m,n=input().split(",")
ans=list()
for check in range(int(m),int(n)+1):
    flag=0
    for even in str(check):
        if int(even)%2==0:
            flag+=1
    if flag==len(str(check)):
        ans.append(str(check))
print(','.join(ans),end="")