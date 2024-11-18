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
                    midpoint = self._create_midpoint(midpoints, n1, n2)
                    # Remove hanging node
                    hanging_node = [node for node in self.graph.nodes if
                                    self.graph.nodes[node]['x'] == self.subgraph.nodes[midpoint]['x'] and
                                    self.graph.nodes[node]['y'] == self.subgraph.nodes[midpoint]['y']][0]
                    self.graph.remove_node(hanging_node)

            self._fill_graph(neighbors, midpoints)

            # Replace subgraph in graph
            self.graph.update(self.subgraph)
