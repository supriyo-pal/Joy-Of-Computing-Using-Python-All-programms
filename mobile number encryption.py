# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 13:10:21 2020

@author: Supriyo
"""
import string
def confidential(mob_num):
    subs_dict={}
    sec_num=[0]*len(mob_num)
    for i in range(len(string.digits)):
        subs_dict[string.digits[i]]=string.digits[i-1]
    for j in range(len(mob_num)):
        sec_num[j]=subs_dict[mob_num[j]]
    return(sec_num)
print(confidential("9547522390"))    