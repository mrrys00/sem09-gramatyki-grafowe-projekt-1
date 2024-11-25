from itertools import combinations
from networkx.algorithms import isomorphism

from ..production import Production
import networkx as nx


class ProductionP3(Production):
    """
    Production P3:
    Divides a quadrilateral with 2 hanging nodes into smaller quadrilaterals
    """

    @property
    def check(self):
        """
        Check if the production can be applied on the selected quadrilateral with 2 hanging nodes.
        """
        for node, data in self.graph.nodes(data=True):
            if data.get('label') == 'Q' and data.get('R') == 1:
                neighbors = list(self.graph.neighbors(node))
                
                corner_nodes = [n for n in neighbors if self.graph.nodes[n].get('h') == 0]
                hanging_nodes = []
                for neighbor in neighbors:
                    for n in self.graph.neighbors(neighbor):
                        if self.graph.nodes[n].get('h') == 1 and n != 'Q' and n not in hanging_nodes:
                            hanging_nodes.append(n)

                if len(corner_nodes) == 4 and len(hanging_nodes) == 2:
                    subgraph = nx.subgraph(self.graph, (*corner_nodes, *hanging_nodes, node))
                    if isomorphism.GraphMatcher(subgraph, self.graph).is_isomorphic():
                        return self._extract_subgraph(node, neighbors)
        
        return None


    def apply(self):
        """Apply P2 to divide the quadrilateral."""
        result = self.check
        if result:
            q_node, neighbors = result
            # Remove the original node and its edges
            self.subgraph.remove_node(q_node)
            self.graph.remove_node(q_node)

            # Obtain delta between vertices
            delta = max(abs(self.subgraph.nodes[neighbors[0]]['x'] - self.subgraph.nodes[neighbors[1]]['x']),
                        abs(self.subgraph.nodes[neighbors[0]]['y'] - self.subgraph.nodes[neighbors[1]]['y']))

            # Create new nodes and edges for the divided structure
            midpoints = {}
            for (n1, n2) in combinations(neighbors, 2):
                # existing edges
                if self.subgraph.get_edge_data(n1, n2):
                    self._create_midpoint(midpoints, n1, n2)
                # artificially add edge to hanging node
                elif abs(self.subgraph.nodes[n1]['x'] - self.subgraph.nodes[n2]['x']) + abs(
                        self.subgraph.nodes[n1]['y'] - self.subgraph.nodes[n2]['y']) == delta:
                    self.subgraph.add_edge(n1, n2, label='E', B=1)
                    self.graph.add_edge(n1, n2)
                    _ = self._create_midpoint(midpoints, n1, n2)
                    

            self._fill_graph(neighbors, midpoints)

            # Replace subgraph in graph
            self.graph.update(self.subgraph)
