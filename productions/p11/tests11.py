import pytest
import networkx as nx
from networkx.algorithms.isomorphism import GraphMatcher

from productions.p11.production11 import ProductionP11
from productions.utils import prepare_valid_test_graph_for_prod_11_initial, \
    prepare_valid_test_graph_for_prod_11_after_modification, prepare_non_valid_test_graph_for_prod_11_initial


@pytest.fixture(scope="function")
def initial_graph_p11():
    """Fixture providing the initial valid graph for Production P11."""
    return prepare_valid_test_graph_for_prod_11_initial()


@pytest.fixture(scope="function")
def expected_graph_p11():
    """Fixture providing the expected graph after Production P11."""
    return prepare_valid_test_graph_for_prod_11_after_modification()


@pytest.fixture(scope="function")
def non_valid_graph_p11():
    """Fixture providing a non-valid graph for Production P11."""
    return prepare_non_valid_test_graph_for_prod_11_initial()


def test_p11_graph_isomorphism_with_left_side(initial_graph_p11):
    """
    Verify if the initial graph is isomorphic to the left side of Production P11.
    """
    left_side_graph = prepare_valid_test_graph_for_prod_11_initial()
    matcher = GraphMatcher(initial_graph_p11, left_side_graph)
    assert matcher.is_isomorphic(), "Graph is not isomorphic to the left side of Production P11."


def test_p11_apply_changes_structure(initial_graph_p11, expected_graph_p11):
    """
    Verify if applying Production P11 correctly transforms the graph structure.
    """
    production = ProductionP11(initial_graph_p11)
    production.apply()

    matcher = GraphMatcher(initial_graph_p11, expected_graph_p11)
    assert matcher.is_isomorphic(), "Graph after production does not match the expected graph."


def test_p11_node_count_after_production(initial_graph_p11, expected_graph_p11):
    """
    Verify if the number of nodes is correct after applying Production P11.
    """
    production = ProductionP11(initial_graph_p11)
    production.apply()

    assert initial_graph_p11.number_of_nodes() == expected_graph_p11.number_of_nodes(), (
        "Number of nodes after production is incorrect."
    )


def test_p11_edge_count_after_production(initial_graph_p11, expected_graph_p11):
    """
    Verify if the number of edges is correct after applying Production P11.
    """
    production = ProductionP11(initial_graph_p11)
    production.apply()

    assert initial_graph_p11.number_of_edges() == expected_graph_p11.number_of_edges(), (
        "Number of edges after production is incorrect."
    )


def test_p11_no_changes_for_non_valid_graph(non_valid_graph_p11):
    """
    Verify that Production P11 does not modify the graph if the conditions are not met.
    """
    production = ProductionP11(non_valid_graph_p11)
    initial_state = nx.to_dict_of_dicts(non_valid_graph_p11)

    production.apply()

    final_state = nx.to_dict_of_dicts(non_valid_graph_p11)
    assert initial_state == final_state, "Graph should not change when conditions are not met."


def test_p11_multiple_apply_no_change(initial_graph_p11):
    """
    Verify that applying Production P11 multiple times does not change the graph further.
    """
    production = ProductionP11(initial_graph_p11)
    production.apply()

    first_state = nx.to_dict_of_dicts(initial_graph_p11)

    production.apply()
    second_state = nx.to_dict_of_dicts(initial_graph_p11)

    assert first_state == second_state, "Graph changed after a second application of Production P11."

