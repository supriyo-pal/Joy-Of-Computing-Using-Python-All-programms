# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 12:37:52 2020

@author: Supriyo
"""

import random
p1=['rock','paper','scissor']
p2=['rock','paper','scissor']
c1=random.choice(p1)
c2=random.choice(p2)

#conditions fro draw
# if c1=='rock' and c2=='rock':
#     print("Draw")
# elif c1=='scissor' and c2=='scissor':
#     print("Draw")
# elif c1=='paper' and c2=='paper':
#     print("Draw")

#conditions for player 2 win
if c1=='rock' and c2=='paper':
    print("Player 2 win")
elif c1=='paper'  and c2=='scissor':    
    print("Player 2 win")    
elif c1=='scissor'  and c2=='rock':    
    print("Player 2 win")

#conditions for player 1 win    
elif c1=='paper' and c2=='rock':
    print("Player 1 win")
elif c1=='scissor'  and c2=='paper':    
    print("Player 1 win")    
elif c1=='rock'  and c2=='scissor':    
    print("Player 2 win")
else:
    print("DRAW")