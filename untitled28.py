# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 12:56:35 2020

@author: Supriyo
"""
# import math
# c=50
# h=30
# d= list(map(int,input("\nEnter the numbers : ").strip().split()))
# for i in range(len(d)):
#     q=math.sqrt((2*c*d[i])/h)
#     print(q)

D=input().split(",")
ques=list()

for d in D:
    ques.append(int(d))
ans=list()
for q in ques:
    sol=(((2*50*q)/30)**0.5)
    ans.append(str(round(sol)))
print(",".join(ans),end="")