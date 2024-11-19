from itertools import combinations

from ..production import Production


class ProductionP9(Production):
    """
    Production P9:
    Divides a pentagon into 5 smaller pentagons
    """

    @property
    def check(self):
        """Check if the production can be applied on the selected pentagon."""
        # Find nodes with R=1 (element marked for splitting) and h=0 for all vertices
        for node, data in self.graph.nodes(data=True):
            if data.get("label") == "P" and data.get("R") == 1:
                neighbors = list(self.graph.neighbors(node))
                if all(self.graph.nodes[n].get("h") == 0 for n in neighbors):
                    neighbors_edges_cnt = 0
                    for n1, n2 in combinations(neighbors, 2):
                        if self.graph.has_edge(n1, n2):
                            neighbors_edges_cnt += 1
                    print(neighbors_edges_cnt)
                    if neighbors_edges_cnt == 5:
                        print("check passed")
                        return self._extract_subgraph(node, neighbors)
        print("didnt pass check")
        return None

    def apply(self):
        """Apply P9 to divide the pentagon"""
        # similar logic to P1
        result = self.check
        if result:
            q_node, neighbors = result

            self.subgraph.remove_node(q_node)
            self.graph.remove_node(q_node)

            midpoints = {}
            for n1, n2 in combinations(neighbors, 2):
                if self.subgraph.get_edge_data(n1, n2):
                    self._create_midpoint(midpoints, n1, n2)

            self._fill_graph(neighbors, midpoints)
            self.graph.update(self.subgraph)

        # TODO implement
