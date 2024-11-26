import pytest
import networkx as nx

from pytest import FixtureRequest

from productions.p10.production10 import ProductionP10
from productions.utils import prepare_valid_test_graph, prepare_corrupted_test_graph, \
    prepare_valid_test_graph_with_hanging_node

G = prepare_valid_test_graph()
G_h = prepare_valid_test_graph_with_hanging_node()
G_n = prepare_corrupted_test_graph()


@pytest.fixture(scope='function', params=[G])
def prepare_graph_without_hanging(request: type[FixtureRequest]):
    G = nx.Graph()
    G.add_node("P:5.0:5.0", label="P", R=1)
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


@pytest.fixture(scope='function', params=[G_h])
def prepare_graph_hanging(request: type[FixtureRequest]):
    G = nx.Graph()
    G.add_node("P:5.0:5.0", label="P", R=1)
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

    yield G


@pytest.fixture(scope='function', params=[G_n])
def prepare_graph_negative(request: type[FixtureRequest]):
    yield prepare_corrupted_test_graph()

def test_positive_p10_check_without_hanging_node(prepare_graph_without_hanging: nx.Graph):
    """check is not None if the graph is valid"""
    assert ProductionP10(prepare_graph_without_hanging).check is None

def test_positive_p10_check(prepare_graph_hanging: nx.Graph):
    """check is not None if the graph is valid"""
    assert ProductionP10(prepare_graph_hanging).check is not None

def test_positive_p10_nodes_number_after_production(prepare_graph_hanging: nx.Graph):
    """apply creates new node in graph, verify nodes number"""
    ProductionP10(prepare_graph_hanging).apply()
    expected_nodes_number = 16
    assert len(prepare_graph_hanging.nodes()) == expected_nodes_number


def test_positive_p10_v_nodes_number_after_production(prepare_graph_hanging: nx.Graph):
    """apply creates new node in graph, verify v nodes number"""
    ProductionP10(prepare_graph_hanging).apply()
    expected_v_nodes_number = 11
    assert len([s for s in prepare_graph_hanging.nodes() if 'v' in s]) == expected_v_nodes_number


def test_positive_p10_q_nodes_number_after_production(prepare_graph_hanging: nx.Graph):
    """apply creates new node in graph, verify g nodes number"""
    ProductionP10(prepare_graph_hanging).apply()
    expected_q_nodes_number = 5
    assert len([s for s in prepare_graph_hanging.nodes() if 'Q' in s]) == expected_q_nodes_number
