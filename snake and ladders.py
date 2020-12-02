# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 10:58:07 2020

@author: Supriyo
"""
from PIL import Image
import random 
end=100

def show_board():
    img=Image.open('C:\\Users\Supriyo\Desktop\sl.png')
    img.show()    

def play():
    #input player 1 and player 2 name
    p1_name= input("Player 1:Enter your name ") 
    p2_name= input("Player 2:Enter your name ")
    
    pp1=0 #initial point of player 1
    pp2=0 #initial point of player 2

    turn=0
    while(1):
        if turn%2==0:#checking for player 1 turn
            print(p1_name,'Your Turn')
            c=int(input("Press 1 to continue and 0 for quit"))#ask player's choice to continue
            if c==0:
                print(p1_name,'scored ',pp1)
                print(p2_name,'scored ',pp2)
                print("Quiting the game Thanks for playing")
                break
            dice=random.randint(1,6) #rooling a dice
            print('Dice Showd: ',dice)
            pp1+=dice #add the point of player 1
            pp1=check_ladder(pp1)#if ladder comes
            pp1=check_snake(pp1)#if snake comes
            
            if pp1>end:#check the player goes beyond the board
                pp1=end #make the point to the end
            print(p1_name,'Your Score: ',pp1)
            if reached_end(pp1):
                print(p1_name,' Won')
                break
        else:
            print(p2_name,'Your Turn')
            c=int(input("Press 1 to continue and 0 for quit"))#ask player's choice to continue
            if c==0:
                print(p1_name,'scored ',pp1)
                print(p2_name,'scored ',pp2)
                print("Quiting the game Thanks for playing")
                break
            dice=random.randint(1,6) #rooling a dice
            print('Dice Showed: ',dice)
            pp2+=dice #add the point of player 2
            pp2=check_ladder(pp2)#if ladder comes
            pp2=check_snake(pp2)#if snake comes
            
            if pp2>end:#check the player goes beyond the board
                pp2=end #make the point to the end
            print(p2_name,'Your Score: ',pp2)
            if reached_end(pp2):
                print(p2_name,' Won')
                break
        turn+=1
def check_ladder(points):
    if points == 8:#1st ladder
        print("Ladder")
        return 26
    elif points==21:
        print("Ladder")
        return 82
    elif points==43:
        print("Ladder")
        return 77
    elif points==50:
        print("Ladder")
        return 91
    elif points==54:
        print("Ladder")
        return 93
    elif points==62:
        print("Ladder")
        return 96
    elif points==66:
        print("Ladder")
        return 87
    elif points==80:
        print("Ladder")
        return 100
    else:
        return points #not a ladder
def check_snake(points):
    if points== 44:
        print("Snake")
        return 22
    elif points==46:
        print("Snake")
        return 5
    elif points==48:
        print("Snake")
        return 9   
    elif points==52:
        print("Snake")
        return 11   
    elif points==55:
        print("Snake")
        return 7   
    elif points==59:
        print("Snake")
        return 17   
    elif points==64:
        print("Snake")
        return 36   
    elif points==69:
        print("Snake")
        return 33   
    elif points==73:
        print("Snake")
        return 1   
    elif points==83:
        print("Snake")
        return 19   
    elif points==92:
        print("Snake")
        return 51   
    elif points==95:
        print("Snake")
        return 24   
    elif points==98:
        print("Snake")
        return 29
    else:#not a snake
        return points
def reached_end(points):
    if points==end:
        return True
    else:
        return False
show_board()
play()