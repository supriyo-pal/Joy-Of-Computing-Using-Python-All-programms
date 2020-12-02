# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 11:55:06 2020

@author: Supriyo
"""

import string 

def remove_matching_letter(l1,l2):
    for i in range(len(l1)):
        for j in range(len(l2)):
            if l1[i]==l2[j]:
                c=l1[i] #l2[j]
                l1.remove(c)
                l2.remove(c)
                l=l1+['*']+l2
                return [l,True]
    l=l1+['*']+l2
    return [l,False]

p1=input("Enter first name : ")
p2=input("Enter the second name :")
p1=p1.upper()
p2=p2.upper()

p1=p1.replace(" ","")
p2=p2.replace(" ","")

l1=list(p1)
l2=list(p2)

proceed=True
while proceed:
    returned_list=remove_matching_letter(l1,l2)
    concatinated_list=returned_list[0]
    proceed=concatinated_list[1]
    star_index=concatinated_list.index('*')
    
    l1=concatinated_list[:star_index]
    l2=concatinated_list[star_index+1:]
    
count=len(l1)+len(l2)

result=['Frieds','Love','Affectio','Mariage','Enemy','Siblings']



while len(result) > 1:
    split_index=(count%len(result))-1
    if split_index >=0:
        right_half=result[split_index+1:]
        left_half=result[:split_index]
        result=right_half+left_half
    else:
        result=result[:len(result)-1]
print(result[0])

