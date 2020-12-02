# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 11:07:58 2020

@author: Supriyo
"""

'''
A group of points andd lines between the points is called graph
points->nodes
lines->edges
'''
import networkx as nx
import numpy as np

g=nx.read_edgelist('facebook_combined.txt')

#sortest path of each pair of node

n=list(g.nodes())

spll=[]

for u in n:
    for v in n:
        if u!=v:
            l=nx.shortest_path_length(g,u,v)
            #print("shortest path between", u, "and",v, "is of length: ",l)
            spll.append(l)
min_spl=min(spll)
max_spl=max(spll)
avg_spl=np.average(spll)

print("Minimum shortet path length:",min_spl)
print("\n Maximum shortet path length:",max_spl)
print("\n Average shortet path length:",avg_spl)