"""
Experimental file
Please DO NOT PUSH changes to this file 
"""

import networkx as nx

from productions.p01.production01 import ProductionP1
from productions.p02.production02 import ProductionP2
from productions.p08.production08 import ProductionP8
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
from productions.utils import (
    visualize_graph,
)

if __name__ == "__main__":

    G = nx.Graph()
    G.add_node("P:5.0:5.0", label="P", R=0)
    G.add_node("Q:0.0:12.0", label="Q", R=0)
    G.add_node("Q:0.0:-2.0", label="Q", R=0)
    G.add_node("Q:-5.0:5.0", label="Q", R=0)
    G.add_node("Q:13.0:2.0", label="Q", R=0)
    G.add_node("Q:13.0:8.0", label="Q", R=0)
    G.add_nodes_from(
        [
            ("v:0.0:0.0", {"label": "v", "x": 0.0, "y": 0.0, "h": 0}),
            ("v:10.0:0.0", {"label": "v", "x": 10.0, "y": 0.0, "h": 0}),
            ("v:10.0:10.0", {"label": "v", "x": 10.0, "y": 10.0, "h": 0}),
            ("v:0.0:10.0", {"label": "v", "x": 0.0, "y": 10.0, "h": 0}),
            ("v:11.0:5.0", {"label": "v", "x": 11.0, "y": 5.0, "h": 0}),
            ("v:15.0:5.0", {"label": "v", "x": 15.0, "y": 5.0, "h": 0}),
            ("v:15.0:15.0", {"label": "v", "x": 15.0, "y": 15.0, "h": 0}),
            ("v:15.0:-5.0", {"label": "v", "x": 15.0, "y": -5.0, "h": 0}),
            ("v:-5.0:-5.0", {"label": "v", "x": -5.0, "y": -5.0, "h": 0}),
            ("v:-5.0:15.0", {"label": "v", "x": -5.0, "y": 15.0, "h": 0}),
        ]
    )
    G.add_edges_from(
        [
            ("Q:13.0:8.0", "v:15.0:15.0"),
            ("Q:13.0:8.0", "v:10.0:10.0"),
            ("Q:13.0:8.0", "v:11.0:5.0"),
            ("Q:13.0:8.0", "v:15.0:5.0"),
            #
            ("Q:13.0:2.0", "v:15.0:5.0"),
            ("Q:13.0:2.0", "v:11.0:5.0"),
            ("Q:13.0:2.0", "v:10.0:0.0"),
            ("Q:13.0:2.0", "v:15.0:-5.0"),
            ("v:11.0:5.0", "v:15.0:5.0", {"label": "E", "B": 1}),
            ("v:15.0:15.0", "v:15.0:5.0", {"label": "E", "B": 1}),
            ("v:15.0:-5.0", "v:15.0:5.0", {"label": "E", "B": 1}),
            # prev
            ("v:0.0:0.0", "v:10.0:0.0", {"label": "E", "B": 0}),
            ("v:11.0:5.0", "v:10.0:10.0", {"label": "E", "B": 1}),
            ("v:10.0:0.0", "v:11.0:5.0", {"label": "E", "B": 1}),
            ("v:10.0:10.0", "v:0.0:10.0", {"label": "E", "B": 0}),
            ("v:0.0:10.0", "v:0.0:0.0", {"label": "E", "B": 0}),
            # P
            ("P:5.0:5.0", "v:0.0:0.0"),
            ("P:5.0:5.0", "v:11.0:5.0"),
            ("P:5.0:5.0", "v:10.0:0.0"),
            ("P:5.0:5.0", "v:10.0:10.0"),
            ("P:5.0:5.0", "v:0.0:10.0"),
            # Q
            ("Q:0.0:12.0", "v:10.0:10.0"),
            ("Q:0.0:12.0", "v:15.0:15.0"),
            ("Q:0.0:12.0", "v:-5.0:15.0"),
            ("Q:0.0:12.0", "v:0.0:10.0"),
            ("Q:-5.0:5.0", "v:0.0:10.0"),
            ("Q:-5.0:5.0", "v:-5.0:15.0"),
            ("Q:-5.0:5.0", "v:-5.0:-5.0"),
            ("Q:-5.0:5.0", "v:-5.0:-5.0"),
            ("Q:-5.0:5.0", "v:0.0:0.0"),
            ("Q:0.0:-2.0", "v:-5.0:-5.0"),
            ("Q:0.0:-2.0", "v:15.0:-5.0"),
            ("Q:0.0:-2.0", "v:10.0:0.0"),
            ("Q:0.0:-2.0", "v:0.0:0.0"),
            # sides
            ("v:-5.0:15.0", "v:0.0:10.0", {"label": "E", "B": 0}),
            ("v:15.0:15.0", "v:10.0:10.0", {"label": "E", "B": 1}),
            ("v:15.0:15.0", "v:-5.0:15.0", {"label": "E", "B": 1}),
            ("v:-5.0:-5.0", "v:-5.0:15.0", {"label": "E", "B": 1}),
            ("v:-5.0:-5.0", "v:0.0:0.0", {"label": "E", "B": 0}),
            ("v:-5.0:-5.0", "v:15.0:-5.0", {"label": "E", "B": 1}),
            ("v:10.0:0.0", "v:15.0:-5.0", {"label": "E", "B": 1}),
        ]
    )

    def do_prod(Prod, G):
        p = Prod(G)
        p.apply()

    def mark_k_closest_Q(G: nx.Graph, k, cord):
        x, y = cord["x"], cord["y"]
        results = []
        for node, data in G.nodes(data=True):
            if data.get("label") == "Q":
                x, y = node.split(":")[1:]
                x, y = float(x), float(y)
                results.append((dist_sq(x, y, cord["x"], cord["y"]), node))
        results = sorted(results)
        print(results)
        for i in range(k):
            node = results[i][1]
            G.nodes[node]["R"] = 1

    def mark_k_closest_2(G: nx.Graph, k, cord):
        x, y = cord["x"], cord["y"]
        results = []
        for node, data in G.nodes(data=True):
            if data.get("label") == "Q":
                results.append((Q_with_closest_neigh(G, node, cord), node))
        results = sorted(results)
        print(results)
        for i in range(k):
            node = results[i][1]
            G.nodes[node]["R"] = 1

    def Q_with_closest_neigh(G, node, cord):
        x, y = cord["x"], cord["y"]
        neighbors = list(G.neighbors(node))

        result = []
        for n in neighbors:
            nx, ny = G.nodes[n]["x"], G.nodes[n]["y"]
            result.append((dist_sq(x, y, nx, ny), n))
        return sorted(result)[0][0]

    def dist_sq(x1, y1, x2, y2):
        return (x1 - x2) ** 2 + (y1 - y2) ** 2

    mark_k_closest_Q(G, 1, {"x": 20, "y": 13})
    for i in range(3):
        visualize_graph(G)
        while (
            do_prod(ProductionP2, G)
            or do_prod(ProductionP1, G)
            or do_prod(ProductionP3, G)
            or do_prod(ProductionP4, G)
            or do_prod(ProductionP8, G)
            or do_prod(ProductionP9, G)
            or do_prod(ProductionP10, G)
            or do_prod(ProductionP11, G)
            or do_prod(ProductionP17, G)
        ):
            pass
        visualize_graph(G)
        mark_k_closest_Q(G, 1, {"x": 15, "y": 15})
        visualize_graph(G)
        while do_prod(ProductionP8, G):
            pass

    visualize_graph(G)
