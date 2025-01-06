from itertools import combinations

from ..production import Production


class ProductionP2(Production):
    """
    Production P2:
    Divides a quadrilateral with 1 hanging node into 4 smaller quadrilaterals
    """

    @property
    def check(self):
        """Check if the production can be applied on the selected quadrilateral."""
        # Find nodes with R=1 (element marked for splitting) and h=0 for all corner vertices
        for node, data in self.graph.nodes(data=True):
            if data.get('label') == 'Q' and data.get('R') == 1:
                neighbors = list(self.graph.neighbors(node))
                if all(self.graph.nodes[n].get('h') == 0 for n in neighbors):
                    neighbors_edges_cnt = 0
                    for (n1, n2) in combinations(neighbors, 2):
                        if self.graph.has_edge(n1, n2):
                            neighbors_edges_cnt += 1
                    if neighbors_edges_cnt == 3:
                        return self._extract_subgraph(node, neighbors)

        return None

    def apply(self):
        """Apply P2 to divide the quadrilateral."""
        result = self.check
        if result:
            q_node, neighbors = result

            subgraph_matrix = {node: [] for node in neighbors}
            for (n1, n2) in combinations(neighbors, 2):
                if self.subgraph.get_edge_data(n1, n2):
                    subgraph_matrix[n1].append(n2)
                    subgraph_matrix[n2].append(n1)
            lone_vertices = list(filter(lambda n: len(subgraph_matrix[n]) == 1, subgraph_matrix.keys()))
            x = (self.subgraph.nodes[lone_vertices[0]]['x'] + self.subgraph.nodes[lone_vertices[1]]['x']) / 2
            y = (self.subgraph.nodes[lone_vertices[0]]['y'] + self.subgraph.nodes[lone_vertices[1]]['y']) / 2
            hanging_node = f'v:{x}:{y}'
            _b = self.graph.get_edge_data(lone_vertices[0], hanging_node)['B']
            self.subgraph.add_edge(lone_vertices[0], lone_vertices[1], label='E', B=_b)
            self.graph.add_edge(lone_vertices[0], lone_vertices[1])

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
