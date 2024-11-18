"""
Experimental file
Please DO NOT PUSH changes to this file 
"""

import networkx as nx

from productions.p01.production01 import ProductionP1
from productions.p02.production02 import ProductionP2
from productions.utils import visualize_graph, prepare_valid_test_graph_with_hanging_node

if __name__ == '__main__':

    G = prepare_valid_test_graph_with_hanging_node()
    # G = nx.Graph()
    # G.add_node('Q:5.0:5.0', label='Q', R=1)
    # G.add_nodes_from([
    #     ('v:0.0:0.0', {'label': 'v', 'x': 0.0, 'y': 0.0, 'h': 0}),
    #     ('v:10.0:0.0', {'label': 'v', 'x': 10.0, 'y': 0.0, 'h': 0}),
    #     ('v:10.0:10.0', {'label': 'v', 'x': 10.0, 'y': 10.0, 'h': 0}),
    #     ('v:0.0:10.0', {'label': 'v', 'x': 0.0, 'y': 10.0, 'h': 0})
    # ])
    # G.add_edges_from([
    #     ('v:0.0:0.0', 'v:10.0:0.0', {'label': 'E', 'B': 1}),
    #     ('v:10.0:0.0', 'v:10.0:10.0', {'label': 'E', 'B': 1}),
    #     ('v:10.0:10.0', 'v:0.0:10.0', {'label': 'E', 'B': 1}),
    #     ('v:0.0:10.0', 'v:0.0:0.0', {'label': 'E', 'B': 1}),
    #     ('Q:5.0:5.0', 'v:0.0:0.0'), ('Q:5.0:5.0', 'v:10.0:0.0'), ('Q:5.0:5.0', 'v:10.0:10.0'), ('Q:5.0:5.0', 'v:0.0:10.0')
    # ])
    # G.add_nodes_from([
    #     ('v1', {'label': 'v', 'x': 0, 'y': 0, 'h': 0}),
    #     ('v2', {'label': 'v', 'x': 1, 'y': 0, 'h': 0}),
    #     ('v3', {'label': 'v', 'x': 1.5, 'y': 0.5, 'h': 0}),
    #     ('v4', {'label': 'v', 'x': 1, 'y': 1, 'h': 0}),
    #     ('v5', {'label': 'v', 'x': 0, 'y': 1, 'h': 0})
    # ])
    # G.add_edges_from([
    #     ('v1', 'v2', {'label': 'E', 'B': 0}),
    #     ('v2', 'v3', {'label': 'E', 'B': 0}),
    #     ('v3', 'v4', {'label': 'E', 'B': 0}),
    #     ('v4', 'v5', {'label': 'E', 'B': 0}),
    #     ('v5', 'v1', {'label': 'E', 'B': 0}),
    #     ('Q', 'v1'), ('Q', 'v2'), ('Q', 'v3'), ('Q', 'v4'), ('Q', 'v5')
    # ])

    # visualize_graph(G)

    prod1 = ProductionP1(G)
    # prod1.apply()
    # visualize_graph(G)
    # prod1.apply()
    # prod1.apply()
    # # prod1.apply()
    # visualize_graph(G)
    prod2 = ProductionP2(G)
    # visualize_graph(G)
    prod2.apply()
    # prod2.apply()
    # prod2.apply()
    visualize_graph(G)
    # visualize_graph(G)


    # prod2 = ProductionP2(G)
    # prod2.visualize('Before P2 Application')
    # prod2.apply()
    # prod2.visualize('After P2 Application')
