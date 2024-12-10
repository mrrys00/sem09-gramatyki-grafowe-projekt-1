import pytest
import networkx as nx
from networkx.algorithms.isomorphism import GraphMatcher

from productions.p17.production17 import ProductionP17
from productions.utils import (
    prepare_valid_test_graph_for_prod_17_initial,
    prepare_non_valid_test_graph_for_prod_17_initial,
    prepare_valid_test_graph_for_prod_17_after_modification,
)


@pytest.fixture(scope="function")
def initial_graph_p17():
    """Fixture providing the initial valid graph for Production P17."""
    return prepare_valid_test_graph_for_prod_17_initial()


@pytest.fixture(scope="function")
def non_valid_graph_p17():
    """Fixture providing an invalid graph for Production P17."""
    return prepare_non_valid_test_graph_for_prod_17_initial()


@pytest.fixture(scope="function")
def expected_graph_p17():
    """Fixture providing the expected graph after Production P17."""
    return prepare_valid_test_graph_for_prod_17_after_modification()


def test_p17_graph_isomorphism_with_left_side(initial_graph_p17: nx.Graph):
    """
    Verify if the initial graph is isomorphic to the left side of Production P17.
    """
    left_side_graph = prepare_valid_test_graph_for_prod_17_initial()
    matcher = GraphMatcher(initial_graph_p17, left_side_graph)
    assert matcher.is_isomorphic(), "Graph is not isomorphic to the left side of Production P17."


def test_p17_apply_changes_R_value(initial_graph_p17: nx.Graph, expected_graph_p17: nx.Graph):
    """
    Verify if applying Production P17 changes the R value of the pentagon.
    """
    production = ProductionP17(initial_graph_p17)
    production.apply()

    for node, data in expected_graph_p17.nodes(data=True):
        if data.get("label") == "P":  # Pentagons are marked during the production
            assert initial_graph_p17.nodes[node]["R"] == data["R"], f"Node {node} R value is incorrect after production."


def test_p17_isomorphism_after_production(initial_graph_p17: nx.Graph, expected_graph_p17: nx.Graph):
    """
    Verify if the resulting graph after applying Production P17 matches the expected graph.
    """
    production = ProductionP17(initial_graph_p17)
    production.apply()

    matcher = GraphMatcher(initial_graph_p17, expected_graph_p17)
    assert matcher.is_isomorphic(), "Graph after production is not isomorphic to the expected graph."


def test_p17_no_extra_nodes_or_edges(initial_graph_p17: nx.Graph):
    """
    Ensure no additional nodes or edges are added during the production.
    """
    production = ProductionP17(initial_graph_p17)
    initial_node_count = initial_graph_p17.number_of_nodes()
    initial_edge_count = initial_graph_p17.number_of_edges()

    production.apply()

    assert initial_graph_p17.number_of_nodes() == initial_node_count, "Number of nodes has changed after production."
    assert initial_graph_p17.number_of_edges() == initial_edge_count, "Number of edges has changed after production."


def test_p17_multiple_apply_no_change(initial_graph_p17: nx.Graph):
    """
    Ensure that applying Production P17 multiple times does not change the graph further.
    """
    production = ProductionP17(initial_graph_p17)
    production.apply()

    initial_state_after_first_apply = nx.to_dict_of_dicts(initial_graph_p17)

    production.apply()

    state_after_second_apply = nx.to_dict_of_dicts(initial_graph_p17)

    assert initial_state_after_first_apply == state_after_second_apply, "Graph changed after a second apply."


def test_p17_initial_to_expected(initial_graph_p17: nx.Graph, expected_graph_p17: nx.Graph):
    """
    Verify that applying Production P17 transforms the initial graph into the expected graph.
    """
    production = ProductionP17(initial_graph_p17)
    production.apply()

    # Compare nodes and their attributes
    nodes_diff = []
    for node, data in initial_graph_p17.nodes(data=True):
        expected_data = expected_graph_p17.nodes.get(node, None)
        if data != expected_data:
            nodes_diff.append((node, data, expected_data))

    # Compare edges and their attributes
    edges_diff = []
    for u, v, data in initial_graph_p17.edges(data=True):
        expected_data = expected_graph_p17.get_edge_data(u, v, default=None)
        if data != expected_data:
            edges_diff.append(((u, v), data, expected_data))

    assert not nodes_diff, f"Node differences found: {nodes_diff}"
    assert not edges_diff, f"Edge differences found: {edges_diff}"


def test_p17_no_changes_for_non_valid_graph(non_valid_graph_p17: nx.Graph):
    """
    Verify that Production P17 does not modify the graph if the conditions are not met.
    """
    production = ProductionP17(non_valid_graph_p17)
    initial_state = nx.to_dict_of_dicts(non_valid_graph_p17)

    production.apply()

    final_state = nx.to_dict_of_dicts(non_valid_graph_p17)

    assert initial_state == final_state, "Graph should not change when conditions are not met."
