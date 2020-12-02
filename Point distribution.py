# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 22:13:40 2020

@author: Supriyo
"""

import networkx as nx
import random
import matplotlib.pyplot as plt
def add_edges():
    nodes=list(g.nodes())
    
    for s in nodes:
        for t in nodes:
            if s!=t:
                r=random.random()
                if r<=0.5:#head
                    g.add_edge(s,t)
    return g


def assign_points(g):
    nodes=list(g.nodes())
    p=[]
    for each in nodes:
        p.append(100)
    return p

        
def distribute_points(g,points):
    nodes=list(g.nodes())
    new_points=[]
    for i in range(len(nodes)):
        new_points.append(0)
        
    for n in nodes:
        out=list(g.out_edges(n))
        if len(out)==0:
            new_points[n]=new_points[n]+points[n]
        else:
            share=points[n]/len(out)
            for (src,tgt) in out:
                new_points[tgt]=new_points[tgt]+share
    return new_points

       
def keep_distributing(points,g):
    #nodes=list(g.nodes())
    while (1):
        new_points=distribute_points(g,points)
        print(new_points)
        points=new_points
        stop=input("press # to stop ")
        if stop=="#":
            break
    return new_points

def rank_by_points(points):
    d={}
    for i in range(len(points)):
        d[i]=points[i]
        print(sorted(d.items(),key=lambda f:f[1]))

g=nx.DiGraph()
g.add_nodes_from([i for i in range(10)])

g=add_edges()

#visualise the graph
nx.draw(g,with_labels=True)
plt.show()


#assin initial points
points=assign_points(g)

#keep distributing
final_points=keep_distributing(points,g)

#rank by ppoints
rank_by_points(final_points)

#default networkx function
result=nx.pagerank(g)
print(sorted(result.items(),key=lambda f:f[1]))
