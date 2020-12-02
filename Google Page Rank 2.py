# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 22:01:56 2020

@author: Supriyo
"""

import networkx as nx

u=nx.Graph()#undirected graph
g=nx.DiGraph()#directed graph

print(g.nodes())
g.add_nodes_from([i for i in range(5)])
print(g.nodes())
print(g.out_edges())
print(g.in_edges())


g.add_edge(1,2)
g.add_edge(0,3)
g.add_edge(2,3)
g.add_edge(3,2)
g.add_edge(4,1)
#g.add_edge()
print(g.edges())
print(g.out_edges(2))
print(g.in_edges(1))


G=nx.star_graph(6)
nx.draw(G)