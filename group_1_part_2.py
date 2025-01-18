"""
Group 1
Project 1 part 2
"""

import networkx as nx
import os

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
from productions.p17.production17 import ProductionP17

from productions.utils import visualize_graph

OUTPUT_DIR = "./results/"


def prepare_output_directory(p: str = OUTPUT_DIR):
    if not os.path.exists(p):
        os.makedirs(p)

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

def run_prod_queue(G: nx.Graph, pent_prod_queue: list, quad_prod_queue: list, reference_node: dict, iterations: int) -> nx.Graph:
    iter = 0
    m = lambda x: '0' * (3-len(str(x))) + str(x)
    visualize_graph(G, title=f"{m(iter)} Initial graph", img_path=OUTPUT_DIR)
    iter += 1

    for _ in range(iterations):
        if ProductionP16(G).apply_with_reference_node(reference_node):
            print("ProductionP16 applied")
            visualize_graph(G, title=f"{m(iter)} ProductionP16 applied", img_path=OUTPUT_DIR)
            iter += 1

        for p in pent_prod_queue:
            applied = False
            while p(G).apply_with_reference_node(reference_node):
                applied = True

            if applied:
                print(f"{p.__name__} applied")
                visualize_graph(G, title=f"{m(iter)} {p.__name__} applied", img_path=OUTPUT_DIR)
                iter += 1

        if ProductionP7(G).apply_with_reference_node(reference_node):
            print("ProductionP7 applied")
            visualize_graph(G, title=f"{m(iter)} ProductionP7 applied", img_path=OUTPUT_DIR)
            iter += 1

        for p in quad_prod_queue:
            applied = False
            while p(G).apply_with_reference_node(reference_node):
                applied = True

            if applied:
                print(f"{p.__name__} applied")
                visualize_graph(G, title=f"{m(iter)} {p.__name__} applied", img_path=OUTPUT_DIR)
                iter += 1

    return G


if __name__ == '__main__':
    prepare_output_directory()

    G = init_2_graph()
    pent_prod_queue = [
        ProductionP17,
        ProductionP10,
        ProductionP11,
        ProductionP9,
    ]
    quad_prod_queue = [
        ProductionP8,
        ProductionP4,
        ProductionP2,
        ProductionP3,
        ProductionP1
    ]
    reference_node = {"x": 7.75, "y": 5.0}
    iterations = 2

    run_prod_queue(G, pent_prod_queue, quad_prod_queue, reference_node, iterations)
