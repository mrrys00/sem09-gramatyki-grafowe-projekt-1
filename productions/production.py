from abc import ABC, abstractmethod
from statistics import fmean
import networkx as nx


class Production(ABC):
    """Base class for graph productions."""

    def __init__(self, graph: nx.Graph):
        self.graph = graph
        self.subgraph = None

    @property
    def check(self):
        """Check if the production can be applied."""
        pass

    @abstractmethod
    def apply(self):
        """Apply the production to modify the graph."""
        pass

    def _extract_subgraph(self, node, neighbors):
        """Extract subgraph from to apply production to"""
        nodes_to_subgraph = [node] + neighbors
        self.subgraph = self.graph.__class__()
        self.subgraph.add_nodes_from((n, self.graph.nodes[n]) for n in nodes_to_subgraph)
        self.subgraph.add_edges_from(
            (n, nbr, d)
            for n, nbrs in self.graph.adj.items()
            if n in nodes_to_subgraph
            for nbr, d in nbrs.items()
            if nbr in nodes_to_subgraph
        )
        return node, neighbors  # Return the node and its neighbors if condition met

    def _create_midpoint(self, midpoints, n1, n2):
        """Create midpoint in the middle of the edge"""
        x = (self.subgraph.nodes[n1]['x'] + self.subgraph.nodes[n2]['x']) / 2
        y = (self.subgraph.nodes[n1]['y'] + self.subgraph.nodes[n2]['y']) / 2
        midpoint = f'v:{x}:{y}'
        old_edge_b = self.subgraph.get_edge_data(n1, n2)['B']
        if midpoint not in midpoints:
            self.subgraph.add_node(
                midpoint, label='v', x=x, y=y, h=1 - old_edge_b)
            midpoints[midpoint] = (n1, n2)
        return midpoint

    def _fill_graph(self, neighbors, midpoints):
        """Fill the subgraph with edges and new hyper edge"""
        # Create new center node
        x = fmean([self.subgraph.nodes[neighbor].get('x') for _, neighbor in enumerate(neighbors)])
        y = fmean([self.subgraph.nodes[neighbor].get('y') for _, neighbor in enumerate(neighbors)])
        center_node = f'v:{x}:{y}'
        self.subgraph.add_node(center_node, label='v', x=x, y=y, h=0)

        # Connect new vertices with center and old ones
        for mp, (n1, n2) in midpoints.items():
            old_edge = self.subgraph.get_edge_data(n1, n2)
            self.subgraph.remove_edge(n1, n2)
            self.graph.remove_edge(n1, n2)
            self.subgraph.add_edge(mp, n1, label='E', B=old_edge['B'])
            self.subgraph.add_edge(mp, n2, label='E', B=old_edge['B'])
            self.subgraph.add_edge(mp, center_node, label='E', B=0)

        # Add new quadrilateral elements
        for node in neighbors:
            neighbors_of_node = list(self.subgraph.neighbors(node))
            x = fmean([self.subgraph.nodes[neighbor].get('x') for neighbor in neighbors_of_node + [node, center_node]])
            y = fmean([self.subgraph.nodes[neighbor].get('y') for neighbor in neighbors_of_node + [node, center_node]])
            q = f'Q:{x}:{y}'
            self.subgraph.add_node(q, label='Q', R=0)
            self.subgraph.add_edge(q, node)
            self.subgraph.add_edge(q, neighbors_of_node[0])
            self.subgraph.add_edge(q, center_node)
            self.subgraph.add_edge(q, neighbors_of_node[1])
