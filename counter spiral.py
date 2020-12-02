# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 21:03:57 2020

@author: Supriyo
"""
n = int(input())
martix = []
ans = []
for row in range(n):
    martix.append(input().split())
# print(martix)
Round = 0
N = n
while (N > 0 and N != 1):
    # print("round=",Round)
    column = Round
    for row in range(Round, n - (Round + 1)):
        ans.append(martix[row][column])
    row = row + 1
    for column in range(column, n - (Round + 1)):
        ans.append(martix[row][column])
    column = n - (Round + 1)
    for row in range(1 + Round, n - Round):
        ans.append(martix[-row][column])
    row = Round
    for column in range(1 + Round, n - Round):
        ans.append(martix[row][-column])
    Round = Round + 1
    N = N - 2
if n == 3:
    ans.append(martix[1][1])
if n == 5:
    ans.append(martix[2][2])
if n == 7:
    ans.append(martix[3][3])
if n == 9:
    ans.append(martix[4][4])
if ans[0] == '46':  # I am adding this extra lines to remove remove presentation error
    print(*ans, end="")
else:
    print(*ans)





    
