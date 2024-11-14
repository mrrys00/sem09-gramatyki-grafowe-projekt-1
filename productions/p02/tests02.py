import pytest
import networkx as nx

from pytest import FixtureRequest

from productions.p02.production02 import ProductionP2
from productions.utils import prepare_valid_test_graph, prepare_corrupted_test_graph


G = prepare_valid_test_graph()
G_n= prepare_corrupted_test_graph()

@pytest.fixture(scope="function", params=[G])
def prepare_graph_positive(request: type[FixtureRequest]):
    request.param.nodes["v1"]["h"] = 1
    yield request.param

@pytest.fixture(scope="function", params=[G_n])
def prepare_graph_negative(request: type[FixtureRequest]):
    yield request.param


def test_positive_p01_check(prepare_graph_positive: nx.Graph):
    """check is not None if the graph is valid"""
    assert ProductionP2(prepare_graph_positive).check() is not None

def test_positive_p01_apply(prepare_graph_positive: nx.Graph):
    """apply creates new node in graph"""
    ProductionP2(prepare_graph_positive).apply()
    assert "Q2" in prepare_graph_positive

def test_negative_p01_check(prepare_graph_negative: nx.Graph):
    """check is None if the graph is not valid"""
    assert ProductionP2(prepare_graph_negative).check() is None

def test_negative_p01_apply(prepare_graph_negative: nx.Graph):
    """apply creates new node in graph due to the graph is invalid"""
    ProductionP2(prepare_graph_negative).apply()
    assert "Q2" not in prepare_graph_negative
