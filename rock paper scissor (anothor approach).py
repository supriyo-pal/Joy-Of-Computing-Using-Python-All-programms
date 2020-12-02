# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 13:40:18 2020

@author: Supriyo
"""
#by using dictionary
def rock_paper_scissor(num1,num2,bit1,bit2):
    p1=int(num1[bit1])%3
    p2=int(num2[bit2])%3
    player_one=[0]*3
    player_two=[0]*3
    if (player_one[p1]==player_two[p2]):
        print("Draw")
    elif (player_one[p1]=='rock' and player_two[p2]=='scissor'):
        print("player 1 wins")
    elif (player_one[p1]=='rock' and player_two[p2]=='paper'):
        print("player 2 wins")
    elif (player_one[p1]=='paper' and player_two[p2]=='scissor'):
        print("player 2 wins")
    elif (player_one[p1]=='paper' and player_two[p2]=='rock'):
        print("player 2 wins")
    elif (player_one[p1]=='scissor' and player_two[p2]=='rock'):
        print("player 2 wins")
    elif (player_one[p1]=='scissor' and player_two[p2]=='paper'):
        print("player 1 wins")
    
        
        
        
player1={0:'rock',1:'paper',2:'scissor'}
player2={0:'rock',1:'paper',2:'scissor'}

while(1):
    num1=input("PLAYER 1:enter your choice : ")#for player 1
    num2=input("PLAYER 2:enter your choice : ")#for player 2
    bit1=int(input("PLAYER 1 ,enter the secret bit position: "))
    bit2=int(input("PLAYER 2 ,enter the secret bit position: "))
    rock_paper_scissor(num1,num2,bit1,bit2)
    ch=input("do you want to continue: y/n : ")
    if ch=='n':
        break
    else:
        continue


    