import pytest
import networkx as nx

from pytest import FixtureRequest

from productions.p03.production03 import ProductionP3
from productions.utils import prepare_valid_test_graph, prepare_corrupted_test_graph, prepare_invalid_test_graph_with_hanging_node_p34_test, prepare_valid_test_graph_with_hanging_node_p3, prepare_valid_test_graph_with_hanging_node_p3_test1, prepare_valid_test_graph_with_hanging_node_p3_test2

G = prepare_valid_test_graph()
G_h = prepare_valid_test_graph_with_hanging_node_p3()
G_n= prepare_corrupted_test_graph()
G_t1 = prepare_valid_test_graph_with_hanging_node_p3_test1()
G_t2 = prepare_valid_test_graph_with_hanging_node_p3_test2()
G_h2 = prepare_invalid_test_graph_with_hanging_node_p34_test()

@pytest.fixture(scope='function', params=[G])
def prepare_graph_positive(request: type[FixtureRequest]):
    yield request.param

@pytest.fixture(scope='function', params=[G_h])
def prepare_graph_positive_hanging(request: type[FixtureRequest]):
    yield request.param

@pytest.fixture(scope='function', params=[G_n])
def prepare_graph_negative(request: type[FixtureRequest]):
    yield request.param

@pytest.fixture(scope='function', params=[G_t1])
def prepare_graph_with_two_G3(request: type[FixtureRequest]):
    yield request.param

@pytest.fixture(scope='function', params=[G_t2])
def prepare_graph_with_two_G3_and_two_squares(request: type[FixtureRequest]):
    yield request.param

@pytest.fixture(scope='function', params=[G_h2])
def prepare_graph_negative_hanging_corner(request: type[FixtureRequest]):
    yield request.param

def test_positive_p03_check(prepare_graph_positive: nx.Graph):
    """check is not None if the graph is valid"""
    assert ProductionP3(prepare_graph_positive).check is None

#TODO write more tests

def test_negative_p03_check(prepare_graph_negative: nx.Graph):
    """check is None if the graph is not valid"""
    assert ProductionP3(prepare_graph_negative).check is None

def test_negative_p03_apply(prepare_graph_negative: nx.Graph):
    """apply creates new node in graph due to the graph is invalid"""
    ProductionP3(prepare_graph_negative).apply()
    assert 'Q' not in prepare_graph_negative

def test_positive_p03_nodes_number_after_production(prepare_graph_positive_hanging: nx.Graph):
    """apply creates new node in graph, verify nodes number"""
    ProductionP3(prepare_graph_positive_hanging).apply()
    expected_nodes_number = 13
    assert len(prepare_graph_positive_hanging.nodes()) == expected_nodes_number

def test_positive_p03_v_nodes_number_after_production(prepare_graph_positive_hanging: nx.Graph):
    """apply creates new node in graph, verify v nodes number"""
    ProductionP3(prepare_graph_positive_hanging).apply()
    expected_v_nodes_number = 9
    assert len([s for s in prepare_graph_positive_hanging.nodes() if 'v' in s]) == expected_v_nodes_number


def test_positive_p03_q_nodes_number_after_production(prepare_graph_positive_hanging: nx.Graph):
    """apply creates new node in graph, verify g nodes number"""
    ProductionP3(prepare_graph_positive_hanging).apply()
    expected_q_nodes_number = 4
    assert len([s for s in prepare_graph_positive_hanging.nodes() if 'Q' in s]) == expected_q_nodes_number

def test_positive_p03_q_nodes_inactive_after_production_after_production(prepare_graph_positive_hanging: nx.Graph):
    """apply creates new node in graph, verify Q nodes R==0 after production"""
    ProductionP3(prepare_graph_positive_hanging).apply()
    q_nodes = [s for s in prepare_graph_positive_hanging.nodes() if 'Q' in s]
    assert all(q_r == 0 for q_r in
               [prepare_graph_positive_hanging.nodes()[q_r0]['R'] for q_r0 in q_nodes])

def test_positive_p03_h_nodes_number_after_production(prepare_graph_positive_hanging: nx.Graph):
    """verify h nodes number, after applying production"""
    ProductionP3(prepare_graph_positive_hanging).apply()
    expected_h_nodes_number = 0
    h_nodes = [(v) for v,data in prepare_graph_positive_hanging.nodes(data=True)
               if data['label'] != 'Q' and data['h'] == 1]
    assert len(h_nodes) == expected_h_nodes_number

def test_positive_p02_edges_number_after_production(prepare_graph_positive_hanging: nx.Graph):
    """apply creates new node in graph, verify edges number"""
    ProductionP3(prepare_graph_positive_hanging).apply()
    expected_edges_number = 28
    assert len(prepare_graph_positive_hanging.edges()) == expected_edges_number


def test_boundary_edges_after_production(prepare_graph_positive_hanging: nx.Graph):
    """verify boundary edges number after applying the production"""
    ProductionP3(prepare_graph_positive_hanging).apply()
    boundary_edges = [(u, v) for u, v, data in prepare_graph_positive_hanging.edges(data=True)
                      if u.find('Q') == -1 and v.find('Q') == -1 and data['B'] == 1]
    assert all(prepare_graph_positive_hanging.edges[u, v]['B'] == 1 for u, v in boundary_edges)

def test_inner_edges_after_production(prepare_graph_positive_hanging: nx.Graph):
    """verify inner edges number after applying the production"""
    ProductionP3(prepare_graph_positive_hanging).apply()
    inner_edges = [(u, v) for u, v, data in prepare_graph_positive_hanging.edges(data=True)
                   if u.find('Q') == -1 and v.find('Q') == -1 and data['B'] == 0]
    assert len(inner_edges) > 0
    assert all(prepare_graph_positive_hanging.edges[u, v]['B'] == 0 for u, v in inner_edges)


def test_negative_p03_check(prepare_graph_negative: nx.Graph):
    """check is None if the graph is not valid"""
    assert ProductionP3(prepare_graph_negative).check is None


def test_negative_p03_apply(prepare_graph_negative: nx.Graph):
    """apply creates new node in graph due to the graph is invalid"""
    ProductionP3(prepare_graph_negative).apply()
    assert 'Q' not in prepare_graph_negative

def test_test1_graph(prepare_graph_with_two_G3: nx.Graph):
    prod3 = ProductionP3(prepare_graph_with_two_G3)

    expected_h_nodes_number = 4
    h_nodes = [(v) for v,data in prepare_graph_with_two_G3.nodes(data=True)
               if data['label'] != 'Q' and data['h'] == 1]
    assert len(h_nodes) == expected_h_nodes_number
    
    prod3.apply()
    prod3.apply()
    
    expected_q_nodes_number = 5
    q_nodes = [s for s in prepare_graph_with_two_G3.nodes() if 'Q' in s]

    assert len(q_nodes) == expected_q_nodes_number

    expected_v_nodes_number = 15
    assert len([s for s in prepare_graph_with_two_G3.nodes() if 'v' in s]) == expected_v_nodes_number

def test_test2_graph(prepare_graph_with_two_G3_and_two_squares: nx.Graph):
    prod3 = ProductionP3(prepare_graph_with_two_G3_and_two_squares)

    expected_h_nodes_number = 8
    h_nodes = [(v) for v,data in prepare_graph_with_two_G3_and_two_squares.nodes(data=True)
               if data['label'] != 'Q' and data['h'] == 1]
    assert len(h_nodes) == expected_h_nodes_number

    prod3.apply()   
    
    expected_q_nodes_number = 2
    q_nodes = [s for s in prepare_graph_with_two_G3_and_two_squares.nodes() if 'Q' in s]

    assert len(q_nodes) == expected_q_nodes_number

    expected_v_nodes_number = 21
    assert len([s for s in prepare_graph_with_two_G3_and_two_squares.nodes() if 'v' in s]) == expected_v_nodes_number

def test_negative_p04_apply_with_hanging_node_in_corner(prepare_graph_negative_hanging_corner: nx.Graph):
    """should not apply production for hanging node in the corner"""
    assert ProductionP3(prepare_graph_negative_hanging_corner).check is None
    ProductionP3(prepare_graph_negative_hanging_corner).apply()
    assert 'Q' not in prepare_graph_negative_hanging_corner
    start_number_of_nodes = 29
    assert len(prepare_graph_negative_hanging_corner.nodes) == start_number_of_nodes
