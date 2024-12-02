from itertools import combinations

from networkx.classes import all_neighbors

from ..production import Production


class ProductionP8(Production):
    """
    Production P8:
    #TODO write documentation
    """

    @property
    def check(self):
        """Check if the production can be applied on the selected quadrilateral."""
        for node, data in self.graph.nodes(data=True):
            if data.get('label') == 'Q' and data.get('R') == 1:
                neighbors = list(self.graph.neighbors(node))
                if len(neighbors) != 4:
                    continue

                for (n1, n2) in combinations(neighbors, 2):
                    if self.graph.has_edge(n1, n2):
                        neighbors1 = list(self.graph.neighbors(n1))
                        neighbors2 = list(self.graph.neighbors(n2))

                        def check_neighbors(primary, secondary, excluded):
                            for node_2 in primary:
                                r_node_2 = self.graph.nodes[node_2]
                                if r_node_2.get('label') == 'Q' and r_node_2.get('R') == 0:
                                    for neighbor in secondary:
                                        if neighbor != excluded and neighbor in self.graph.neighbors(node_2):
                                            whole_except_q = neighbors + list(self.graph.neighbors(node_2)) + [node]
                                            return self._extract_subgraph(node_2, whole_except_q)

                        check_neighbors(neighbors1, neighbors2, n1)
                        check_neighbors(neighbors2, neighbors1, n2)


        return None

    def apply(self):
        """Apply P8 to mark for breaking the quadrilateral."""
        result = self.check
        if result:
            q_node, neighbors = result

            self.subgraph.nodes[q_node]['R'] = 1
            self.graph.update(self.subgraph)
