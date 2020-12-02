# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 11:49:38 2020

@author: Supriyo
"""
# t1=('Amit','Simran','Neeru','Ravi','Shubhadha')
# t2=t1+t1
# print(len(t2))
# t1=t1+('Poonam',)
# print(t1)

# import random
# def play():
#     a=input('enter a number from 1 to 10')
#     r=random.randint(1,10)
#     if a==r:
#         return 1
#     else:
#         return 0
# amt=0
# for i in range(1,3):
#     amt=amt+play()
# print(amt)

#game 1
# import random
# r=random.uniform(0,1)
# if (r<=0.5):
#     print('won')
# else:
#     print('lose')

# import random
# r=random.choice(range(1,6))
# if (r%2==0):
#     print('won')

s1=input('enter first string:')
s2=input('enter second string:')
if sorted(s1)==sorted(s2):
    print('anagram')
else:
    print('not')