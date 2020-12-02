# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 11:34:09 2020

@author: Supriyo
"""

import networkx as nx
import matplotlib.pyplot as plt

g=nx.Graph()

for i in range(1,10):
    g.add_node(i)
e=[(1,2),(2,3),(3,4),(4,5),(5,6),(6,7),(7,8),(8,9),(9,10)]
g.add_edges_from(e)

nx.draw(g)
plt.show()
    