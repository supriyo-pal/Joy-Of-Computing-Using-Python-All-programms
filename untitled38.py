# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 14:21:28 2020

@author: Supriyo
"""

import random
import networkx as nx
import matplotlib.pyplot as plt

g=nx.Graph()
g.add_nodes_from([i for i in range(6)])
while(nx.is_connected(g)!=True):
    x=random.choice(list(g.nodes()))
    y=random.choice(list(g.nodes()))
    if x!=y:
        g.add_edge(x,y)
    else:
        continue

nx.draw(g)
plt.show()