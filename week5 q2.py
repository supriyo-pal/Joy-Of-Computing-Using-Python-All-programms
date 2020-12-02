# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 22:25:30 2020

@author: Supriyo
"""

pos = {
    "x": 0, 
    "y": 0
}
z=int(input("input a number"))
c=0
while (c!=z):

    n = input("input direction and steps")
    c=c+1
    if not n:
        break

    direction,steps=n.split()
    if direction == "UP":
        pos["y"] += int(steps)
    elif direction == "DOWN":
        pos["y"] -= int(steps)
    elif direction == "LEFT":
        pos["x"] -= int(steps)
    elif direction == "RIGHT":
        pos["x"] += int(steps)
        
print (int(round((pos["x"]**2 + pos["y"]**2)**0.5)))