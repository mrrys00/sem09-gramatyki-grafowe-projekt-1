import pytest
import networkx as nx

from pytest import FixtureRequest

from productions.p07.production07 import ProductionP7
from productions.utils import (
    prepare_graph_with_R0_quadrilateral,
    prepare_graph_without_R0_quadrilateral,
)

@pytest.fixture(scope='function')
def prepare_graph_positive_p7(request: FixtureRequest):
    """Prepare a valid graph for testing Production P7."""
    G = prepare_graph_with_R0_quadrilateral()
    yield G

@pytest.fixture(scope='function')
def prepare_graph_negative_p7(request: FixtureRequest):
    """Prepare an invalid graph for testing Production P7."""
    G = prepare_graph_without_R0_quadrilateral()
    yield G

def test_positive_p07_check(prepare_graph_positive_p7: nx.Graph):
    """Check is not None if the graph is valid for P7."""
    production = ProductionP7(prepare_graph_positive_p7)
    assert production.check is not None

def test_positive_p07_apply(prepare_graph_positive_p7: nx.Graph):
    """Apply P7 on a valid graph and verify that R is updated."""
    production = ProductionP7(prepare_graph_positive_p7)
    q_node = production.check
    assert q_node is not None

    initial_R = prepare_graph_positive_p7.nodes[q_node]['R']
    production.apply()

    new_R = prepare_graph_positive_p7.nodes[q_node]['R']
    assert new_R == 1
    assert new_R != initial_R

def test_p7_check_returns_node():
    """Test that the check method returns a node when R == 0 quadrilateral exists."""
    G = prepare_graph_with_R0_quadrilateral()
    production = ProductionP7(G)
    assert production.check is not None
    assert production.check == 'Q1'

def test_p7_apply_marks_quadrilateral():
    """Test that apply method sets R = 1 for the quadrilateral with R == 0."""
    G = prepare_graph_with_R0_quadrilateral()
    production = ProductionP7(G)
    q_node = production.check
    assert q_node is not None
    initial_R = G.nodes[q_node]['R']
    production.apply()
    new_R = G.nodes[q_node]['R']
    assert new_R == 1
    assert new_R != initial_R

def test_p7_check_returns_none():
    """Test that the check method returns None when no R == 0 quadrilateral exists."""
    G = prepare_graph_without_R0_quadrilateral()
    production = ProductionP7(G)
    assert production.check is None

def test_p7_apply_does_nothing():
    """Test that apply method does nothing when no R == 0 quadrilateral exists."""
    G = prepare_graph_without_R0_quadrilateral()
    production = ProductionP7(G)
    initial_R_values = {
        n: data['R']
        for n, data in G.nodes(data=True)
        if data.get('label') == 'Q'
    }
    production.apply()
    final_R_values = {
        n: data['R']
        for n, data in G.nodes(data=True)
        if data.get('label') == 'Q'
    }
    assert initial_R_values == final_R_values

def test_p7_does_not_affect_other_nodes():
    """Test that apply method does not affect other quadrilateral nodes."""
    G = prepare_graph_with_R0_quadrilateral()
    # Add another quadrilateral with R = 2
    G.add_node('Q2', label='Q', R=2)
    G.add_nodes_from([
        ('v4', {'label': 'v', 'x': 2, 'y': 0}),
        ('v5', {'label': 'v', 'x': 2, 'y': 1})
    ])
    G.add_edges_from([
        ('Q2', 'v1'),
        ('Q2', 'v2'),
        ('Q2', 'v4'),
        ('Q2', 'v5'),
        ('v1', 'v4'),
        ('v4', 'v5'),
        ('v5', 'v2'),
        ('v2', 'v1')
    ])
    production = ProductionP7(G)
    q_node = production.check
    assert q_node == 'Q1'
    initial_R_Q2 = G.nodes['Q2']['R']
    production.apply()
    # Ensure that Q2's R value has not changed
    assert G.nodes['Q2']['R'] == initial_R_Q2

def test_p7_no_new_nodes_or_edges():
    """Test that apply method does not add new nodes or edges."""
    G = prepare_graph_with_R0_quadrilateral()
    initial_node_count = G.number_of_nodes()
    initial_edge_count = G.number_of_edges()
    production = ProductionP7(G)
    production.apply()
    final_node_count = G.number_of_nodes()
    final_edge_count = G.number_of_edges()
    assert initial_node_count == final_node_count
    assert initial_edge_count == final_edge_count
