# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 13:28:05 2020

@author: Supriyo
"""

sen=input("provide a sentence ")
code=list()
upper=0
lower=0
for i in range(len(sen)):
    code.append(sen[i])
print(code)

for g in sen:
    if g.isupper()==True:
        upper+=1
    if g.islower()==True:
        lower+=1

print(upper," ",lower)
