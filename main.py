import networkx as nx

from productions.p01.production01 import ProductionP1
from productions.p02.production02 import ProductionP2

# Sample usage and visualization
G = nx.Graph()
G.add_node("Q", label="Q", R=1)  # Element marked for splitting
G.add_nodes_from([
    ("v1", {"label": "v", "x": 0, "y": 0, "h": 0}),
    ("v2", {"label": "v", "x": 1, "y": 0, "h": 0}),
    ("v3", {"label": "v", "x": 1, "y": 1, "h": 0}),
    ("v4", {"label": "v", "x": 0, "y": 1, "h": 0})
])
G.add_edges_from([
    ("v1", "v2", {"label": "E", "B": 0}),
    ("v2", "v3", {"label": "E", "B": 0}),
    ("v3", "v4", {"label": "E", "B": 0}),
    ("v4", "v1", {"label": "E", "B": 0})
])

prod1 = ProductionP1(G)
prod1.visualize("Before P1 Application")
prod1.apply()
prod1.visualize("After P1 Application")

prod2 = ProductionP2(G)
prod2.visualize("Before P2 Application")
prod2.apply()
prod2.visualize("After P1 Application")