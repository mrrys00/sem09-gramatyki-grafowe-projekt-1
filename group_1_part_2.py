"""
Group 1
Project 1 part 2
"""

import networkx as nx

from productions.production import Production
from productions.p01.production01 import ProductionP1
from productions.p02.production02 import ProductionP2
from productions.p03.production03 import ProductionP3
from productions.p04.production04 import ProductionP4
from productions.p07.production07 import ProductionP7
from productions.p08.production08 import ProductionP8
from productions.p09.production09 import ProductionP9
from productions.p10.production10 import ProductionP10
from productions.p11.production11 import ProductionP11
from productions.p16.production16 import ProductionP16

from productions.utils import visualize_graph

VISUALIZE_ALL = True

def init_2_graph() -> nx.Graph:
    G = nx.Graph()
    G.add_nodes_from([
        ('v:0.0:0.0', {'label': 'v', 'x': 0.0, 'y': 0.0, 'h': 0}),
        ('v:10.0:0.0', {'label': 'v', 'x': 10.0, 'y': 0.0, 'h': 0}),
        ('v:10.0:5.0', {'label': 'v', 'x': 10.0, 'y': 5.0, 'h': 0}),
        ('v:10.0:10.0', {'label': 'v', 'x': 10.0, 'y': 10.0, 'h': 0}),
        ('v:0.0:10.0', {'label': 'v', 'x': 0.0, 'y': 10.0, 'h': 0}),
        
        ('v:3.0:2.0', {'label': 'v', 'x': 3.0, 'y': 2.0, 'h': 0}),
        ('v:7.0:2.0', {'label': 'v', 'x': 7.0, 'y': 2.0, 'h': 0}),
        ('v:8.0:5.0', {'label': 'v', 'x': 8.0, 'y': 5.0, 'h': 0}),
        ('v:3.0:8.0', {'label': 'v', 'x': 3.0, 'y': 8.0, 'h': 0}),
        ('v:7.0:8.0', {'label': 'v', 'x': 7.0, 'y': 8.0, 'h': 0}),

        ('P:5.0:5.0', {'label': 'P', 'R': 0}),

        ('Q:5.0:1.0', {'label': 'Q', 'R': 0}),
        ('Q:9.0:3.0', {'label': 'Q', 'R': 0}),
        ('Q:9.0:8.0', {'label': 'Q', 'R': 0}),
        ('Q:5.0:9.0', {'label': 'Q', 'R': 0}),
        ('Q:2.0:5.0', {'label': 'Q', 'R': 0}),
    ])
    G.add_edges_from([
        ('v:0.0:0.0', 'v:10.0:0.0', {'label': 'E', 'B': 1}),
        ('v:10.0:0.0', 'v:10.0:5.0', {'label': 'E', 'B': 1}),
        ('v:10.0:5.0', 'v:10.0:10.0', {'label': 'E', 'B': 1}),
        ('v:10.0:10.0', 'v:0.0:10.0', {'label': 'E', 'B': 1}),
        ('v:0.0:10.0', 'v:0.0:0.0', {'label': 'E', 'B': 1}),
        
        ('v:0.0:0.0', 'v:3.0:2.0', {'label': 'E', 'B': 0}),
        ('v:10.0:0.0', 'v:7.0:2.0', {'label': 'E', 'B': 0}),
        ('v:10.0:5.0', 'v:8.0:5.0', {'label': 'E', 'B': 0}),
        ('v:10.0:10.0', 'v:7.0:8.0', {'label': 'E', 'B': 0}),
        ('v:0.0:10.0', 'v:3.0:8.0', {'label': 'E', 'B': 0}),

        ('v:3.0:2.0', 'v:7.0:2.0', {'label': 'E', 'B': 0}),
        ('v:7.0:2.0', 'v:8.0:5.0', {'label': 'E', 'B': 0}),
        ('v:8.0:5.0', 'v:7.0:8.0', {'label': 'E', 'B': 0}),
        ('v:7.0:8.0', 'v:3.0:8.0', {'label': 'E', 'B': 0}),
        ('v:3.0:8.0', 'v:3.0:2.0', {'label': 'E', 'B': 0}),
        
        # for ('P:5.0:5.0', {'label': 'P', 'R': 0}),
        ('v:3.0:2.0', 'P:5.0:5.0'),
        ('v:7.0:2.0', 'P:5.0:5.0'),
        ('v:8.0:5.0', 'P:5.0:5.0'),
        ('v:7.0:8.0', 'P:5.0:5.0'),
        ('v:3.0:8.0', 'P:5.0:5.0'),
        
        # for ('Q:5.0:1.0', {'label': 'Q', 'R': 0}),
        ('v:0.0:0.0', 'Q:5.0:1.0'),
        ('v:10.0:0.0', 'Q:5.0:1.0'),
        ('v:7.0:2.0', 'Q:5.0:1.0'),
        ('v:3.0:2.0', 'Q:5.0:1.0'),

        # for ('Q:9.0:3.0', {'label': 'Q', 'R': 0}),
        ('v:7.0:2.0', 'Q:9.0:3.0'),
        ('v:10.0:0.0', 'Q:9.0:3.0'),
        ('v:10.0:5.0', 'Q:9.0:3.0'),
        ('v:8.0:5.0', 'Q:9.0:3.0'),

        # for ('Q:9.0:8.0', {'label': 'Q', 'R': 0}),
        ('v:8.0:5.0', 'Q:9.0:8.0'),
        ('v:10.0:5.0', 'Q:9.0:8.0'),
        ('v:10.0:10.0', 'Q:9.0:8.0'),
        ('v:7.0:8.0', 'Q:9.0:8.0'),

        # for ('Q:5.0:9.0', {'label': 'Q', 'R': 0}),
        ('v:3.0:8.0', 'Q:5.0:9.0'),
        ('v:7.0:8.0', 'Q:5.0:9.0'),
        ('v:10.0:10.0', 'Q:5.0:9.0'),
        ('v:0.0:10.0', 'Q:5.0:9.0'),

        # for ('Q:2.0:5.0', {'label': 'Q', 'R': 0}),
        ('v:0.0:0.0', 'Q:2.0:5.0'),
        ('v:3.0:2.0', 'Q:2.0:5.0'),
        ('v:3.0:8.0', 'Q:2.0:5.0'),
        ('v:0.0:10.0', 'Q:2.0:5.0'),
    ])
    
    return G


prod_queue = [
    
    [ProductionP16],
    [ProductionP9],
    [ProductionP7],
    [ProductionP8,ProductionP8],
    [ProductionP2],
    [ProductionP3],
    [ProductionP1],
    [ProductionP7],
    [ProductionP8,ProductionP8],
    [ProductionP2],
    [ProductionP3],
    [ProductionP1],
]

def run_prod_chain(G: nx.Graph, prod_queue: list[list]=prod_queue) -> nx.Graph:

    for p_tuple in prod_queue:
        for p in p_tuple:
            prod_name = f"{p.__name__} applied"
            p(G).apply()
            print(prod_name)
        if VISUALIZE_ALL: visualize_graph(G, title=prod_name)

    return G


if __name__ == '__main__':
    G = init_2_graph()
    visualize_graph(G)
    G = run_prod_chain(G=G)
    print("works")
