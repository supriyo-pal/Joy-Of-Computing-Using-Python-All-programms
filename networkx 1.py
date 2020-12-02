# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 20:32:17 2020

@author: Supriyo
"""

import networkx as nx
import matplotlib.pyplot as plt 


g=nx.gnp_random_graph(50,0.3)#50 number of nodes and 0.3 is the probability

nx.draw(g)
plt.show
# g.nodes()
# print(g.nodes())
# print(g.edges())