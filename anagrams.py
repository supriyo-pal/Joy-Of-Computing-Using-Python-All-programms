# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 11:36:37 2020

@author: Supriyo

An anagram is a word or phrase formed by rearranging the letters of a 
different word or phrase, typically using all the original letters exactly once. 
For example, the word anagram can be rearranged into nag a ram,
or the word binary into brainy or the word adobe into abode.
"""

str1=input("enter the first string ")
str2=input("enter the second string ")

if (sorted(str1)==sorted(str2)):
    print("these are anagrams")
else:
    print("not anagrams ")