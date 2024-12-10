import networkx as nx
import matplotlib.pyplot as plt
from statistics import fmean


def visualize_graph(graph: nx.Graph, title: str = "Graph Visualization"):
    """Visualize the graph."""
    multiedges_labels = ["Q", "P"]  # TODO might need to extend this list
    colors = [
        "lightblue" if data.get("label") in multiedges_labels else "lightgreen"
        for node, data in graph.nodes(True)
    ]
    labels = {}
    for node, data in graph.nodes(True):
        if data.get("label") in multiedges_labels:
            labels[node] = f"{data.get('label')}\nR = {data.get('R')}"
        else:
            labels[node] = (
                f"x = {data.get('x')}\ny = {data.get('y')}\nh = {data.get('h')}"
            )
    edge_labels = {}
    for u, v, data in graph.edges(data=True):
        if data.get("label") is not None:
            edge_labels[(u, v)] = f"{data.get('label')}\nB = {data.get('B')}"

    positions = {}
    for point, data in graph.nodes(True):
        if data.get("label") in multiedges_labels:
            x = fmean(
                [graph.nodes[neighbor].get("x") for neighbor in graph.neighbors(point)]
            )
            y = fmean(
                [graph.nodes[neighbor].get("y") for neighbor in graph.neighbors(point)]
            )
            positions[point] = (x, y)
        else:
            positions[point] = (data.get("x"), data.get("y"))

    plt.figure(figsize=(20, 20))
    nx.draw(
        graph,
        pos=positions,
        with_labels=True,
        labels=labels,
        node_color=colors,
        node_size=3000,
    )
    nx.draw_networkx_edge_labels(
        graph, pos=positions, edge_labels=edge_labels, font_size=12
    )
    plt.title(title)
    plt.show()


def prepare_valid_test_graph() -> nx.Graph:
    """Prepares the basic 4-nodes and one Q-node graph"""
    G = nx.Graph()
    G.add_node('Q', label='Q', R=1)
    G.add_nodes_from([
        ('v:0.0:0.0', {'label': 'v', 'x': 0.0, 'y': 0.0, 'h': 0}),
        ('v:1.0:0.0', {'label': 'v', 'x': 1.0, 'y': 0.0, 'h': 0}),
        ('v:1.0:1.0', {'label': 'v', 'x': 1.0, 'y': 1.0, 'h': 0}),
        ('v:0.0:1.0', {'label': 'v', 'x': 0.0, 'y': 1.0, 'h': 0})
    ])
    G.add_edges_from([
        ('v:0.0:0.0', 'v:1.0:0.0', {'label': 'E', 'B': 1}),
        ('v:1.0:0.0', 'v:1.0:1.0', {'label': 'E', 'B': 1}),
        ('v:1.0:1.0', 'v:0.0:1.0', {'label': 'E', 'B': 1}),
        ('v:0.0:1.0', 'v:0.0:0.0', {'label': 'E', 'B': 1}),
        ('Q', 'v:0.0:0.0'), ('Q', 'v:1.0:0.0'), ('Q', 'v:1.0:1.0'), ('Q', 'v:0.0:1.0')
    ])

    return G


def prepare_valid_test_graph_with_hanging_node() -> nx.Graph:
    """Prepares the basic 4-nodes and one Q-node graph"""
    G = nx.Graph()
    G.add_node('Q', label='Q', R=1)
    G.add_nodes_from([
        ('v:0.0:0.0', {'label': 'v', 'x': 0.0, 'y': 0.0, 'h': 0}),
        ('v:1.0:0.0', {'label': 'v', 'x': 1.0, 'y': 0.0, 'h': 0}),
        ('v:1.0:1.0', {'label': 'v', 'x': 1.0, 'y': 1.0, 'h': 0}),
        ('v:0.0:1.0', {'label': 'v', 'x': 0.0, 'y': 1.0, 'h': 0}),
        ('v:1.0:0.5', {'label': 'v', 'x': 1.0, 'y': 0.5, 'h': 1})
    ])
    G.add_edges_from([
        ('v:0.0:0.0', 'v:1.0:0.0', {'label': 'E', 'B': 1}),
        ('v:1.0:0.0', 'v:1.0:0.5', {'label': 'E', 'B': 1}),
        ('v:1.0:0.5', 'v:1.0:1.0', {'label': 'E', 'B': 1}),
        ('v:1.0:1.0', 'v:0.0:1.0', {'label': 'E', 'B': 1}),
        ('v:0.0:1.0', 'v:0.0:0.0', {'label': 'E', 'B': 1}),
        ('Q', 'v:0.0:0.0'), ('Q', 'v:1.0:0.0'), ('Q', 'v:1.0:1.0'), ('Q', 'v:0.0:1.0')
    ])

    return G


def prepare_valid_test_graph_for_prod_8_initial() -> nx.Graph:
    """Prepares the basic 4-nodes and one Q-node graph"""
    G = nx.Graph()
    G.add_node('Q', label='Q', R=0)
    G.add_nodes_from([
        ('v:0.0:0.0', {'label': 'v', 'x': 0.0, 'y': 0.0, 'h': 0}),
        ('v:1.0:0.0', {'label': 'v', 'x': 1.0, 'y': 0.0, 'h': 0}),
        ('v:1.0:1.0', {'label': 'v', 'x': 1.0, 'y': 1.0, 'h': 0}),
        ('v:0.0:1.0', {'label': 'v', 'x': 0.0, 'y': 1.0, 'h': 0}),
        ('v:1.0:0.5', {'label': 'v', 'x': 1.0, 'y': 0.5, 'h': 1}),
        ('v:2.0:0.5', {'label': 'v', 'x': 2.0, 'y': 0.5, 'h': 2}),
        ('v:2.0:1.0', {'label': 'v', 'x': 2.0, 'y': 1.0, 'h': 2}),
        ('Q1', {'label': 'Q', 'R': 1}),
    ])
    G.add_edges_from([
        ('v:1.0:0.0', 'v:1.0:0.5', {'label': 'E', 'B': 1}),
        ('v:1.0:0.5', 'v:1.0:1.0', {'label': 'E', 'B': 1}),
        ('Q', 'v:0.0:0.0'), ('Q', 'v:1.0:0.0'), ('Q', 'v:1.0:1.0'), ('Q', 'v:0.0:1.0'),
        ('Q1', 'v:1.0:1.0'), ('Q1', 'v:1.0:0.5'), ('Q1', 'v:2.0:0.5'), ('Q1', 'v:2.0:1.0')
    ])

    return G


def prepare_non_valid_test_graph_for_prod_8_initial() -> nx.Graph:
    """Prepares the basic 4-nodes and one Q-node graph"""
    G = nx.Graph()
    G.add_node('Q', label='Q', R=0)
    G.add_nodes_from([
        ('v:0.0:0.0', {'label': 'v', 'x': 0.0, 'y': 0.0, 'h': 0}),
        ('v:1.0:0.0', {'label': 'v', 'x': 1.0, 'y': 0.0, 'h': 0}),
        ('v:1.0:1.0', {'label': 'v', 'x': 1.0, 'y': 1.0, 'h': 0}),
        ('v:0.0:1.0', {'label': 'v', 'x': 0.0, 'y': 1.0, 'h': 0}),
        ('v:1.0:0.5', {'label': 'v', 'x': 1.0, 'y': 0.5, 'h': 1}),
        ('v:2.0:0.5', {'label': 'v', 'x': 2.0, 'y': 0.5, 'h': 2}),
        ('v:2.0:1.0', {'label': 'v', 'x': 2.0, 'y': 1.0, 'h': 2}),
        ('Q1', {'label': 'Q', 'R': 0}),
    ])
    G.add_edges_from([
        ('v:1.0:0.0', 'v:1.0:0.5', {'label': 'E', 'B': 1}),
        ('v:1.0:0.5', 'v:1.0:1.0', {'label': 'E', 'B': 1}),
        ('Q', 'v:0.0:0.0'), ('Q', 'v:1.0:0.0'), ('Q', 'v:1.0:1.0'), ('Q', 'v:0.0:1.0'),
        ('Q1', 'v:1.0:1.0'), ('Q1', 'v:1.0:0.5'), ('Q1', 'v:2.0:0.5'), ('Q1', 'v:2.0:1.0')
    ])

    return G


def prepare_valid_test_graph_for_prod_8_after_modification() -> nx.Graph:
    """Prepares the basic 4-nodes and one Q-node graph"""
    G = nx.Graph()
    G.add_node('Q', label='Q', R=1)
    G.add_nodes_from([
        ('v:0.0:0.0', {'label': 'v', 'x': 0.0, 'y': 0.0, 'h': 0}),
        ('v:1.0:0.0', {'label': 'v', 'x': 1.0, 'y': 0.0, 'h': 0}),
        ('v:1.0:1.0', {'label': 'v', 'x': 1.0, 'y': 1.0, 'h': 0}),
        ('v:0.0:1.0', {'label': 'v', 'x': 0.0, 'y': 1.0, 'h': 0}),
        ('v:1.0:0.5', {'label': 'v', 'x': 1.0, 'y': 0.5, 'h': 1}),
        ('v:2.0:0.5', {'label': 'v', 'x': 2.0, 'y': 0.5, 'h': 2}),
        ('v:2.0:1.0', {'label': 'v', 'x': 2.0, 'y': 1.0, 'h': 2}),
        ('Q1', {'label': 'Q', 'R': 1}),
    ])
    G.add_edges_from([
        ('v:1.0:0.0', 'v:1.0:0.5', {'label': 'E', 'B': 1}),
        ('v:1.0:0.5', 'v:1.0:1.0', {'label': 'E', 'B': 1}),
        ('Q', 'v:0.0:0.0'), ('Q', 'v:1.0:0.0'), ('Q', 'v:1.0:1.0'), ('Q', 'v:0.0:1.0'),
        ('Q1', 'v:1.0:1.0'), ('Q1', 'v:1.0:0.5'), ('Q1', 'v:2.0:0.5'), ('Q1', 'v:2.0:1.0')
    ])

    return G


def prepare_valid_test_graph_with_hanging_node_p3() -> nx.Graph:
    """Prepares the basic 4-nodes and one Q-node graph"""
    G = nx.Graph()
    G.add_node('Q', label='Q', R=1)
    G.add_nodes_from([
        ('v:0.0:0.0', {'label': 'v', 'x': 0.0, 'y': 0.0, 'h': 0}),
        ('v:1.0:0.0', {'label': 'v', 'x': 1.0, 'y': 0.0, 'h': 0}),
        ('v:1.0:1.0', {'label': 'v', 'x': 1.0, 'y': 1.0, 'h': 0}),
        ('v:0.0:1.0', {'label': 'v', 'x': 0.0, 'y': 1.0, 'h': 0}),
        ('v:1.0:0.5', {'label': 'v', 'x': 1.0, 'y': 0.5, 'h': 1}),
        ('v:0.5:0.0', {'label': 'v', 'x': 0.5, 'y': 0.0, 'h': 1})

    ])
    G.add_edges_from([
        ('v:0.0:0.0', 'v:0.5:0.0', {'label': 'E', 'B': 1}),
        ('v:0.5:0.0', 'v:1.0:0.0', {'label': 'E', 'B': 1}),
        ('v:1.0:0.0', 'v:1.0:0.5', {'label': 'E', 'B': 1}),
        ('v:1.0:0.5', 'v:1.0:1.0', {'label': 'E', 'B': 1}),
        ('v:1.0:1.0', 'v:0.0:1.0', {'label': 'E', 'B': 1}),
        ('v:0.0:1.0', 'v:0.0:0.0', {'label': 'E', 'B': 1}),
        ('Q', 'v:0.0:0.0'), ('Q', 'v:1.0:0.0'), ('Q', 'v:1.0:1.0'), ('Q', 'v:0.0:1.0')
    ])

    return G


def prepare_valid_test_graph_with_hanging_node_p4() -> nx.Graph:
    """Prepares the basic 4-nodes and one Q-node graph"""
    G = nx.Graph()
    G.add_node('Q', label='Q', R=1)
    G.add_nodes_from([
        ('v:0.0:0.0', {'label': 'v', 'x': 0.0, 'y': 0.0, 'h': 0}),
        ('v:1.0:0.0', {'label': 'v', 'x': 1.0, 'y': 0.0, 'h': 0}),
        ('v:1.0:1.0', {'label': 'v', 'x': 1.0, 'y': 1.0, 'h': 0}),
        ('v:0.0:1.0', {'label': 'v', 'x': 0.0, 'y': 1.0, 'h': 0}),
        ('v:0.0:0.5', {'label': 'v', 'x': 0.0, 'y': 0.5, 'h': 1}),
        ('v:1.0:0.5', {'label': 'v', 'x': 1.0, 'y': 0.5, 'h': 1})

    ])
    G.add_edges_from([
        ('v:0.0:0.0', 'v:0.0:0.5', {'label': 'E', 'B': 1}),
        ('v:0.0:0.5', 'v:0.0:1.0', {'label': 'E', 'B': 1}),
        ('v:1.0:0.0', 'v:1.0:0.5', {'label': 'E', 'B': 1}),
        ('v:1.0:0.5', 'v:1.0:1.0', {'label': 'E', 'B': 1}),
        ('v:1.0:1.0', 'v:0.0:1.0', {'label': 'E', 'B': 1}),
        ('v:0.0:1.0', 'v:0.0:0.0', {'label': 'E', 'B': 1}),
        ('v:0.0:0.0', 'v:1.0:0.0', {'label': 'E', 'B': 1}),
        ('Q', 'v:0.0:0.0'), ('Q', 'v:1.0:0.0'), ('Q', 'v:1.0:1.0'), ('Q', 'v:0.0:1.0')
    ])

    return G


def prepare_valid_test_graph_for_prod_11_initial() -> nx.Graph:
    """Prepares the basic 4-nodes and one Q-node graph"""
    G = nx.Graph()
    G.add_node('P', label='Q', R=1)
    G.add_nodes_from([
        ('v:0.0:0.0', {'label': 'v', 'x': 0.0, 'y': 0.0, 'h': 0}),
        ('v:1.0:0.0', {'label': 'v', 'x': 1.0, 'y': 0.0, 'h': 0}),
        ('v:1.0:1.0', {'label': 'v', 'x': 1.0, 'y': 1.0, 'h': 0}),
        ('v:0.0:1.0', {'label': 'v', 'x': 0.0, 'y': 1.0, 'h': 0}),
        ('v:1.5:0.5', {'label': 'v', 'x': 1.5, 'y': 0.5, 'h': 0}),
        ('v:0.5:0.0', {'label': 'v', 'x': 0.5, 'y': 0.0, 'h': 1}),
        ('v:0.0:0.5', {'label': 'v', 'x': 0.0, 'y': 0.5, 'h': 1}),
    ])
    G.add_edges_from([
        ('v:1.0:1.0', 'v:0.0:1.0', {'label': 'E', 'B': 1}),
        ('v:1.0:0.0', 'v:1.5:0.5', {'label': 'E', 'B': 1}),
        ('v:1.5:0.5', 'v:1.0:1.0', {'label': 'E', 'B': 1}),

        ('v:0.5:0.0', 'v:0.0:0.0', {'label': 'E', 'B': 1}),
        ('v:1.0:0.0', 'v:0.5:0.0', {'label': 'E', 'B': 1}),
        ('v:0.0:0.0', 'v:0.0:0.5', {'label': 'E', 'B': 1}),
        ('v:0.0:0.5', 'v:0.0:1.0', {'label': 'E', 'B': 1}),

        ('P', 'v:0.0:0.0'), ('P', 'v:1.0:0.0'), ('P', 'v:1.0:1.0'), ('P', 'v:0.0:1.0'),
        ('P', 'v:1.5:0.5')
    ])

    return G


def prepare_valid_test_graph_for_prod_11_big_1() -> nx.Graph:
    """Prepares the basic 4-nodes and one Q-node graph"""
    G = nx.Graph()
    G.add_node('P', label='Q', R=1)
    G.add_nodes_from([
        ('v:0.0:0.0', {'label': 'v', 'x': 0.0, 'y': 0.0, 'h': 0}),
        ('v:1.0:0.0', {'label': 'v', 'x': 1.0, 'y': 0.0, 'h': 0}),
        ('v:1.0:-1.0', {'label': 'v', 'x': 1.0, 'y': -1.0, 'h': 0}),
        ('v:-1.0:-1.0', {'label': 'v', 'x': -1.0, 'y': -1.0, 'h': 1}),

        ('v:1.0:1.0', {'label': 'v', 'x': 1.0, 'y': 1.0, 'h': 0}),
        ('v:0.0:1.0', {'label': 'v', 'x': 0.0, 'y': 1.0, 'h': 0}),
        ('v:-1.0:1.0', {'label': 'v', 'x': -1.0, 'y': 1.0, 'h': 0}),

        ('v:1.5:0.5', {'label': 'v', 'x': 1.5, 'y': 0.5, 'h': 0}),
        ('v:0.5:0.0', {'label': 'v', 'x': 0.5, 'y': 0.0, 'h': 1}),

        ('v:0.0:0.5', {'label': 'v', 'x': 0.0, 'y': 0.5, 'h': 1}),
        ('v:0.0:2.0', {'label': 'v', 'x': 0.0, 'y': 2.0, 'h': 1}),
        ('Q1', {'label': 'Q', 'R': 0}),
        ('Q2', {'label': 'Q', 'R': 0}),
        ('Q3', {'label': 'Q', 'R': 0}),

    ])
    G.add_edges_from([
        ('v:1.0:1.0', 'v:0.0:1.0', {'label': 'E', 'B': 1}),
        ('v:1.0:0.0', 'v:1.5:0.5', {'label': 'E', 'B': 1}),
        ('v:1.5:0.5', 'v:1.0:1.0', {'label': 'E', 'B': 1}),

        ('v:0.5:0.0', 'v:0.0:0.0', {'label': 'E', 'B': 1}),
        ('v:1.0:0.0', 'v:0.5:0.0', {'label': 'E', 'B': 1}),
        ('v:0.0:0.0', 'v:0.0:0.5', {'label': 'E', 'B': 1}),
        ('v:0.0:0.5', 'v:0.0:1.0', {'label': 'E', 'B': 1}),

        ('v:1.0:-1.0', 'v:1.0:0.0', {'label': 'E', 'B': 1}),
        ('v:1.0:-1.0', 'v:-1.0:-1.0', {'label': 'E', 'B': 1}),

        ('v:-1.0:-1.0', 'v:0.0:0.0', {'label': 'E', 'B': 1}),
        ('v:-1.0:-1.0', 'v:-1.0:1.0', {'label': 'E', 'B': 1}),
        ('v:0.0:1.0', 'v:-1.0:1.0', {'label': 'E', 'B': 1}),

        ('v:0.0:2.0', 'v:-1.0:1.0', {'label': 'E', 'B': 1}),
        ('v:0.0:2.0', 'v:1.0:1.0', {'label': 'E', 'B': 1}),

        ('P', 'v:0.0:0.0'), ('P', 'v:1.0:0.0'), ('P', 'v:1.0:1.0'), ('P', 'v:0.0:1.0'),
        ('P', 'v:1.5:0.5'),
        ('Q1', 'v:0.0:0.0'), ('Q1', 'v:1.0:0.0'), ('Q1', 'v:1.0:-1.0'), ('Q1', 'v:-1.0:-1.0'),
        ('Q2', 'v:0.0:0.0'), ('Q2', 'v:-1.0:-1.0'), ('Q2', 'v:-1.0:1.0'), ('Q2', 'v:0.0:1.0'),
        ('Q3', 'v:0.0:2.0'), ('Q3', 'v:1.0:1.0'), ('Q3', 'v:-1.0:1.0'), ('Q3', 'v:0.0:1.0'),

    ])

    return G


def prepare_valid_test_graph_for_prod_11_big_2() -> nx.Graph:
    """Prepares the basic 4-nodes and one Q-node graph"""
    G = nx.Graph()
    G.add_node('P', label='Q', R=1)
    G.add_nodes_from([
        ('v:0.0:0.0', {'label': 'v', 'x': 0.0, 'y': 0.0, 'h': 0}),
        ('v:1.0:0.0', {'label': 'v', 'x': 1.0, 'y': 0.0, 'h': 0}),
        ('v:1.0:-1.0', {'label': 'v', 'x': 1.0, 'y': -1.0, 'h': 0}),
        ('v:-1.0:-1.0', {'label': 'v', 'x': -1.0, 'y': -1.0, 'h': 1}),

        ('v:1.0:1.0', {'label': 'v', 'x': 1.0, 'y': 1.0, 'h': 0}),
        ('v:0.0:1.0', {'label': 'v', 'x': 0.0, 'y': 1.0, 'h': 0}),
        ('v:-1.0:1.0', {'label': 'v', 'x': -1.0, 'y': 1.0, 'h': 0}),

        ('v:1.5:0.5', {'label': 'v', 'x': 1.5, 'y': 0.5, 'h': 0}),
        ('v:0.5:0.0', {'label': 'v', 'x': 0.5, 'y': 0.0, 'h': 1}),

        ('v:0.0:2.0', {'label': 'v', 'x': 0.0, 'y': 2.0, 'h': 1}),
        ('v:0.5:1.0', {'label': 'v', 'x': 0.5, 'y': 1.0, 'h': 1}),
        ('Q1', {'label': 'Q', 'R': 0}),
        ('Q2', {'label': 'Q', 'R': 0}),
        ('Q3', {'label': 'Q', 'R': 0}),

    ])
    G.add_edges_from([
        ('v:0.5:1.0', 'v:0.0:1.0', {'label': 'E', 'B': 1}),
        ('v:1.0:1.0', 'v:0.5:1.0', {'label': 'E', 'B': 1}),

        ('v:1.0:0.0', 'v:1.5:0.5', {'label': 'E', 'B': 1}),
        ('v:1.5:0.5', 'v:1.0:1.0', {'label': 'E', 'B': 1}),

        ('v:0.5:0.0', 'v:0.0:0.0', {'label': 'E', 'B': 1}),
        ('v:1.0:0.0', 'v:0.5:0.0', {'label': 'E', 'B': 1}),
        ('v:0.0:0.0', 'v:0.0:1.0', {'label': 'E', 'B': 1}),

        ('v:1.0:-1.0', 'v:1.0:0.0', {'label': 'E', 'B': 1}),
        ('v:1.0:-1.0', 'v:-1.0:-1.0', {'label': 'E', 'B': 1}),

        ('v:-1.0:-1.0', 'v:0.0:0.0', {'label': 'E', 'B': 1}),
        ('v:-1.0:-1.0', 'v:-1.0:1.0', {'label': 'E', 'B': 1}),
        ('v:0.0:2.0', 'v:-1.0:1.0', {'label': 'E', 'B': 1}),

        ('v:0.0:1.0', 'v:-1.0:1.0', {'label': 'E', 'B': 1}),

        ('v:0.0:2.0', 'v:1.0:1.0', {'label': 'E', 'B': 1}),

        ('P', 'v:0.0:0.0'), ('P', 'v:1.0:0.0'), ('P', 'v:1.0:1.0'), ('P', 'v:0.0:1.0'),
        ('P', 'v:1.5:0.5'),
        ('Q1', 'v:0.0:0.0'), ('Q1', 'v:1.0:0.0'), ('Q1', 'v:1.0:-1.0'), ('Q1', 'v:-1.0:-1.0'),
        ('Q2', 'v:-1.0:-1.0'), ('Q2', 'v:-1.0:1.0'), ('Q2', 'v:0.0:0.0'), ('Q2', 'v:0.0:1.0'),
        ('Q3', 'v:0.0:2.0'), ('Q3', 'v:-1.0:1.0'), ('Q3', 'v:1.0:1.0'), ('Q3', 'v:0.0:1.0'),

    ])

    return G


def prepare_valid_test_graph_for_prod_11_big_3() -> nx.Graph:
    """Prepares the basic 4-nodes and one Q-node graph"""
    G = nx.Graph()
    G.add_node('P', label='Q', R=1)
    G.add_nodes_from([
        ('v:0.0:0.0', {'label': 'v', 'x': 0.0, 'y': 0.0, 'h': 0}),
        ('v:1.0:0.0', {'label': 'v', 'x': 1.0, 'y': 0.0, 'h': 0}),
        ('v:-0.5:-0.5', {'label': 'v', 'x': -0.5, 'y': -0.5, 'h': 0}),
        ('v:1.0:-1.0', {'label': 'v', 'x': 1.0, 'y': -1.0, 'h': 0}),
        ('v:-1.0:-1.0', {'label': 'v', 'x': -1.0, 'y': -1.0, 'h': 1}),

        ('v:1.0:1.0', {'label': 'v', 'x': 1.0, 'y': 1.0, 'h': 0}),
        ('v:0.0:1.0', {'label': 'v', 'x': 0.0, 'y': 1.0, 'h': 0}),
        ('v:-0.5:1.0', {'label': 'v', 'x': -0.5, 'y': 1.0, 'h': 0}),
        ('v:-1.0:1.0', {'label': 'v', 'x': -1.0, 'y': 1.0, 'h': 0}),

        ('v:1.5:0.5', {'label': 'v', 'x': 1.5, 'y': 0.5, 'h': 0}),
        ('v:0.5:0.0', {'label': 'v', 'x': 0.5, 'y': 0.0, 'h': 1}),

        ('v:0.0:2.0', {'label': 'v', 'x': 0.0, 'y': 2.0, 'h': 1}),
        ('v:1.0:2.0', {'label': 'v', 'x': 1.0, 'y': 2.0, 'h': 1}),
        ('v:0.5:1.0', {'label': 'v', 'x': 0.5, 'y': 1.0, 'h': 1}),
        ('Q1', {'label': 'Q', 'R': 0}),
        ('Q2', {'label': 'Q', 'R': 0}),
        ('Q3', {'label': 'Q', 'R': 1}),
        ('Q4', {'label': 'Q', 'R': 1}),

    ])
    G.add_edges_from([
        ('v:0.5:1.0', 'v:0.0:1.0', {'label': 'E', 'B': 1}),
        ('v:1.0:1.0', 'v:0.5:1.0', {'label': 'E', 'B': 1}),

        ('v:1.0:0.0', 'v:1.5:0.5', {'label': 'E', 'B': 1}),
        ('v:1.5:0.5', 'v:1.0:1.0', {'label': 'E', 'B': 1}),

        ('v:0.5:0.0', 'v:0.0:0.0', {'label': 'E', 'B': 1}),
        ('v:1.0:0.0', 'v:0.5:0.0', {'label': 'E', 'B': 1}),
        ('v:0.0:0.0', 'v:0.0:1.0', {'label': 'E', 'B': 1}),

        ('v:1.0:-1.0', 'v:1.0:0.0', {'label': 'E', 'B': 1}),
        ('v:1.0:-1.0', 'v:-1.0:-1.0', {'label': 'E', 'B': 1}),

        ('v:-1.0:-1.0', 'v:-0.5:-0.5', {'label': 'E', 'B': 1}),
        ('v:0.0:0.0', 'v:-0.5:-0.5', {'label': 'E', 'B': 1}),
        ('v:-1.0:-1.0', 'v:-1.0:1.0', {'label': 'E', 'B': 1}),
        ('v:0.0:2.0', 'v:-1.0:1.0', {'label': 'E', 'B': 1}),

        ('v:-0.5:1.0', 'v:-1.0:1.0', {'label': 'E', 'B': 1}),
        ('v:-0.5:1.0', 'v:0.0:1.0', {'label': 'E', 'B': 1}),

        ('v:0.0:2.0', 'v:1.0:2.0', {'label': 'E', 'B': 1}),
        ('v:1.0:2.0', 'v:1.0:1.0', {'label': 'E', 'B': 1}),
        ('v:-0.5:1.0', 'v:-0.5:-0.5', {'label': 'E', 'B': 1}),

        ('P', 'v:0.0:0.0'), ('P', 'v:1.0:0.0'), ('P', 'v:1.0:1.0'), ('P', 'v:0.0:1.0'),
        ('P', 'v:1.5:0.5'),
        ('Q1', 'v:0.0:0.0'), ('Q1', 'v:1.0:0.0'), ('Q1', 'v:1.0:-1.0'), ('Q1', 'v:-1.0:-1.0'),
        ('Q2', 'v:-1.0:1.0'), ('Q2', 'v:0.0:2.0'), ('Q2', 'v:1.0:1.0'), ('Q2', 'v:0.0:1.0'),
        ('Q2', 'v:1.0:2.0'),
        ('Q3', 'v:-0.5:-0.5'), ('Q3', 'v:-0.5:1.0'), ('Q3', 'v:0.0:1.0'), ('Q3', 'v:0.0:0.0'),
        ('Q4', 'v:-0.5:-0.5'), ('Q4', 'v:-0.5:1.0'), ('Q4', 'v:-1.0:-1.0'), ('Q4', 'v:-1.0:1.0'),

    ])

    return G


def prepare_valid_test_graph_for_prod_11_after_modification() -> nx.Graph:
    """Prepares the graph after applying Production P11 (final version matching the second screenshot)."""
    G = nx.Graph()

    G.add_nodes_from([
        ('v:1', {'label': 'v', 'x': 0.0, 'y': 1.0, 'h': 0}),
        ('v:2', {'label': 'v', 'x': 1.0, 'y': 1.0, 'h': 0}),
        ('v:3', {'label': 'v', 'x': 1.0, 'y': 0.0, 'h': 0}),
        ('v:4', {'label': 'v', 'x': 0.0, 'y': 0.0, 'h': 0}),
        ('v:5', {'label': 'v', 'x': 1.5, 'y': 0.5, 'h': 0}),
        ('v:6', {'label': 'v', 'x': 0.5, 'y': 0.0, 'h': 0}),
        ('v:7', {'label': 'v', 'x': 0.0, 'y': 0.5, 'h': 0}),
        ('v:8', {'label': 'v', 'x': 0.5, 'y': 1.0, 'h': -1}),
        ('v:9', {'label': 'v', 'x': 1.25, 'y': 0.75, 'h': -1}),
        ('v:10', {'label': 'v', 'x': 1.25, 'y': 0.25, 'h': -1}),
        ('v:11', {'label': 'v', 'x': 0.7, 'y': 0.5, 'h': 0}),
    ])

    G.add_nodes_from([
        ('Q1', {'label': 'Q', 'R': 0}),
        ('Q2', {'label': 'Q', 'R': 0}),
        ('Q3', {'label': 'Q', 'R': 0}),
        ('Q4', {'label': 'Q', 'R': 0}),
        ('Q5', {'label': 'Q', 'R': 0}),
    ])

    G.add_edges_from([
        ('v:6', 'v:4', {'label': 'E', 'B': 1}),
        ('v:6', 'v:3', {'label': 'E', 'B': 1}),
        ('v:7', 'v:1', {'label': 'E', 'B': 1}),
        ('v:7', 'v:4', {'label': 'E', 'B': 1}),
        ('v:11', 'v:6', {'label': 'E', 'B': 1}),
        ('v:11', 'v:7', {'label': 'E', 'B': 1}),
        ('v:11', 'v:8', {'label': 'E', 'B': 1}),
        ('v:11', 'v:9', {'label': 'E', 'B': 1}),
        ('v:11', 'v:10', {'label': 'E', 'B': 1}),
        ('v:8', 'v:1', {'label': 'E', 'B': 1}),
        ('v:8', 'v:2', {'label': 'E', 'B': 1}),
        ('v:9', 'v:2', {'label': 'E', 'B': 1}),
        ('v:9', 'v:5', {'label': 'E', 'B': 1}),
        ('v:10', 'v:3', {'label': 'E', 'B': 1}),
        ('v:10', 'v:5', {'label': 'E', 'B': 1}),
        ('Q1', 'v:1'), ('Q1', 'v:8'), ('Q1', 'v:11'), ('Q1', 'v:7'),
        ('Q2', 'v:4'), ('Q2', 'v:6'), ('Q2', 'v:11'), ('Q2', 'v:7'),
        ('Q3', 'v:3'), ('Q3', 'v:10'), ('Q3', 'v:11'), ('Q3', 'v:6'),
        ('Q4', 'v:5'), ('Q4', 'v:11'), ('Q4', 'v:10'), ('Q4', 'v:9'),
        ('Q5', 'v:2'), ('Q5', 'v:9'), ('Q5', 'v:8'), ('Q5', 'v:11'),
    ])

    return G


def prepare_non_valid_test_graph_for_prod_11_initial() -> nx.Graph:
    """Prepares the basic 4-nodes and one Q-node graph"""
    G = nx.Graph()
    G.add_node('P', label='Q', R=1)
    G.add_nodes_from([
        ('v:0.0:0.0', {'label': 'v', 'x': 0.0, 'y': 0.0, 'h': 0}),
        ('v:1.0:0.0', {'label': 'v', 'x': 1.0, 'y': 0.0, 'h': 0}),
        ('v:1.0:1.0', {'label': 'v', 'x': 1.0, 'y': 1.0, 'h': 0}),
        ('v:0.0:1.0', {'label': 'v', 'x': 0.0, 'y': 1.0, 'h': 0}),
        ('v:1.5:0.5', {'label': 'v', 'x': 1.5, 'y': 0.5, 'h': 0}),
        ('v:0.5:0.0', {'label': 'v', 'x': 0.5, 'y': 0.0, 'h': 0}),
        ('v:0.0:0.5', {'label': 'v', 'x': 0.0, 'y': 0.5, 'h': 1}),
    ])
    G.add_edges_from([
        ('v:1.0:1.0', 'v:0.0:1.0', {'label': 'E', 'B': 1}),
        ('v:1.0:0.0', 'v:1.5:0.5', {'label': 'E', 'B': 1}),
        ('v:1.5:0.5', 'v:1.0:1.0', {'label': 'E', 'B': 1}),

        ('v:0.5:0.0', 'v:0.0:0.0', {'label': 'E', 'B': 1}),
        ('v:1.0:0.0', 'v:0.5:0.0', {'label': 'E', 'B': 1}),
        ('v:0.0:0.0', 'v:0.0:0.5', {'label': 'E', 'B': 1}),
        ('v:0.0:0.5', 'v:0.0:1.0', {'label': 'E', 'B': 1}),

        ('P', 'v:0.0:0.0'), ('P', 'v:1.0:0.0'), ('P', 'v:1.0:1.0'), ('P', 'v:0.0:1.0'),
        ('P', 'v:1.5:0.5')
    ])

    return G


def prepare_graph_with_R0_quadrilateral() -> nx.Graph:
    """Prepares a graph with a quadrilateral element where R == 0."""
    G = nx.Graph()
    G.add_node('Q1', label='Q', R=0)
    G.add_nodes_from([
        ('v0', {'label': 'v', 'x': 0, 'y': 0}),
        ('v1', {'label': 'v', 'x': 1, 'y': 0}),
        ('v2', {'label': 'v', 'x': 1, 'y': 1}),
        ('v3', {'label': 'v', 'x': 0, 'y': 1})
    ])
    G.add_edges_from([
        ('Q1', 'v0'),
        ('Q1', 'v1'),
        ('Q1', 'v2'),
        ('Q1', 'v3')
    ])
    G.add_edges_from([
        ('v0', 'v1'),
        ('v1', 'v2'),
        ('v2', 'v3'),
        ('v3', 'v0')
    ])
    return G


def prepare_graph_without_R0_quadrilateral() -> nx.Graph:
    """Prepares a graph where no quadrilateral elements have R == 0."""
    G = nx.Graph()
    G.add_node('Q1', label='Q', R=1)
    G.add_nodes_from([
        ('v0', {'label': 'v', 'x': 0, 'y': 0}),
        ('v1', {'label': 'v', 'x': 1, 'y': 0}),
        ('v2', {'label': 'v', 'x': 1, 'y': 1}),
        ('v3', {'label': 'v', 'x': 0, 'y': 1})
    ])
    G.add_edges_from([
        ('Q1', 'v0'),
        ('Q1', 'v1'),
        ('Q1', 'v2'),
        ('Q1', 'v3')
    ])
    G.add_edges_from([
        ('v0', 'v1'),
        ('v1', 'v2'),
        ('v2', 'v3'),
        ('v3', 'v0')
    ])
    return G


def prepare_valid_test_graph_for_prod_17_initial() -> nx.Graph:
    """Prepares the basic 4-nodes and one P-node graph"""
    G = nx.Graph()
    G.add_node('P', label='Q', R=0)
    G.add_nodes_from([
        ('v:0.0:0.0', {'label': 'v', 'x': 0.0, 'y': 0.0, 'h': 0}),
        ('v:0.5:0.0', {'label': 'v', 'x': 0.5, 'y': 0.0, 'h': 0}),
        ('v:1.0:0.0', {'label': 'v', 'x': 1.0, 'y': 0.0, 'h': 0}),
        ('v:1.0:1.0', {'label': 'v', 'x': 1.0, 'y': 1.0, 'h': 0}),
        ('v:0.0:1.0', {'label': 'v', 'x': 0.0, 'y': 1.0, 'h': 0}),
        ('v:1.0:0.5', {'label': 'v', 'x': 1.0, 'y': 0.5, 'h': 1}),
        ('v:2.0:0.5', {'label': 'v', 'x': 2.0, 'y': 0.5, 'h': 2}),
        ('v:2.0:1.0', {'label': 'v', 'x': 2.0, 'y': 1.0, 'h': 2}),
        ('Q', {'label': 'Q', 'R': 1}),
    ])
    G.add_edges_from([
        ('v:1.0:0.0', 'v:1.0:0.5', {'label': 'E', 'B': 1}),
        ('v:1.0:0.5', 'v:1.0:1.0', {'label': 'E', 'B': 1}),
        ('P', 'v:0.0:0.0'), ('P', 'v:1.0:0.0'), ('P', 'v:1.0:1.0'), ('P', 'v:0.0:1.0'),
        ('P', 'v:0.5:0.0'), ('Q', 'v:1.0:1.0'), ('Q', 'v:1.0:0.5'), ('Q', 'v:2.0:0.5'), ('Q', 'v:2.0:1.0')
    ])

    return G


def prepare_non_valid_test_graph_for_prod_17_initial() -> nx.Graph:
    """Prepares the basic 4-nodes and one P-node graph"""
    G = nx.Graph()
    G.add_node('P', label='Q', R=0)
    G.add_nodes_from([
        ('v:0.0:0.0', {'label': 'v', 'x': 0.0, 'y': 0.0, 'h': 0}),
        ('v:0.5:0.0', {'label': 'v', 'x': 0.5, 'y': 0.0, 'h': 0}),
        ('v:1.0:0.0', {'label': 'v', 'x': 1.0, 'y': 0.0, 'h': 0}),
        ('v:1.0:1.0', {'label': 'v', 'x': 1.0, 'y': 1.0, 'h': 0}),
        ('v:0.0:1.0', {'label': 'v', 'x': 0.0, 'y': 1.0, 'h': 0}),
        ('v:1.0:0.5', {'label': 'v', 'x': 1.0, 'y': 0.5, 'h': 1}),
        ('v:2.0:0.5', {'label': 'v', 'x': 2.0, 'y': 0.5, 'h': 2}),
        ('v:2.0:1.0', {'label': 'v', 'x': 2.0, 'y': 1.0, 'h': 2}),
        ('Q', {'label': 'Q', 'R': 0}),
    ])
    G.add_edges_from([
        ('v:1.0:0.0', 'v:1.0:0.5', {'label': 'E', 'B': 1}),
        ('v:1.0:0.5', 'v:1.0:1.0', {'label': 'E', 'B': 1}),
        ('P', 'v:0.0:0.0'), ('P', 'v:1.0:0.0'), ('P', 'v:1.0:1.0'), ('P', 'v:0.0:1.0'),
        ('P', 'v:0.5:0.0'), ('Q', 'v:1.0:1.0'), ('Q', 'v:1.0:0.5'), ('Q', 'v:2.0:0.5'), ('Q', 'v:2.0:1.0')
    ])

    return G


def prepare_valid_test_graph_for_prod_17_after_modification() -> nx.Graph:
    """Prepares the basic 4-nodes and one P-node graph"""
    G = nx.Graph()
    G.add_node('P', label='Q', R=1)
    G.add_nodes_from([
        ('v:0.0:0.0', {'label': 'v', 'x': 0.0, 'y': 0.0, 'h': 0}),
        ('v:0.5:0.0', {'label': 'v', 'x': 0.5, 'y': 0.0, 'h': 0}),
        ('v:1.0:0.0', {'label': 'v', 'x': 1.0, 'y': 0.0, 'h': 0}),
        ('v:1.0:1.0', {'label': 'v', 'x': 1.0, 'y': 1.0, 'h': 0}),
        ('v:0.0:1.0', {'label': 'v', 'x': 0.0, 'y': 1.0, 'h': 0}),
        ('v:1.0:0.5', {'label': 'v', 'x': 1.0, 'y': 0.5, 'h': 1}),
        ('v:2.0:0.5', {'label': 'v', 'x': 2.0, 'y': 0.5, 'h': 2}),
        ('v:2.0:1.0', {'label': 'v', 'x': 2.0, 'y': 1.0, 'h': 2}),
        ('Q', {'label': 'Q', 'R': 1}),
    ])
    G.add_edges_from([
        ('v:1.0:0.0', 'v:1.0:0.5', {'label': 'E', 'B': 1}),
        ('v:1.0:0.5', 'v:1.0:1.0', {'label': 'E', 'B': 1}),
        ('P', 'v:0.0:0.0'), ('P', 'v:1.0:0.0'), ('P', 'v:1.0:1.0'), ('P', 'v:0.0:1.0'),
        ('P', 'v:0.5:0.0'), ('Q', 'v:1.0:1.0'), ('Q', 'v:1.0:0.5'), ('Q', 'v:2.0:0.5'), ('Q', 'v:2.0:1.0')
    ])

    return G


def prepare_corrupted_test_graph() -> nx.Graph:
    """Prepares the basic 4-nodes graph"""
    G = nx.Graph()
    G.add_nodes_from([
        ('v:0.0:0.0', {'label': 'v', 'x': 0, 'y': 0, 'h': 0}),
        ('v:1.0:0.0', {'label': 'v', 'x': 1, 'y': 0, 'h': 0}),
        ('v:1.0:1.0', {'label': 'v', 'x': 1, 'y': 1, 'h': 0}),
        ('v:0.0:1.0', {'label': 'v', 'x': 0, 'y': 1, 'h': 0})
    ])
    G.add_edges_from([
        ('v:0.0:0.0', 'v:1.0:0.0', {'label': 'E', 'B': 1}),
        ('v:1.0:0.0', 'v:1.0:1.0', {'label': 'E', 'B': 1}),
        ('v:1.0:1.0', 'v:0.0:1.0', {'label': 'E', 'B': 1}),
        ('v:0.0:1.0', 'v:0.0:0.0', {'label': 'E', 'B': 1}),
    ])

    return G
