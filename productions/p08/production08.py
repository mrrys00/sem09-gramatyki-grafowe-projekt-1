from itertools import combinations

from math import sqrt
from ..production import Production


class ProductionP8(Production):
    """
    Production P8:
    Marks the quadrilateral for breaking if small quadrilateral is already marked
    """

    def _check_neighbors(self, primary_neighbors, secondary_neighbors, excluded_neighbor, neighbors, node):
        """Helper to check neighbor conditions and extract the subgraph."""
        for neighbor in primary_neighbors:
            neighbor_data = self.graph.nodes[neighbor]
            if neighbor_data.get('label') == 'Q' and neighbor_data.get('R') == 0:
                neighbor_subgraph_nodes = list(self.graph.neighbors(neighbor))
                if len(neighbor_subgraph_nodes) != 4:
                    continue
                for secondary in secondary_neighbors:
                    if secondary != excluded_neighbor and secondary in self.graph.neighbors(neighbor):
                        # Combine all relevant nodes and ensure uniqueness
                        all_nodes = neighbors + neighbor_subgraph_nodes + [node]
                        unique_nodes = list(dict.fromkeys(all_nodes))
                        return self._extract_subgraph(neighbor, unique_nodes)
        return None

    @property
    def check(self):
        """Check if the production can be applied on the selected quadrilateral."""
        for node, data in self.graph.nodes(data=True):
            if data.get('label') == 'Q' and data.get('R') == 1:
                neighbors = list(self.graph.neighbors(node))
                if len(neighbors) != 4:
                    continue

                for n1, n2 in combinations(neighbors, 2):
                    if self.graph.has_edge(n1, n2):
                        neighbors_n1 = list(self.graph.neighbors(n1))
                        neighbors_n2 = list(self.graph.neighbors(n2))

                        subgraph_a = self._check_neighbors(neighbors_n1, neighbors_n2, n1, neighbors, node)
                        subgraph_b = self._check_neighbors(neighbors_n2, neighbors_n1, n2, neighbors, node)

                        result = next((sg for sg in (subgraph_a, subgraph_b) if sg is not None), None)
                        if result:
                            return result

        return None

    def apply(self):
        """Apply P8 to the quadrilateral if possible."""
        result = self.check
        if result:
            q_node, neighbors = result

            # Update the subgraph
            self.subgraph.nodes[q_node]['R'] = 1
            self.graph.update(self.subgraph)
            return True
        return False

    def apply_with_reference_node(self, reference_node):
        """Apply P8 to the quadrilateral if possible."""
        candidate_nodes = list(self.graph.nodes(data=True))
        candidate_nodes.sort(key=lambda x: sqrt((float(x[0].split(':')[1]) - reference_node['x'])**2 + (float(x[0].split(':')[2]) - reference_node['y'])**2))

        central_node = None
        for node, data in candidate_nodes:
            if data.get('label') == 'Q' and data.get('R') == 1:
                central_node = node
                break

        if central_node:
            neighbors = list(self.graph.neighbors(central_node))
            if len(neighbors) != 4:
                return False

            for n1, n2 in combinations(neighbors, 2):
                if self.graph.has_edge(n1, n2):
                    neighbors_n1 = list(self.graph.neighbors(n1))
                    neighbors_n2 = list(self.graph.neighbors(n2))

                    subgraph_a = self._check_neighbors(neighbors_n1, neighbors_n2, n1, neighbors, central_node)
                    subgraph_b = self._check_neighbors(neighbors_n2, neighbors_n1, n2, neighbors, central_node)

                    result = next((sg for sg in (subgraph_a, subgraph_b) if sg is not None), None)
                    if result:
                        self.graph.nodes[result[0]]['R'] = 1
                        return True

        return False
