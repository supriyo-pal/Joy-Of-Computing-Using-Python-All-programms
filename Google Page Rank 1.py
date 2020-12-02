# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 12:54:36 2020

@author: Supriyo
"""
import networkx as nx
import random
import matplotlib.pyplot as plt
import operator

g=nx.gnp_random_graph(10,0.5,directed=True)
nx.draw(g,with_labels=True)
plt.show()
#x is the random source node
x=random.choice([i for i in range(g.number_of_nodes())])
dict_counter={}

for i in range(g.number_of_nodes()):
    dict_counter[i]=0#initialise the counter value to 0
    
dict_counter[x]=dict_counter[x]+1 #increment the counter value

for i in range(10000):
    list_n=list(g.neighbors(x))
    if (len(list_n)==0):#if x is a sink 
        x=random.choice([i for i in range(g.number_of_nodes())])
        dict_counter[x]=dict_counter[x]+1#increment the counter value
    else:
        x=random.choice(list_n)#choose a node randomly from the neighbours of x
        dict_counter[x]=dict_counter[x]+1#increment the counter value

p=nx.pagerank(g)
sorted_p=sorted(p.items(),key=operator.itemgetter(1))
sorted_rw=sorted(dict_counter.items(),key=operator.itemgetter(1))

print(p)
print(dict_counter)

print(sorted_p)
print(sorted_rw)