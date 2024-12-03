import pytest
import networkx as nx


from productions.p09.production09 import ProductionP9
from productions.utils import (
    prepare_valid_test_graph,
    prepare_corrupted_test_graph,
    prepare_valid_test_graph_with_hanging_node,
)


G = prepare_valid_test_graph()
G_h = prepare_valid_test_graph_with_hanging_node()
G_n = prepare_corrupted_test_graph()


@pytest.fixture(scope="function")
def prepare_graph_positive():
    yield prepare_valid_test_graph()


@pytest.fixture(scope="function")
def prepare_graph_positive_hanging():
    yield prepare_valid_test_graph_with_hanging_node()


@pytest.fixture(scope="function")
def prepare_graph_negative():
    yield prepare_corrupted_test_graph()


def test_positive_p09_check(prepare_graph_positive: nx.Graph):
    """check is not None if the graph is valid"""
    assert ProductionP9(prepare_graph_positive).check is not None


def test_positive_p09_check_after_production(prepare_graph_positive: nx.Graph):
    """check is not None if the graph is valid"""
    ProductionP9(prepare_graph_positive).apply()
    assert ProductionP9(prepare_graph_positive).check is None


def test_positive_p09_nodes_number_after_production(prepare_graph_positive: nx.Graph):
    """verify nodes number, after applying the production"""
    ProductionP9(prepare_graph_positive).apply()
    expected_nodes_number = 16
    assert len(prepare_graph_positive.nodes()) == expected_nodes_number


def test_positive_p09_v_nodes_number_after_production(prepare_graph_positive: nx.Graph):
    """verify v nodes number, after applying the production"""
    ProductionP9(prepare_graph_positive).apply()
    expected_v_nodes_number = 11
    assert (
        len([s for s in prepare_graph_positive.nodes() if "v" in s])
        == expected_v_nodes_number
    )


def test_positive_p09_q_nodes_number_after_production(prepare_graph_positive: nx.Graph):
    """verify g nodes number, after applying the production"""
    ProductionP9(prepare_graph_positive).apply()
    expected_q_nodes_number = 5
    assert (
        len([s for s in prepare_graph_positive.nodes() if "Q" in s])
        == expected_q_nodes_number
    )


def test_positive_p09_q_nodes_inactive_after_production_after_production(
    prepare_graph_positive: nx.Graph,
):
    """verify Q nodes R==0, after applying the production"""
    ProductionP9(prepare_graph_positive).apply()
    q_nodes = [s for s in prepare_graph_positive.nodes() if "Q" in s]
    assert all(
        q_r == 0
        for q_r in [prepare_graph_positive.nodes()[q_r0]["R"] for q_r0 in q_nodes]
    )


def test_positive_p09_h_nodes_number_before_production(
    prepare_graph_positive: nx.Graph,
):
    """verify h nodes number, before apply production"""
    expected_h_nodes_number = 0
    h_nodes = [
        (v)
        for v, data in prepare_graph_positive.nodes(data=True)
        if data["label"] != "P" and data["h"] == 1
    ]
    assert len(h_nodes) == expected_h_nodes_number


def test_positive_p09_h_nodes_number_after_production(prepare_graph_positive: nx.Graph):
    """verify h nodes number, after applying production"""
    ProductionP9(prepare_graph_positive).apply()
    expected_h_nodes_number = 0
    h_nodes = [
        (v)
        for v, data in prepare_graph_positive.nodes(data=True)
        if data["label"] != "Q" and data["h"] == 1
    ]
    assert len(h_nodes) == expected_h_nodes_number


def test_positive_p09_edges_number_after_production(prepare_graph_positive: nx.Graph):
    """verify edges number, after applying the production"""
    ProductionP9(prepare_graph_positive).apply()
    expected_edges_number = 35
    assert len(prepare_graph_positive.edges()) == expected_edges_number


def test_boundary_edges_before_production(prepare_graph_positive: nx.Graph):
    """verify boundary edges number, before applying the production"""
    boundary_edges = [
        (u, v, data)
        for u, v, data in prepare_graph_positive.edges(data=True)
        if u.find("P") == -1 and v.find("P") == -1 and data["B"] == 1
    ]
    expected_boundary_edges_number = 5
    assert len(boundary_edges) == expected_boundary_edges_number


def test_boundary_edges_after_production(prepare_graph_positive: nx.Graph):
    """verify boundary edges number after applying the production"""
    ProductionP9(prepare_graph_positive).apply()
    boundary_edges = [
        (u, v)
        for u, v, data in prepare_graph_positive.edges(data=True)
        if u.find("Q") == -1 and v.find("Q") == -1 and data["B"] == 1
    ]
    assert all(prepare_graph_positive.edges[u, v]["B"] == 1 for u, v in boundary_edges)


def test_inner_edges_before_production(prepare_graph_positive: nx.Graph):
    """verify inner edges number before applying the production"""
    inner_edges = [
        (u, v)
        for u, v, data in prepare_graph_positive.edges(data=True)
        if u.find("P") == -1 and v.find("P") == -1 and data["B"] == 0
    ]
    assert len(inner_edges) == 0


def test_inner_edges_after_production(prepare_graph_positive: nx.Graph):
    """verify inner edges number after applying the production"""
    ProductionP9(prepare_graph_positive).apply()
    inner_edges = [
        (u, v)
        for u, v, data in prepare_graph_positive.edges(data=True)
        if u.find("Q") == -1 and v.find("Q") == -1 and data["B"] == 0
    ]
    assert len(inner_edges) > 0
    assert all(prepare_graph_positive.edges[u, v]["B"] == 0 for u, v in inner_edges)


def test_negative_p09_check(prepare_graph_negative: nx.Graph):
    """check is None if the graph is not valid"""
    assert ProductionP9(prepare_graph_negative).check is None


def test_negative_p09_apply(prepare_graph_negative: nx.Graph):
    """apply creates new node in graph due to the graph is invalid"""
    ProductionP9(prepare_graph_negative).apply()
    assert "P" not in prepare_graph_negative


def test_negative_p09_hanging_check(prepare_graph_positive_hanging: nx.Graph):
    """check is None if the graph is not valid"""
    assert ProductionP9(prepare_graph_positive_hanging).check is None


def test_negative_p09_hanging_apply(prepare_graph_positive_hanging: nx.Graph):
    """apply creates new node in graph due to the graph is invalid"""
    ProductionP9(prepare_graph_positive_hanging).apply()
    assert "P" not in prepare_graph_positive_hanging


def prepare_valid_test_graph() -> nx.Graph:
    """Prepares the basic 5-nodes and one P-node graph"""
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


def prepare_valid_test_graph_with_hanging_node() -> nx.Graph:
    """Prepares the basic 5-nodes and one P-node graph"""
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
    return G


def prepare_corrupted_test_graph() -> nx.Graph:
    """Prepares the basic 5-nodes graph"""
    G = nx.Graph()
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


def prepare_valid_bigger_graph():
    G = nx.Graph()
    G.add_node("P:5.0:5.0", label="P", R=1)
    G.add_nodes_from(
        [
            ("v:0.0:0.0", {"label": "v", "x": 0.0, "y": 0.0, "h": 0}),
            ("v:10.0:0.0", {"label": "v", "x": 10.0, "y": 0.0, "h": 0}),
            ("v:10.0:10.0", {"label": "v", "x": 10.0, "y": 10.0, "h": 0}),
            ("v:0.0:10.0", {"label": "v", "x": 0.0, "y": 10.0, "h": 0}),
            ("v:15.0:5.0", {"label": "v", "x": 15.0, "y": 5.0, "h": 0}),
            ("v:0.0:15.0", {"label": "v", "x": 0.0, "y": 15.0, "h": 0}),
            ("v:0.0:-5.0", {"label": "v", "x": 0.0, "y": -5.0, "h": 0}),
            ("v:-5.0:0.0", {"label": "v", "x": -5.0, "y": 0.0, "h": 0}),
            ("v:-5.0:10.0", {"label": "v", "x": -5.0, "y": 10.0, "h": 0}),
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
            # a
            ("v:-5.0:10.0", "v:0.0:10.0"),
            ("v:0.0:15.0", "v:10.0:10.0"),
            ("v:0.0:15.0", "v:-5.0:10.0"),
            ("v:-5.0:0.0", "v:-5.0:10.0"),
            ("v:-5.0:0.0", "v:0.0:0.0"),
            ("v:-5.0:0.0", "v:0.0:-5.0"),
            ("v:10.0:0.0", "v:0.0:-5.0"),
        ]
    )
    return G
