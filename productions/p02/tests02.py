import pytest
import networkx as nx

from pytest import FixtureRequest

from productions.p02.production02 import ProductionP2
from productions.utils import prepare_valid_test_graph, prepare_corrupted_test_graph, \
    prepare_valid_test_graph_with_hanging_node

G = prepare_valid_test_graph()
G_h = prepare_valid_test_graph_with_hanging_node()
G_n = prepare_corrupted_test_graph()


@pytest.fixture(scope='function', params=[G])
def prepare_graph_positive(request: type[FixtureRequest]):
    request.param.nodes['v1']['h'] = 1
    yield request.param


@pytest.fixture(scope='function', params=[G_h])
def prepare_graph_positive_hanging(request: type[FixtureRequest]):
    yield request.param


@pytest.fixture(scope='function', params=[G_n])
def prepare_graph_negative(request: type[FixtureRequest]):
    yield request.param


def test_positive_p02_check_without_hanging_node(prepare_graph_positive: nx.Graph):
    """check is not None if the graph is valid"""
    assert ProductionP2(prepare_graph_positive).check is None


def test_positive_p02_check(prepare_graph_positive_hanging: nx.Graph):
    """check is not None if the graph is valid"""
    assert ProductionP2(prepare_graph_positive_hanging).check is not None


def test_positive_p02_apply_check(prepare_graph_positive_hanging: nx.Graph):
    """check is None after apply the production1"""
    G = prepare_graph_positive_hanging
    ProductionP2(prepare_graph_positive_hanging).apply()
    assert ProductionP2(prepare_graph_positive_hanging).check is None


def test_positive_p02_apply_nodes_number(prepare_graph_positive_hanging: nx.Graph):
    """apply creates new node in graph, verify nodes number"""
    ProductionP2(prepare_graph_positive_hanging).apply()
    expected_nodes_number = 13
    assert len(prepare_graph_positive_hanging.nodes()) == expected_nodes_number


def test_positive_p02_apply_v_nodes_number(prepare_graph_positive_hanging: nx.Graph):
    """apply creates new node in graph, verify v nodes number"""
    ProductionP2(prepare_graph_positive_hanging).apply()
    expected_v_nodes_number = 9
    assert len([s for s in prepare_graph_positive_hanging.nodes() if 'v' in s]) == expected_v_nodes_number


def test_positive_p02_apply_q_nodes_number(prepare_graph_positive_hanging: nx.Graph):
    """apply creates new node in graph, verify g nodes number"""
    ProductionP2(prepare_graph_positive_hanging).apply()
    expected_q_nodes_number = 4
    assert len([s for s in prepare_graph_positive_hanging.nodes() if 'Q' in s]) == expected_q_nodes_number


def test_positive_p02_apply_q_nodes_inactive_after_production(prepare_graph_positive_hanging: nx.Graph):
    """apply creates new node in graph, verify Q nodes R==0 after production"""
    ProductionP2(prepare_graph_positive_hanging).apply()
    q_nodes = [s for s in prepare_graph_positive_hanging.nodes() if 'Q' in s]
    assert all(q_r == 0 for q_r in
               [prepare_graph_positive_hanging.nodes()[q_r0]['R'] for q_r0 in q_nodes])


def test_positive_p02_apply_edges_number(prepare_graph_positive_hanging: nx.Graph):
    """apply creates new node in graph, verify edges number"""
    ProductionP2(prepare_graph_positive_hanging).apply()
    expected_edges_number = 28
    assert len(prepare_graph_positive_hanging.edges()) == expected_edges_number


def test_negative_p02_check(prepare_graph_negative: nx.Graph):
    """check is None if the graph is not valid"""
    assert ProductionP2(prepare_graph_negative).check is None


def test_negative_p02_apply(prepare_graph_negative: nx.Graph):
    """apply creates new node in graph due to the graph is invalid"""
    ProductionP2(prepare_graph_negative).apply()
    assert 'Q' not in prepare_graph_negative
