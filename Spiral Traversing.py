# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 20:09:15 2020

@author: Supriyo
"""
import turtle
import random

turtle.bgcolor("black")
se=turtle.Turtle()
width=5
height=7
dot_distance=25
se.setpos(-250,250)

se.penup()
list_color=["White","red","blue","green","orange","pink","violet","grey","brown","yellow"]

def spiral(m,n): #m = row,n = column, a=list of list
    k=0 
    l=0
    f=0
    se.color("white")
    '''
        k=index of starting row
        l=index of starting column
    '''
    col=random.randint(0,9)
    se.color(list_color[col])
    
    while(k<m and l<n):
      #printing the first row from the remaining row
      if(f==1):
          se.right(90)
      for i in range(l,n):
          #print(a[k][i],end=" ")
          se.dot()
          se.forward(dot_distance)
      k+=1
      f=1
      
      se.right(90)
      col=random.randint(0,10)
      se.color(list_color[col])
      
      for i in range(k,m):
          #print(a[i][n-1],end=" ")#printing the last column
          se.dot()
          se.forward(dot_distance)       
      n-=1
      se.right(90)
      
      if k<m:
          #printing the last row from the remainig rows
          for i in range(n-1,l-1,-1):
              #print(a[m-1][i],end=" ")
              se.dot()
              se.forward(dot_distance)
          m-=1
      se.right(90)
      col=random.randint(0,9)
      se.color(list_color[col])
      if(l<n):
          #printing the first column from the remaining column
          for i in range(m-1,k-1,-1):
             # print(a[i][l],end=" ")
             se.dot()
             se.forward(dot_distance)
          l+=1
              
# a=[]
# count=1
# for i in range(4):
#     l=[]
#     for j in range(4):
#         l.append(count)
#         count+=1
#     a.append(l)
spiral(10,10)
turtle.done()
   
              
          
          
          
    
    