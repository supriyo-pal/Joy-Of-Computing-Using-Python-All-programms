# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 11:09:41 2020

@author: Supriyo
"""
import random
doors=[0]*3
goat_door=[0]*2 #there are three doors comprises of 1 BMW and two goats

swap=0#no of swap wins
dont_swap=0#no of dont swap wins
j=0
while(j<10): #loop will continue 10th time
    x=random.randint(0,2)  # x th door will comprise of BMW
    
    doors[x]= "BMW"
    
    for i in range(0,3):
        if i==x: #because any one position contais BMW
            continue #thats why continue
        else:
            doors[i]="Goat" #else fill the other two position with goat
            goat_door.append(i)#filling done
            
    choice=int(input("enter your choice :"))
    door_open=random.choice(goat_door)#open a door that comprises of goat
    
    while(door_open==choice):#door open should not be eual to choice made by the participants
        door_open=random.choice(goat_door)
    ch=input('do you want to swap : y/n ')
    if ch=='y':
        if  doors[choice]=='Goat':
            print("Player wins")
            swap=swap+1
        else:
            print("Player lost")
    else:
        if  doors[choice]=='Goat':
            print("Player lost")
        else:
            print("Player wins")
            dont_swap+=1
    j+=1
print(swap)
print(dont_swap)



