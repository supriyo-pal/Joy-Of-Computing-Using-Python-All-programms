# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 10:24:22 2020

@author: Supriyo
"""
# Python program to check if given
# number is power of 2 or not 

# Function to check if x is power of 2
def isPowerOfTwo(n):
	if (n == 0):
		return False
	while (n != 1):
			if (n % 2 != 0):
				return False
			n = n // 2
			
	return True

# Driver code
n=int(input("enter the number: "))
if(isPowerOfTwo(n)):
	print('Yes')
else:
	print('No')

