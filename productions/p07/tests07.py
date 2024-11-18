import pytest
import networkx as nx

from pytest import FixtureRequest

from productions.p07.production07 import ProductionP7
from productions.utils import prepare_valid_test_graph, prepare_corrupted_test_graph, prepare_valid_test_graph_with_hanging_node


G = prepare_valid_test_graph()
G_h = prepare_valid_test_graph_with_hanging_node()
G_n= prepare_corrupted_test_graph()

@pytest.fixture(scope='function', params=[G])
def prepare_graph_positive(request: type[FixtureRequest]):
    yield request.param

@pytest.fixture(scope='function', params=[G_h])
def prepare_graph_positive_hanging(request: type[FixtureRequest]):
    yield request.param

@pytest.fixture(scope='function', params=[G_n])
def prepare_graph_negative(request: type[FixtureRequest]):
    yield request.param


def test_positive_p07_check(prepare_graph_positive: nx.Graph):
    """check is not None if the graph is valid"""
    assert ProductionP7(prepare_graph_positive).check is not None

#TODO write more tests

def test_negative_p07_check(prepare_graph_negative: nx.Graph):
    """check is None if the graph is not valid"""
    assert ProductionP7(prepare_graph_negative).check is None

def test_negative_p07_apply(prepare_graph_negative: nx.Graph):
    """apply creates new node in graph due to the graph is invalid"""
    ProductionP7(prepare_graph_negative).apply()
    assert 'Q' not in prepare_graph_negative
