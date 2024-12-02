import pytest
import networkx as nx
from networkx.algorithms.isomorphism import GraphMatcher

from productions.p08.production08 import ProductionP8
from productions.utils import (
    prepare_valid_test_graph_for_prod_8_initial,
    prepare_valid_test_graph_for_prod_8_after_modification, prepare_non_valid_test_graph_for_prod_8_initial,
)

@pytest.fixture(scope="function")
def initial_graph_p8():
    """Fixture providing the initial valid graph for Production P8."""
    return prepare_valid_test_graph_for_prod_8_initial()

@pytest.fixture(scope="function")
def expected_graph_p8():
    """Fixture providing the expected graph after Production P8."""
    return prepare_valid_test_graph_for_prod_8_after_modification()


def test_p8_graph_isomorphism_with_left_side(initial_graph_p8: nx.Graph):
    """
    Verify if the initial graph is isomorphic to the left side of Production P8.
    """
    left_side_graph = prepare_valid_test_graph_for_prod_8_initial()
    matcher = GraphMatcher(initial_graph_p8, left_side_graph)
    assert matcher.is_isomorphic(), "Graph is not isomorphic to the left side of Production P8."


def test_p8_apply_changes_R_value(initial_graph_p8: nx.Graph, expected_graph_p8: nx.Graph):
    """
    Verify if applying Production P8 changes the R value of the quadrilateral.
    """
    production = ProductionP8(initial_graph_p8)
    production.apply()

    for node, data in expected_graph_p8.nodes(data=True):
        if data.get("label") == "Q":
            assert initial_graph_p8.nodes[node]["R"] == data["R"], f"Node {node} R value is incorrect after production."


def test_p8_isomorphism_after_production(initial_graph_p8: nx.Graph, expected_graph_p8: nx.Graph):
    """
    Verify if the resulting graph after applying Production P8 matches the expected graph.
    """
    production = ProductionP8(initial_graph_p8)
    production.apply()

    matcher = GraphMatcher(initial_graph_p8, expected_graph_p8)
    assert matcher.is_isomorphic(), "Graph after production is not isomorphic to the expected graph."


def test_p8_no_extra_nodes_or_edges(initial_graph_p8: nx.Graph):
    """
    Ensure no additional nodes or edges are added during the production.
    """
    production = ProductionP8(initial_graph_p8)
    initial_node_count = initial_graph_p8.number_of_nodes()
    initial_edge_count = initial_graph_p8.number_of_edges()

    production.apply()

    assert initial_graph_p8.number_of_nodes() == initial_node_count, "Number of nodes has changed after production."
    assert initial_graph_p8.number_of_edges() == initial_edge_count, "Number of edges has changed after production."


def test_p8_multiple_apply_no_change(initial_graph_p8: nx.Graph):
    """
    Ensure that applying Production P8 multiple times does not change the graph further.
    """
    production = ProductionP8(initial_graph_p8)
    production.apply()

    initial_state_after_first_apply = nx.to_dict_of_dicts(initial_graph_p8)

    production.apply()

    state_after_second_apply = nx.to_dict_of_dicts(initial_graph_p8)

    assert initial_state_after_first_apply == state_after_second_apply, "Graph changed after a second apply."


def test_p8_initial_to_expected(initial_graph_p8: nx.Graph, expected_graph_p8: nx.Graph):
    """
    Verify that applying Production P8 transforms the initial graph into the expected graph.
    """
    production = ProductionP8(initial_graph_p8)
    production.apply()

    # Compare nodes and their attributes
    nodes_diff = []
    for node, data in initial_graph_p8.nodes(data=True):
        expected_data = expected_graph_p8.nodes.get(node, None)
        if data != expected_data:
            nodes_diff.append((node, data, expected_data))

    # Compare edges and their attributes
    edges_diff = []
    for u, v, data in initial_graph_p8.edges(data=True):
        expected_data = expected_graph_p8.get_edge_data(u, v, default=None)
        if data != expected_data:
            edges_diff.append(((u, v), data, expected_data))

    assert not nodes_diff, f"Node differences found: {nodes_diff}"
    assert not edges_diff, f"Edge differences found: {edges_diff}"




def test_p8_Q_changes_R_value(initial_graph_p8: nx.Graph):
    """
    Verify that the value of R for the Q node changes from 0 to 1 after applying Production P8.
    """
    production = ProductionP8(initial_graph_p8)
    result = production.check
    assert result is not None, "No valid Q node found to apply the production."

    q_node, _ = result

    assert initial_graph_p8.nodes[q_node]["R"] == 0, f"Initial R value of node {q_node} is not 0."

    production.apply()

    assert initial_graph_p8.nodes[q_node]["R"] == 1, f"R value of node {q_node} did not change to 1 after apply."

def test_p8_no_propagation_when_both_Q_have_R_0():
    """
    Verify that Production P8 does not propagate changes when both Q nodes have R=0.
    """

    # Prepare the invalid graph
    invalid_graph = prepare_non_valid_test_graph_for_prod_8_initial()
    production = ProductionP8(invalid_graph)

    # Capture the initial state of the graph
    initial_state = nx.to_dict_of_dicts(invalid_graph)

    # Apply the production
    production.apply()

    # Capture the state of the graph after applying the production
    final_state = nx.to_dict_of_dicts(invalid_graph)

    # Ensure the graph state remains unchanged
    assert initial_state == final_state, "Graph state should not change when both Q nodes have R=0."

