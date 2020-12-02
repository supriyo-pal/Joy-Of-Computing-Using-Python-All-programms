# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 11:59:19 2020

@author: Supriyo
"""
import networkx as nx
g=nx.barbell_graph(4,2)
h=nx.barbell_graph(5,3)
nx.draw(g)
nx.draw(h)

i=nx.complete_graph(4)
nx.draw(i)

j=nx.cycle_graph(6)
nx.draw(j)

k=nx.ladder_graph(10)
nx.draw(k)

l=nx.path_graph(6)
nx.draw(l)

m=nx.star_graph(10)
nx.draw(m)

n=nx.wheel_graph(10)
nx.draw(n)

o=nx.gnp_random_graph(5,0.5)#0.5  is the probability
nx.draw(o)