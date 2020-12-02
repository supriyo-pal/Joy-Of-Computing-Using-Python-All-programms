# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 11:07:22 2020

@author: Supriyo
"""
number=int(input ())
def add_digits(num):
        return (num - 1) % 9 + 1 if num > 0 else 0

print(add_digits(number))
#print(add_digits(number))