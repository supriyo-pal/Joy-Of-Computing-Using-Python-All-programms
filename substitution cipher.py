# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 10:19:33 2020

@author: Supriyo
"""
import string

dict={}
data=""
file=open("op_file.txt","w")
for i in range (len(string.ascii_letters)):
    dict[string.ascii_letters[i]]=string.ascii_letters[i-1] #i th letter will be replaced by i-1 th letter
print(dict)    

with open("sp.txt") as f:
    while True:
        c=f.read(1) #boolean value 1 need to be passed for TRUE
        if not c:
            print("end of file")
            break
        if c in dict:
            data=dict[c]
        else:
            data=c
        file.write(data)
        print (data)    
file.close()
