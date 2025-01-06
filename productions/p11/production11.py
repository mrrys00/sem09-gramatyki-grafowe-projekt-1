from itertools import combinations
from statistics import fmean

import networkx as nx
from networkx.classes import neighbors

from ..production import Production
from ..utils import visualize_graph


class ProductionP11(Production):
    """
    Production P11:
    Breaking pentagon int 5 smaller quadrilaterals
    """

    @property
    def check(self):
        """Check if the production can be applied on the selected pentagon."""

        def get_common_neighbors_with_label(node1, node2, label):
            """Find common neighbors of two nodes that match a specific label and geometric condition."""
            neighbors1 = set(self.graph.neighbors(node1))
            neighbors2 = set(self.graph.neighbors(node2))
            common_neighbors = neighbors1 & neighbors2

            # Filter common neighbors by label and geometric properties
            return [
                n for n in common_neighbors
                if (
                        self.graph.nodes[n].get('label') == label and
                        self.graph.nodes[n].get('x') == (
                                self.graph.nodes[node1].get('x') + self.graph.nodes[node2].get('x')) / 2 and
                        self.graph.nodes[n].get('y') == (
                                self.graph.nodes[node1].get('y') + self.graph.nodes[node2].get('y')) / 2 and
                        n not in neighbors
                )
            ]

        for node, data in self.graph.nodes(data=True):
            if data.get('label') != 'Q' or data.get('R') != 1:
                continue

            neighbors = list(self.graph.neighbors(node))
            if len(neighbors) != 5:
                continue

            results = []
            for n1, n2 in combinations(neighbors, 2):
                if not self.graph.has_edge(n1, n2):
                    common_neighbors = get_common_neighbors_with_label(n1, n2, 'v')
                    results.extend(common_neighbors)

                if len(results) == 2:
                    return self._extract_subgraph(node, neighbors + results)

        return None

    def apply(self):
        """Apply P11 to pentagon if possible."""
        result = self.check
        if result:
            q_node, nodes = result
            # Remove the original node and its edges
            neighbors = list(self.graph.neighbors(q_node))
            not_neighbors = [item for item in nodes if item not in neighbors]
            for n in not_neighbors:
                self.subgraph.nodes[n]['h'] = 0
            self.subgraph.remove_node(q_node)
            self.graph.remove_node(q_node)

            # Create new nodes and edges for the divided structure
            midpoints = {}
            for (n1, n2) in combinations(nodes, 2):
                # existing edges
                data = self.subgraph.get_edge_data(n1, n2)
                if data:
                    if n1 in neighbors and n2 in neighbors:
                        midpoint = self._create_midpoint(midpoints, n1, n2)
                        self.subgraph.nodes[midpoint]['h'] = 1 - data['B']

            self._fill_graph(neighbors, midpoints)

            x = fmean([self.subgraph.nodes[neighbor].get('x') for _, neighbor in enumerate(neighbors)])
            y = fmean([self.subgraph.nodes[neighbor].get('y') for _, neighbor in enumerate(neighbors)])
            center_node = f'v:{x}:{y}'

            for n3 in list(midpoints) + not_neighbors:
                self.subgraph.add_edge(n3, center_node, label='E', B=0)

            # Replace subgraph in graph
            self.graph.update(self.subgraph)
            return True
        return False
