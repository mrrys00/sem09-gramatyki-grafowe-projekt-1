from itertools import combinations

from ..production import Production


class ProductionP1(Production):
    """
    Production P1:
    Divides a quadrilateral into 4 smaller quadrilaterals
    """

    def check(self):
        """Check if the production can be applied on the selected quadrilateral."""
        # Find nodes with R=1 (element marked for splitting) and h=0 for all vertices
        for node, data in self.graph.nodes(data=True):
            if data.get('label') == 'Q' and data.get('R') == 1:
                neighbors = list(self.graph.neighbors(node))
                if all(self.graph.nodes[n].get('h') == 0 for n in neighbors):
                    neighbors_edges_cnt = 0
                    for (n1, n2) in combinations(neighbors, 2):
                        if self.graph.has_edge(n1, n2):
                            neighbors_edges_cnt += 1
                    if neighbors_edges_cnt == 4:
                        return self._extract_subgraph(node, neighbors)

        return None

    def apply(self):
        """Apply P1 to divide the quadrilateral."""
        result = self.check()
        if result:
            q_node, neighbors = result
            # Remove the original node and its edges
            self.subgraph.remove_node(q_node)
            self.graph.remove_node(q_node)

            # Create new nodes and edges for the divided structure
            midpoints = {}
            for (n1, n2) in combinations(neighbors, 2):
                if self.subgraph.get_edge_data(n1, n2):
                    self._create_midpoint(midpoints, n1, n2)

            self._fill_graph(neighbors, midpoints)

            # Replace subgraph in graph
            self.graph.update(self.subgraph)
