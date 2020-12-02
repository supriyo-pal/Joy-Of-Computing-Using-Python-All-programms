# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 10:52:32 2020

@author: Supriyo
"""

# 3x3 board 

import numpy
board=numpy.array([['-','-','-'],['-','-','-'],['-','-','-']])

p1s='X'
p2s="O"

#for placing the symbol to the particular position
def place(symbol):
    print(numpy.matrix(board)) #2d array will be priented by matrix form
    while(1):
        row=int(input('enter row 1/2/3 '))
        col=int(input('enter column 1/2/3 '))
        if row>0 and row<4 and col>0 and col<4 and board[row-1][col-1]=='-': #it will check for rows and columns
            break
        else:
            print('invalid input, Please enter again')
    board[row-1][col-1]=symbol 

#for checking the elements of the rows    
def check_rows(symbol):
    for r in range(3):
        count=0
        for c in range(3):
            if board[r][c]==symbol:
                count+=1
        if count==3: #check rows
            print(numpy.matrix(board))
            print(symbol,'won')
            return True
    return False

#for checking the elements of the columns
def check_cols(symbol):
    for c in range(3):
        count=0
        for r in range(3):
            if board[r][c]==symbol:
                count+=1
        if count==3:#check columns
            print(numpy.matrix(board))
            print(symbol,'won')
            return True
    return False   

#for checking the elements of the diagonal
def check_diagonal(symbol):
    if board[0][2]==board[1][1] and board[1][1]==board[2][0] and board[1][1]==symbol:
        print(symbol,'won')
        return True
    if board[0][0]==board[1][1] and board[1][1]==board[2][2] and board[1][1]==symbol:
        print(symbol,'won')
        return True
    return False


def won(symbol):
     return check_rows(symbol) or check_cols(symbol) or check_diagonal(symbol)
         
def play():
    for turn in range(9):
        if turn%2==0:
            print('X turn')
            place(p1s)
            if won(p1s):
                break
        else:
            print('O turn')
            place(p2s)
            if won(p2s):
               break
    if not won(p1s) and not won(p2s):
        print("draw")
play()
                




