import networkx as nx
import pytest

from productions.p01.production01 import ProductionP1
from productions.utils import prepare_valid_test_graph, prepare_corrupted_test_graph


@pytest.fixture(scope='function')
def prepare_graph_positive():
    yield prepare_valid_test_graph()


@pytest.fixture(scope='function')
def prepare_graph_negative():
    yield prepare_corrupted_test_graph()


def test_positive_p01_check(prepare_graph_positive: nx.Graph):
    """check is not None if the graph is valid"""
    assert ProductionP1(prepare_graph_positive).check is not None


def test_positive_p01_check_after_production(prepare_graph_positive: nx.Graph):
    """check is None, after applying the production"""
    ProductionP1(prepare_graph_positive).apply()
    assert ProductionP1(prepare_graph_positive).check is None


def test_positive_p01_nodes_number_after_production(prepare_graph_positive: nx.Graph):
    """verify nodes number, after applying the production"""
    ProductionP1(prepare_graph_positive).apply()
    expected_nodes_number = 13
    assert len(prepare_graph_positive.nodes()) == expected_nodes_number


def test_positive_p01_v_nodes_number_after_production(prepare_graph_positive: nx.Graph):
    """verify v nodes number, after applying the production"""
    ProductionP1(prepare_graph_positive).apply()
    expected_v_nodes_number = 9
    assert len([s for s in prepare_graph_positive.nodes() if 'v' in s]) == expected_v_nodes_number


def test_positive_p01_q_nodes_number_after_production(prepare_graph_positive: nx.Graph):
    """verify g nodes number, after applying the production"""
    ProductionP1(prepare_graph_positive).apply()
    expected_q_nodes_number = 4
    assert len([s for s in prepare_graph_positive.nodes() if 'Q' in s]) == expected_q_nodes_number


def test_positive_p01_q_nodes_inactive_after_production_after_production(prepare_graph_positive: nx.Graph):
    """verify Q nodes R==0, after applying the production"""
    ProductionP1(prepare_graph_positive).apply()
    q_nodes = [s for s in prepare_graph_positive.nodes() if 'Q' in s]
    assert all(q_r == 0 for q_r in
               [prepare_graph_positive.nodes()[q_r0]['R'] for q_r0 in q_nodes])


def test_positive_p01_h_nodes_number_before_production(prepare_graph_positive: nx.Graph):
    """verify h nodes number, before apply production"""
    expected_h_nodes_number = 0
    h_nodes = [(v) for v,data in prepare_graph_positive.nodes(data=True)
               if data['label'] != 'Q' and data['h'] == 1]
    assert len(h_nodes) == expected_h_nodes_number


def test_positive_p01_h_nodes_number_after_production(prepare_graph_positive: nx.Graph):
    """verify h nodes number, after applying production"""
    ProductionP1(prepare_graph_positive).apply()
    expected_h_nodes_number = 0
    h_nodes = [(v) for v,data in prepare_graph_positive.nodes(data=True)
               if data['label'] != 'Q' and data['h'] == 1]
    assert len(h_nodes) == expected_h_nodes_number


def test_positive_p01_edges_number_after_production(prepare_graph_positive: nx.Graph):
    """verify edges number, after applying the production"""
    ProductionP1(prepare_graph_positive).apply()
    expected_edges_number = 28
    assert len(prepare_graph_positive.edges()) == expected_edges_number


def test_boundary_edges_before_production(prepare_graph_positive: nx.Graph):
    """verify boundary edges number, before applying the production"""
    boundary_edges = [(u, v, data) for u, v, data in prepare_graph_positive.edges(data=True)
                      if u.find('Q') == -1 and v.find('Q') == -1 and data['B'] == 1]
    expected_boundary_edges_number = 4
    assert len(boundary_edges) == expected_boundary_edges_number


def test_boundary_edges_after_production(prepare_graph_positive: nx.Graph):
    """verify boundary edges number after applying the production"""
    ProductionP1(prepare_graph_positive).apply()
    boundary_edges = [(u, v) for u, v, data in prepare_graph_positive.edges(data=True)
                      if u.find('Q') == -1 and v.find('Q') == -1 and data['B'] == 1]
    assert all(prepare_graph_positive.edges[u, v]['B'] == 1 for u, v in boundary_edges)


def test_inner_edges_before_production(prepare_graph_positive: nx.Graph):
    """verify inner edges number before applying the production"""
    inner_edges = [(u, v) for u, v, data in prepare_graph_positive.edges(data=True)
                   if u.find('Q') == -1 and v.find('Q') == -1 and data['B'] == 0]
    assert len(inner_edges) == 0


def test_inner_edges_after_production(prepare_graph_positive: nx.Graph):
    """verify inner edges number after applying the production"""
    ProductionP1(prepare_graph_positive).apply()
    inner_edges = [(u, v) for u, v, data in prepare_graph_positive.edges(data=True)
                   if u.find('Q') == -1 and v.find('Q') == -1 and data['B'] == 0]
    assert len(inner_edges) > 0
    assert all(prepare_graph_positive.edges[u, v]['B'] == 0 for u, v in inner_edges)


def test_negative_p01_check(prepare_graph_negative: nx.Graph):
    """check is None if the graph is not valid"""
    assert ProductionP1(prepare_graph_negative).check is None


def test_negative_p01_after_production(prepare_graph_negative: nx.Graph):
    """apply creates new node in graph due to the graph is invalid"""
    ProductionP1(prepare_graph_negative).apply()
    assert 'Q' not in prepare_graph_negative
