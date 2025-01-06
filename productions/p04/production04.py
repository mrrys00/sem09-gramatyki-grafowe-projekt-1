from itertools import combinations
from networkx.algorithms import isomorphism

from ..production import Production
import networkx as nx


class ProductionP4(Production):
    """
    Production P4:
    Divides a quadrilateral with 2 hanging nodes into smaller quadrilaterals
    """

    def __init__(self, graph):
        super().__init__(graph)
        self.hanging_nodes = [] 

    @property
    def check(self):
        """
        Check if the production can be applied on the selected quadrilateral with 2 hanging nodes.
        """
        for node, data in self.graph.nodes(data=True):
            if data.get('label') == 'Q' and data.get('R') == 1:
                neighbors = list(self.graph.neighbors(node))
                
                corner_nodes = [n for n in neighbors if self.graph.nodes[n].get('h') == 0]

                self.hanging_nodes = []
                for (n1, n2) in combinations(corner_nodes, 2):
                    for n in nx.common_neighbors(self.graph, n1, n2):
                        if self.graph.nodes[n].get('h') == 1 and n[0] != 'Q' and n not in self.hanging_nodes and n not in corner_nodes:
                            self.hanging_nodes.append(n)

                self.hanging_nodes.sort() 

                if len(corner_nodes) == 4 and len(self.hanging_nodes) == 2:
                    r = self.graph.nodes[node].get('R')
                    if r != None:
                        neighbors_edges_cnt = 0
                        for (n1, n2) in combinations(neighbors, 2):
                            if self.graph.has_edge(n1, n2):
                                neighbors_edges_cnt += 1
                        if neighbors_edges_cnt == 2:
                            return self._extract_subgraph(node, neighbors)
        
        return None

    def apply(self):
        """Apply P4 to divide the quadrilateral."""
        result = self.check
        if result:
            q_node, neighbors = result

            hanging_node1 = self.hanging_nodes[0]
            hanging_node2 = self.hanging_nodes[1]

            verticles_for_hn1 = [n for n in neighbors if self.graph.get_edge_data(n, hanging_node1)]
            verticles_for_hn2 = [n for n in neighbors if self.graph.get_edge_data(n, hanging_node2)]

            _b1 = self.graph.get_edge_data(verticles_for_hn1[0], hanging_node1)['B']
            self.subgraph.add_edge(verticles_for_hn1[0], verticles_for_hn1[1], label='E', B=_b1)
            self.graph.add_edge(verticles_for_hn1[0], verticles_for_hn1[1])

            _b2 = self.graph.get_edge_data(verticles_for_hn2[1], hanging_node2)['B']
            self.subgraph.add_edge(verticles_for_hn2[0], verticles_for_hn2[1], label='E', B=_b2)
            self.graph.add_edge(verticles_for_hn2[0], verticles_for_hn2[1])
            
            # Remove the original node and its edges
            self.subgraph.remove_node(q_node)
            self.graph.remove_node(q_node)

            # Create new nodes and edges for the divided structure
            midpoints = {}
            for (n1, n2) in combinations(neighbors, 2):
                # existing edges
                if self.subgraph.get_edge_data(n1, n2):
                    self._create_midpoint(midpoints, n1, n2)

            self._fill_graph(neighbors, midpoints)

            # Replace subgraph in graph
            self.graph.update(self.subgraph)
            return True
        return False
