"""
Group 1
Project part 2
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

def init_2_graph() -> nx.Graph:
    G = nx.Graph()
    G.add_nodes_from([
        ('v:0.0:0.0', {'label': 'v', 'x': 0.0, 'y': 0.0, 'h': 0}),
        ('v:10.0:0.0', {'label': 'v', 'x': 10.0, 'y': 0.0, 'h': 0}),
        ('v:10.0:5.0', {'label': 'v', 'x': 10.0, 'y': 5.0, 'h': 0}),
        ('v:10.0:10.0', {'label': 'v', 'x': 10.0, 'y': 10.0, 'h': 0}),
        ('v:0.0:10.0', {'label': 'v', 'x': 0.0, 'y': 10.0, 'h': 0}),
        ('v:0.0:5.0', {'label': 'v', 'x': 0.0, 'y': 5.0, 'h': 0}),
        
        ('v:3.0:2.0', {'label': 'v', 'x': 3.0, 'y': 2.0, 'h': 0}),
        ('v:7.0:2.0', {'label': 'v', 'x': 7.0, 'y': 2.0, 'h': 0}),
        ('v:2.0:5.0', {'label': 'v', 'x': 2.0, 'y': 5.0, 'h': 0}),
        ('v:8.0:5.0', {'label': 'v', 'x': 8.0, 'y': 5.0, 'h': 0}),
        ('v:3.0:8.0', {'label': 'v', 'x': 3.0, 'y': 8.0, 'h': 0}),
        ('v:7.0:8.0', {'label': 'v', 'x': 7.0, 'y': 8.0, 'h': 0}),

        # ('Q:5.0:5.0', {'label': 'Q', 'R': 1}),
    ])
    G.add_edges_from([
        ('v:0.0:0.0', 'v:10.0:0.0', {'label': 'E', 'B': 1}),
        ('v:10.0:0.0', 'v:10.0:5.0', {'label': 'E', 'B': 1}),
        ('v:10.0:5.0', 'v:10.0:10.0', {'label': 'E', 'B': 1}),
        ('v:10.0:10.0', 'v:0.0:10.0', {'label': 'E', 'B': 1}),
        ('v:0.0:10.0', 'v:0.0:5.0', {'label': 'E', 'B': 1}),
        ('v:0.0:5.0', 'v:0.0:0.0', {'label': 'E', 'B': 1}),
        
        ('v:0.0:0.0', 'v:3.0:2.0', {'label': 'E', 'B': 0}),
        ('v:10.0:0.0', 'v:7.0:2.0', {'label': 'E', 'B': 0}),
        ('v:10.0:5.0', 'v:8.0:5.0', {'label': 'E', 'B': 0}),
        ('v:10.0:10.0', 'v:7.0:8.0', {'label': 'E', 'B': 0}),
        ('v:0.0:10.0', 'v:3.0:8.0', {'label': 'E', 'B': 0}),
        ('v:0.0:5.0', 'v:2.0:5.0', {'label': 'E', 'B': 0}),

        ('v:3.0:2.0', 'v:7.0:2.0', {'label': 'E', 'B': 0}),
        ('v:7.0:2.0', 'v:8.0:5.0', {'label': 'E', 'B': 0}),
        ('v:8.0:5.0', 'v:7.0:8.0', {'label': 'E', 'B': 0}),
        ('v:7.0:8.0', 'v:3.0:8.0', {'label': 'E', 'B': 0}),
        ('v:3.0:8.0', 'v:2.0:5.0', {'label': 'E', 'B': 0}),
        ('v:2.0:5.0', 'v:3.0:2.0', {'label': 'E', 'B': 0}),
        
        # ('v:3.0:2.0', 'Q:5.0:5.0'),
        # ('v:7.0:2.0', 'Q:5.0:5.0'),
        # ('v:8.0:5.0', 'Q:5.0:5.0'),
        # ('v:7.0:8.0', 'Q:5.0:5.0'),
        # ('v:3.0:8.0', 'Q:5.0:5.0'),
        # ('v:2.0:5.0', 'Q:5.0:5.0'),
    ])
    
    return G


prod_queue = [
    [ProductionP2, ProductionP1],
    [ProductionP9],
    [ProductionP7],
    [ProductionP8,ProductionP8],
    [ProductionP8,ProductionP8],
    [ProductionP2,ProductionP3],
    [ProductionP1],
    [ProductionP7],
    [ProductionP8,ProductionP8],
    [ProductionP2,ProductionP3],
    [ProductionP1]
]

def run_prod_chain(G: nx.Graph, prod_queue: list[list]=prod_queue) -> nx.Graph:

    for p_tuple in prod_queue:
        # print(type(p_tuple), p_tuple)
        for p in p_tuple:
            # print(type(p), p)
            p_obj = p(G)
            p_obj.apply()
        # print("OK")
        visualize_graph(G)

    return G

def temp_do_all_productions(G: nx.Graph):
    
    for p in [
        ProductionP1,
        ProductionP2,
        ProductionP3,
        ProductionP4,
        ProductionP7,
        ProductionP8,
        ProductionP9,
        ProductionP10,
        ProductionP11,
        ProductionP16
    ]:
        p_obj = p(G)
        p_obj.apply()
        print(p)
        # visualize_graph(G)

if __name__ == '__main__':
    G = init_2_graph()
    visualize_graph(G)
    G = run_prod_chain(G=G)
    # TODO need to brilliant idea what to do …
    # G = temp_do_all_productions(G)
    visualize_graph(G)
    print("works")