import pytest
import networkx as nx

from pytest import FixtureRequest

from productions.p09.production09 import ProductionP9
from productions.utils import (
    prepare_valid_test_graph,
    prepare_corrupted_test_graph,
    prepare_valid_test_graph_with_hanging_node,
)

G = prepare_valid_test_graph()
G_h = prepare_valid_test_graph_with_hanging_node()
G_n= prepare_corrupted_test_graph()

@pytest.fixture(scope="function")
def prepare_graph_positive():
    yield prepare_valid_test_graph()

@pytest.fixture(scope="function")
def prepare_graph_positive_hanging():
    yield prepare_valid_test_graph_with_hanging_node()

@pytest.fixture(scope="function")
def prepare_graph_negative():
    yield prepare_corrupted_test_graph()

def test_positive_p16_check(prepare_graph_positive: nx.Graph):
    """check is not None if the graph is valid"""
    assert ProductionP16(prepare_graph_positive).check is not None

def test_negative_p16_check(prepare_graph_negative: nx.Graph):
    """check is None if the graph is not valid"""
    assert ProductionP16(prepare_graph_negative).check is None

def test_negative_p16_apply(prepare_graph_negative: nx.Graph):
    """apply creates new node in graph due to the graph is invalid"""
    ProductionP16(prepare_graph_negative).apply()
    assert 'P' not in prepare_graph_negative


def prepare_valid_test_graph() -> nx.Graph:
    """Prepares the basic 5-nodes and one P-node graph"""
    G = nx.Graph()
    G.add_node("P:5.0:5.0", label="P", R=0)
    G.add_nodes_from(
        [
            ("v:0.0:0.0", {"label": "v", "x": 0.0, "y": 0.0, "h": 0}),
            ("v:10.0:0.0", {"label": "v", "x": 10.0, "y": 0.0, "h": 0}),
            ("v:10.0:10.0", {"label": "v", "x": 10.0, "y": 10.0, "h": 0}),
            ("v:0.0:10.0", {"label": "v", "x": 0.0, "y": 10.0, "h": 0}),
            ("v:15.0:5.0", {"label": "v", "x": 15.0, "y": 5.0, "h": 0}),
        ]
    )
    G.add_edges_from(
        [
            ("v:0.0:0.0", "v:10.0:0.0", {"label": "E", "B": 1}),
            ("v:15.0:5.0", "v:10.0:10.0", {"label": "E", "B": 1}),
            ("v:10.0:0.0", "v:15.0:5.0", {"label": "E", "B": 1}),
            ("v:10.0:10.0", "v:0.0:10.0", {"label": "E", "B": 1}),
            ("v:0.0:10.0", "v:0.0:0.0", {"label": "E", "B": 1}),
            ("P:5.0:5.0", "v:0.0:0.0"),
            ("P:5.0:5.0", "v:15.0:5.0"),
            ("P:5.0:5.0", "v:10.0:0.0"),
            ("P:5.0:5.0", "v:10.0:10.0"),
            ("P:5.0:5.0", "v:0.0:10.0"),
        ]
    )
    return G


def prepare_valid_test_graph_with_hanging_node() -> nx.Graph:
    """Prepares the basic 5-nodes and one P-node graph"""
    G = nx.Graph()
    G.add_node("P:5.0:5.0", label="P", R=0)
    G.add_nodes_from(
        [
            ("v:0.0:0.0", {"label": "v", "x": 0.0, "y": 0.0, "h": 0}),
            ("v:5.0:0.0", {"label": "v", "x": 5.0, "y": 0.0, "h": 0}),
            ("v:10.0:0.0", {"label": "v", "x": 10.0, "y": 0.0, "h": 0}),
            ("v:10.0:10.0", {"label": "v", "x": 10.0, "y": 10.0, "h": 0}),
            ("v:0.0:10.0", {"label": "v", "x": 0.0, "y": 10.0, "h": 0}),
            ("v:15.0:5.0", {"label": "v", "x": 15.0, "y": 5.0, "h": 0}),
        ]
    )
    G.add_edges_from(
        [
            ("v:0.0:0.0", "v:5.0:0.0", {"label": "E", "B": 1}),
            ("v:5.0:0.0", "v:10.0:0.0", {"label": "E", "B": 1}),
            ("v:15.0:5.0", "v:10.0:10.0", {"label": "E", "B": 1}),
            ("v:10.0:0.0", "v:15.0:5.0", {"label": "E", "B": 1}),
            ("v:10.0:10.0", "v:0.0:10.0", {"label": "E", "B": 1}),
            ("v:0.0:10.0", "v:0.0:0.0", {"label": "E", "B": 1}),
            ("P:5.0:5.0", "v:0.0:0.0"),
            ("P:5.0:5.0", "v:15.0:5.0"),
            ("P:5.0:5.0", "v:10.0:0.0"),
            ("P:5.0:5.0", "v:10.0:10.0"),
            ("P:5.0:5.0", "v:0.0:10.0"),
        ]
    )
    return G


def prepare_corrupted_test_graph() -> nx.Graph:
    """Prepares the basic 5-nodes graph"""
    G = nx.Graph()
    G.add_node("P:5.0:5.0", label="P", R=1)
    G.add_nodes_from(
        [
            ("v:0.0:0.0", {"label": "v", "x": 0, "y": 0, "h": 0}),
            ("v:1.0:0.0", {"label": "v", "x": 1, "y": 0, "h": 0}),
            ("v:1.0:1.0", {"label": "v", "x": 1, "y": 1, "h": 0}),
            ("v:0.0:1.0", {"label": "v", "x": 0, "y": 1, "h": 0}),
        ]
    )
    G.add_edges_from(
        [
            ("v:0.0:0.0", "v:1.0:0.0", {"label": "E", "B": 1}),
            ("v:1.0:0.0", "v:1.0:1.0", {"label": "E", "B": 1}),
            ("v:1.0:1.0", "v:0.0:1.0", {"label": "E", "B": 1}),
            ("v:0.0:1.0", "v:0.0:0.0", {"label": "E", "B": 1}),
        ]
    )
    return G
