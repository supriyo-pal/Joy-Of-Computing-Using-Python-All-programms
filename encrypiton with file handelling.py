# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 13:26:38 2020

@author: Supriyo
"""

import string

dict={}
data=""
file=open("output.txt","w") #open the output file

for i in range (len(string.ascii_letters)):
    dict[string.ascii_letters[i]]=string.ascii_letters[i-1] #i th letter as key and the value will be i-1 th letter
print(dict)

#open the input file and write the text    
with open('input.txt','w') as f1:
    f1.write("PLATINUM ")

#open the input file and     
with open("input.txt") as f:
    while True:
        c=f.read(1) #boolean value 1 need to be passed for TRUE
        if not c:
            print("end of file")
            break
        if c in dict:
            data=dict[c]#i th letter will be replaced by i-1 th letter
        else:
            data=c
        file.write(data) #write the output to the output file
        print (data)

#open the output file and read
with open("output.txt",'r') as f2:
    result=f2.read()
    print(result)
    
file.close()
f1.close()
f.close()
f2.close()