import networkx as nx

def prepare_valid_test_graph() -> nx.Graph:
    """Prepares the basic 4-nodes and one Q-node graph"""
    G = nx.Graph()
    G.add_node("Q", label="Q", R=1)
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
        ("v4", "v1", {"label": "E", "B": 0}),
        ("Q", "v1"), ("Q", "v2"), ("Q", "v3"), ("Q", "v4")
    ])

    return G

def prepare_corrupted_test_graph() -> nx.Graph:
    """Prepares the basic 4-nodes graph"""
    G = nx.Graph()
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
        ("v4", "v1", {"label": "E", "B": 0}),
    ])

    return G
