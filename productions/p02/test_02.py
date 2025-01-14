import pytest
import networkx as nx

from productions.p02.production02 import ProductionP2
from productions.utils import prepare_valid_test_graph, prepare_corrupted_test_graph, \
    prepare_valid_test_graph_with_hanging_node


@pytest.fixture(scope='function')
def prepare_graph_positive():
    yield prepare_valid_test_graph()


@pytest.fixture(scope='function')
def prepare_graph_positive_hanging():
    yield prepare_valid_test_graph_with_hanging_node()


@pytest.fixture(scope='function')
def prepare_graph_negative():
    yield prepare_corrupted_test_graph()

@pytest.fixture(scope='function')
def prepare_bigger_graph():
    G = nx.Graph()
    G.add_nodes_from([
        ('v:0.0:0.0', {'label': 'v', 'x': 0.0, 'y': 0.0, 'h': 0}),
        ('v:5.0:0.0', {'label': 'v', 'x': 5.0, 'y': 0.0, 'h': 0}),
        ('v:10.0:0.0', {'label': 'v', 'x': 10.0, 'y': 0.0, 'h': 0}),
        ('v:10.0:5.0', {'label': 'v', 'x': 10.0, 'y': 5.0, 'h': 0}),
        ('v:10.0:10.0', {'label': 'v', 'x': 10.0, 'y': 10.0, 'h': 0}),
        ('v:5.0:10.0', {'label': 'v', 'x': 5.0, 'y': 10.0, 'h': 0}),
        ('v:0.0:10.0', {'label': 'v', 'x': 0.0, 'y': 10.0, 'h': 0}),
        ('v:0.0:5.0', {'label': 'v', 'x': 0.0, 'y': 5.0, 'h': 0}),
        ('v:5.0:5.0', {'label': 'v', 'x': 5.0, 'y': 5.0, 'h': 0}),

        ('v:2.5:5.0', {'label': 'v', 'x': 2.5, 'y': 5.0, 'h': 1}),
        ('v:0.0:2.5', {'label': 'v', 'x': 0.0, 'y': 2.5, 'h': 0}),
        ('v:2.5:0.0', {'label': 'v', 'x': 2.5, 'y': 0.0, 'h': 0}),
        ('v:5.0:2.5', {'label': 'v', 'x': 5.0, 'y': 2.5, 'h': 1}),
        ('v:2.5:2.5', {'label': 'v', 'x': 2.5, 'y': 2.5, 'h': 0}),

        ('Q:2.5:7.5', {'label': 'Q', 'R': 1}),
        ('Q:7.5:7.5', {'label': 'Q', 'R': 1}),
        ('Q:7.5:2.5', {'label': 'Q', 'R': 0}),

        ('Q:1.25:1.25', {'label': 'Q', 'R': 0}),
        ('Q:1.25:3.75', {'label': 'Q', 'R': 0}),
        ('Q:3.75:1.25', {'label': 'Q', 'R': 0}),
        ('Q:3.75:3.75', {'label': 'Q', 'R': 0})
    ])
    G.add_edges_from([
        ('v:0.0:0.0', 'v:2.5:0.0', {'label': 'E', 'B': 1}),
        ('v:2.5:0.0', 'v:5.0:0.0', {'label': 'E', 'B': 1}),
        ('v:5.0:0.0', 'v:10.0:0.0', {'label': 'E', 'B': 1}),
        ('v:10.0:0.0', 'v:10.0:5.0', {'label': 'E', 'B': 1}),
        ('v:10.0:5.0', 'v:10.0:10.0', {'label': 'E', 'B': 1}),
        ('v:10.0:10.0', 'v:5.0:10.0', {'label': 'E', 'B': 1}),
        ('v:5.0:10.0', 'v:0.0:10.0', {'label': 'E', 'B': 1}),
        ('v:0.0:10.0', 'v:0.0:5.0', {'label': 'E', 'B': 1}),
        ('v:0.0:5.0', 'v:0.0:2.5', {'label': 'E', 'B': 1}),
        ('v:0.0:2.5', 'v:0.0:0.0', {'label': 'E', 'B': 1}),

        ('v:5.0:5.0', 'v:10.0:5.0', {'label': 'E', 'B': 0}),
        ('v:5.0:5.0', 'v:5.0:10.0', {'label': 'E', 'B': 0}),

        ('v:0.0:5.0', 'v:2.5:5.0', {'label': 'E', 'B': 0}),
        ('v:2.5:5.0', 'v:5.0:5.0', {'label': 'E', 'B': 0}),
        ('v:5.0:5.0', 'v:5.0:2.5', {'label': 'E', 'B': 0}),
        ('v:5.0:2.5', 'v:5.0:0.0', {'label': 'E', 'B': 0}),

        ('v:0.0:2.5', 'v:2.5:2.5', {'label': 'E', 'B': 0}),
        ('v:2.5:5.0', 'v:2.5:2.5', {'label': 'E', 'B': 0}),
        ('v:5.0:2.5', 'v:2.5:2.5', {'label': 'E', 'B': 0}),
        ('v:2.5:0.0', 'v:2.5:2.5', {'label': 'E', 'B': 0}),

        ('Q:2.5:7.5', 'v:5.0:10.0'), ('Q:2.5:7.5', 'v:0.0:10.0'), ('Q:2.5:7.5', 'v:0.0:5.0'), ('Q:2.5:7.5', 'v:5.0:5.0'),
        ('Q:7.5:7.5', 'v:5.0:5.0'), ('Q:7.5:7.5', 'v:10.0:5.0'), ('Q:7.5:7.5', 'v:10.0:10.0'), ('Q:7.5:7.5', 'v:5.0:10.0'),
        ('Q:7.5:2.5', 'v:5.0:5.0'), ('Q:7.5:2.5', 'v:5.0:0.0'), ('Q:7.5:2.5', 'v:10.0:0.0'), ('Q:7.5:2.5', 'v:10.0:5.0'),

        ('Q:1.25:1.25', 'v:2.5:2.5'), ('Q:1.25:1.25', 'v:0.0:0.0'), ('Q:1.25:1.25', 'v:0.0:2.5'), ('Q:1.25:1.25', 'v:2.5:0.0'), 
        ('Q:1.25:3.75', 'v:0.0:5.0'), ('Q:1.25:3.75', 'v:2.5:5.0'), ('Q:1.25:3.75', 'v:2.5:2.5'), ('Q:1.25:3.75', 'v:0.0:2.5'), 
        ('Q:3.75:1.25', 'v:2.5:2.5'), ('Q:3.75:1.25', 'v:2.5:0.0'), ('Q:3.75:1.25', 'v:5.0:0.0'), ('Q:3.75:1.25', 'v:5.0:2.5'), 
        ('Q:3.75:3.75', 'v:2.5:2.5'), ('Q:3.75:3.75', 'v:2.5:5.0'), ('Q:3.75:3.75', 'v:5.0:5.0'), ('Q:3.75:3.75', 'v:5.0:2.5'), 
    ])
    yield G


def test_positive_p02_check_without_hanging_node(prepare_graph_positive: nx.Graph):
    """check is not None if the graph is valid"""
    assert ProductionP2(prepare_graph_positive).check is None


def test_positive_p02_check(prepare_graph_positive_hanging: nx.Graph):
    """check is not None if the graph is valid"""
    assert ProductionP2(prepare_graph_positive_hanging).check is not None


def test_positive_p02_check_after_production(prepare_graph_positive_hanging: nx.Graph):
    """check is None after apply the production1"""
    ProductionP2(prepare_graph_positive_hanging).apply()
    assert ProductionP2(prepare_graph_positive_hanging).check is None


def test_positive_p02_nodes_number_after_production(prepare_graph_positive_hanging: nx.Graph):
    """apply creates new node in graph, verify nodes number"""
    ProductionP2(prepare_graph_positive_hanging).apply()
    expected_nodes_number = 13
    assert len(prepare_graph_positive_hanging.nodes()) == expected_nodes_number


def test_positive_p02_v_nodes_number_after_production(prepare_graph_positive_hanging: nx.Graph):
    """apply creates new node in graph, verify v nodes number"""
    ProductionP2(prepare_graph_positive_hanging).apply()
    expected_v_nodes_number = 9
    assert len([s for s in prepare_graph_positive_hanging.nodes() if 'v' in s]) == expected_v_nodes_number


def test_positive_p02_q_nodes_number_after_production(prepare_graph_positive_hanging: nx.Graph):
    """apply creates new node in graph, verify g nodes number"""
    ProductionP2(prepare_graph_positive_hanging).apply()
    expected_q_nodes_number = 4
    assert len([s for s in prepare_graph_positive_hanging.nodes() if 'Q' in s]) == expected_q_nodes_number


def test_positive_p02_q_nodes_inactive_after_production_after_production(prepare_graph_positive_hanging: nx.Graph):
    """apply creates new node in graph, verify Q nodes R==0 after production"""
    ProductionP2(prepare_graph_positive_hanging).apply()
    q_nodes = [s for s in prepare_graph_positive_hanging.nodes() if 'Q' in s]
    assert all(q_r == 0 for q_r in
               [prepare_graph_positive_hanging.nodes()[q_r0]['R'] for q_r0 in q_nodes])


def test_positive_p02_h_nodes_number_before_production(prepare_graph_positive_hanging: nx.Graph):
    """verify h nodes number, before apply production"""
    expected_h_nodes_number = 1
    h_nodes = [(v) for v,data in prepare_graph_positive_hanging.nodes(data=True)
               if data['label'] != 'Q' and data['h'] == 1]
    assert len(h_nodes) == expected_h_nodes_number


def test_positive_p02_h_nodes_number_after_production(prepare_graph_positive_hanging: nx.Graph):
    """verify h nodes number, after applying production"""
    ProductionP2(prepare_graph_positive_hanging).apply()
    expected_h_nodes_number = 0
    h_nodes = [(v) for v,data in prepare_graph_positive_hanging.nodes(data=True)
               if data['label'] != 'Q' and data['h'] == 1]
    assert len(h_nodes) == expected_h_nodes_number
    

def test_positive_p02_edges_number_after_production(prepare_graph_positive_hanging: nx.Graph):
    """apply creates new node in graph, verify edges number"""
    ProductionP2(prepare_graph_positive_hanging).apply()
    expected_edges_number = 28
    assert len(prepare_graph_positive_hanging.edges()) == expected_edges_number


def test_positive_boundary_edges_before_production(prepare_graph_positive_hanging: nx.Graph):
    """verify boundary edges number, before applying the production"""
    boundary_edges = [(u, v, data) for u, v, data in prepare_graph_positive_hanging.edges(data=True)
                      if u.find('Q') == -1 and v.find('Q') == -1 and data['B'] == 1]
    expected_boundary_edges_number = 5
    assert len(boundary_edges) == expected_boundary_edges_number


def test_positive_boundary_edges_after_production(prepare_graph_positive_hanging: nx.Graph):
    """verify boundary edges number after applying the production"""
    ProductionP2(prepare_graph_positive_hanging).apply()
    boundary_edges = [(u, v) for u, v, data in prepare_graph_positive_hanging.edges(data=True)
                      if u.find('Q') == -1 and v.find('Q') == -1 and data['B'] == 1]
    assert all(prepare_graph_positive_hanging.edges[u, v]['B'] == 1 for u, v in boundary_edges)


def test_positive_inner_edges_before_production(prepare_graph_positive_hanging: nx.Graph):
    """verify inner edges number before applying the production"""
    inner_edges = [(u, v) for u, v, data in prepare_graph_positive_hanging.edges(data=True)
                   if u.find('Q') == -1 and v.find('Q') == -1 and data['B'] == 0]
    assert len(inner_edges) == 0


def test_positive_inner_edges_after_production(prepare_graph_positive_hanging: nx.Graph):
    """verify inner edges number after applying the production"""
    ProductionP2(prepare_graph_positive_hanging).apply()
    inner_edges = [(u, v) for u, v, data in prepare_graph_positive_hanging.edges(data=True)
                   if u.find('Q') == -1 and v.find('Q') == -1 and data['B'] == 0]
    assert len(inner_edges) > 0
    assert all(prepare_graph_positive_hanging.edges[u, v]['B'] == 0 for u, v in inner_edges)


# ========


def test_positive_bigger_p02_check(prepare_bigger_graph: nx.Graph):
    """check is not None if the graph is valid"""
    assert ProductionP2(prepare_bigger_graph).check is not None


def test_positive_bigger_p02_check_after_production(prepare_bigger_graph: nx.Graph):
    """check is None after apply the production1"""
    ProductionP2(prepare_bigger_graph).apply()
    assert ProductionP2(prepare_bigger_graph).check is not None


def test_positive_bigger_p02_check_after_production_twice(prepare_bigger_graph: nx.Graph):
    """check is None after apply the production1"""
    ProductionP2(prepare_bigger_graph).apply()
    ProductionP2(prepare_bigger_graph).apply()
    assert ProductionP2(prepare_bigger_graph).check is None


def test_positive_bigger_p02_nodes_number_after_production(prepare_bigger_graph: nx.Graph):
    """apply creates new node in graph, verify nodes number"""
    ProductionP2(prepare_bigger_graph).apply()
    expected_nodes_number = 28
    assert len(prepare_bigger_graph.nodes()) == expected_nodes_number


def test_positive_bigger_p02_v_nodes_number_after_production(prepare_bigger_graph: nx.Graph):
    """apply creates new node in graph, verify v nodes number"""
    ProductionP2(prepare_bigger_graph).apply()
    expected_v_nodes_number = 18
    assert len([s for s in prepare_bigger_graph.nodes() if 'v' in s]) == expected_v_nodes_number


def test_positive_bigger_p02_q_nodes_number_after_production(prepare_bigger_graph: nx.Graph):
    """apply creates new node in graph, verify g nodes number"""
    ProductionP2(prepare_bigger_graph).apply()
    expected_q_nodes_number = 10
    assert len([s for s in prepare_bigger_graph.nodes() if 'Q' in s]) == expected_q_nodes_number


def test_positive_bigger_p02_q_nodes_inactive_after_production_after_production_twice(prepare_bigger_graph: nx.Graph):
    """apply creates new node in graph, verify Q nodes R==0 after production"""
    ProductionP2(prepare_bigger_graph).apply()
    ProductionP2(prepare_bigger_graph).apply()
    q_nodes = [s for s in prepare_bigger_graph.nodes() if 'Q' in s]
    assert all(q_r == 0 for q_r in
               [prepare_bigger_graph.nodes()[q_r0]['R'] for q_r0 in q_nodes])


def test_positive_bigger_p02_h_nodes_number_before_production(prepare_bigger_graph: nx.Graph):
    """verify h nodes number, before apply production"""
    expected_h_nodes_number = 2
    h_nodes = [(v) for v,data in prepare_bigger_graph.nodes(data=True)
               if data['label'] != 'Q' and data['h'] == 1]
    assert len(h_nodes) == expected_h_nodes_number


def test_positive_bigger_p02_h_nodes_number_after_production(prepare_bigger_graph: nx.Graph):
    """verify h nodes number, after applying production"""
    ProductionP2(prepare_bigger_graph).apply()
    expected_h_nodes_number = 2
    h_nodes = [(v) for v,data in prepare_bigger_graph.nodes(data=True)
               if data['label'] != 'Q' and data['h'] == 1]
    assert len(h_nodes) == expected_h_nodes_number


def test_positive_bigger_p02_h_nodes_number_after_production_twice(prepare_bigger_graph: nx.Graph):
    """verify h nodes number, after applying production twice"""
    ProductionP2(prepare_bigger_graph).apply()
    expected_h_nodes_number = 2
    h_nodes = [(v) for v,data in prepare_bigger_graph.nodes(data=True)
               if data['label'] != 'Q' and data['h'] == 1]
    assert len(h_nodes) == expected_h_nodes_number
    

def test_positive_bigger_p02_edges_number_after_production(prepare_bigger_graph: nx.Graph):
    """apply creates new node in graph, verify edges number"""
    ProductionP2(prepare_bigger_graph).apply()
    expected_edges_number = 67
    assert len(prepare_bigger_graph.edges()) == expected_edges_number


def test_positive_bigger_boundary_edges_before_production(prepare_bigger_graph: nx.Graph):
    """verify boundary edges number, before applying the production"""
    boundary_edges = [(u, v, data) for u, v, data in prepare_bigger_graph.edges(data=True)
                      if u.find('Q') == -1 and v.find('Q') == -1 and data['B'] == 1]
    expected_boundary_edges_number = 10
    assert len(boundary_edges) == expected_boundary_edges_number


def test_positive_bigger_boundary_edges_after_production(prepare_bigger_graph: nx.Graph):
    """verify boundary edges number after applying the production"""
    ProductionP2(prepare_bigger_graph).apply()
    boundary_edges = [(u, v) for u, v, data in prepare_bigger_graph.edges(data=True)
                      if u.find('Q') == -1 and v.find('Q') == -1 and data['B'] == 1]
    assert all(prepare_bigger_graph.edges[u, v]['B'] == 1 for u, v in boundary_edges)


def test_positive_bigger_inner_edges_before_production(prepare_bigger_graph: nx.Graph):
    """verify inner edges number before applying the production"""
    inner_edges = [(u, v) for u, v, data in prepare_bigger_graph.edges(data=True)
                   if u.find('Q') == -1 and v.find('Q') == -1 and data['B'] == 0]
    assert len(inner_edges) == 10


def test_positive_bigger_inner_edges_after_production(prepare_bigger_graph: nx.Graph):
    """verify inner edges number after applying the production"""
    ProductionP2(prepare_bigger_graph).apply()
    inner_edges = [(u, v) for u, v, data in prepare_bigger_graph.edges(data=True)
                   if u.find('Q') == -1 and v.find('Q') == -1 and data['B'] == 0]
    assert len(inner_edges) == 15
    assert all(prepare_bigger_graph.edges[u, v]['B'] == 0 for u, v in inner_edges)


# ========


def test_negative_p02_check(prepare_graph_negative: nx.Graph):
    """check is None if the graph is not valid"""
    assert ProductionP2(prepare_graph_negative).check is None


def test_negative_p02_apply(prepare_graph_negative: nx.Graph):
    """apply creates new node in graph due to the graph is invalid"""
    ProductionP2(prepare_graph_negative).apply()
    assert 'Q' not in prepare_graph_negative
