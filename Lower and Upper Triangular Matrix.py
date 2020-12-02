# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 10:43:18 2020

@author: Supriyo
"""

#A lower triangular matrix is a square matrix (where the number of rows and columns are equal)  where all the elements above the diagonal are zero.
#For example, the following is a lower triangular matrix with the number of rows and columns equal to 3.

# 1 0 0
# 4 5 0
# 7 8 9

def lower(matrix, row, col): 
   for i in range(0, row):    
        for j in range(0, col):        
            if (i < j):            
                print("0", end = " ");            
            else: 
                print(matrix[i][j],  
                       end = " " );        
        print(" ");       
# Function to form upper triangular marix 
def upper(matrix, row, col):   
    for i in range(0, row):       
        for j in range(0, col):           
            if (i > j): 
                print("0", end = " ")               
            else: 
                print(matrix[i][j],  
                       end = " " )           
        print(" ");   
matrix=[] 
element=int(input("enter the diamention: "))
row=element
col=element     

for i in range (row):
    a=[]
    for j in range(col):
        a.append(int(input()))
    matrix.append(a)

print("Lower triangular matrix: "); 
lower(matrix, row, col); 
      
print("Upper triangular matrix: "); 
upper(matrix, row, col); 