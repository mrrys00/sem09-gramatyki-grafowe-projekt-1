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
        """Apply P3 to divide the quadrilateral."""
        result = self.check
        if result:
            q_node, neighbors = result

            subgraph_matrix = {node: [] for node in neighbors}
            for (n1, n2) in combinations(neighbors, 2):
                if self.subgraph.get_edge_data(n1, n2):
                    subgraph_matrix[n1].append(n2)
                    subgraph_matrix[n2].append(n1)
            lone_vertices = list(filter(lambda n: len(subgraph_matrix[n]) == 1, subgraph_matrix.keys()))

            mid_x1 = (self.subgraph.nodes[lone_vertices[0]]['x'] + self.subgraph.nodes[lone_vertices[1]]['x']) / 2
            mid_y1 = self.subgraph.nodes[lone_vertices[0]]['y'] 
            hanging_node1 = f'v:{mid_x1}:{mid_y1}'

            mid_x2 = self.subgraph.nodes[lone_vertices[1]]['x'] 
            mid_y2 = (self.subgraph.nodes[lone_vertices[0]]['y'] + self.subgraph.nodes[lone_vertices[1]]['y']) / 2
            hanging_node2 = f'v:{mid_x2}:{mid_y2}'

            _b1 = self.graph.get_edge_data(lone_vertices[0], hanging_node1)['B']
            self.subgraph.add_edge(lone_vertices[0], 'v:1.0:0.0', label='E', B=_b1)
            self.graph.add_edge(lone_vertices[0], 'v:1.0:0.0')

            _b2 = self.graph.get_edge_data(lone_vertices[1], hanging_node2)['B']
            self.subgraph.add_edge('v:1.0:0.0', lone_vertices[1], label='E', B=_b2)
            self.graph.add_edge('v:1.0:0.0', lone_vertices[1])
            
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
