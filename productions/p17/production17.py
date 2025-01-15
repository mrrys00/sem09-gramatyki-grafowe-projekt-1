from itertools import combinations
from math import sqrt
from ..production import Production


class ProductionP17(Production):
    """
    Production P17:
    Marks the pentagon for breaking if small quadrilateral is already marked
    """

    def _is_node_central(self, central_node, node_1, node_2):
        """Check if the central node is equidistant from two other nodes."""
        central_node_data = self.graph.nodes[central_node]
        node_1_data = self.graph.nodes[node_1]
        node_2_data = self.graph.nodes[node_2]
        return (
            node_1_data['x'] + node_2_data['x'] == 2 * central_node_data['x'] and
            node_1_data['y'] + node_2_data['y'] == 2 * central_node_data['y']
        )

    def _check_neighbors(self, primary_neighbors, secondary_neighbors, excluded_neighbors, neighbors, node):
        """Helper to check neighbor conditions and extract the subgraph."""
        for neighbor in primary_neighbors:
            neighbor_data = self.graph.nodes[neighbor]
            if neighbor_data.get('label') == 'Q' and neighbor_data.get('R') == 0:
                neighbor_subgraph_nodes = list(self.graph.neighbors(neighbor))
                if len(neighbor_subgraph_nodes) == 5:
                    for secondary in secondary_neighbors:
                        if secondary not in excluded_neighbors and secondary in self.graph.neighbors(neighbor) and \
                                self._is_node_central(excluded_neighbors[1], excluded_neighbors[0], secondary):
                            all_nodes = neighbors + neighbor_subgraph_nodes + [node]
                            unique_nodes = list(dict.fromkeys(all_nodes))
                            return self._extract_subgraph(neighbor, unique_nodes)
        return None

    def _find_candidate_nodes(self, reference_node):
        """Find candidate nodes sorted by proximity to the reference node."""
        candidate_nodes = list(self.graph.nodes(data=True))
        candidate_nodes.sort(key=lambda x: sqrt((float(x[0].split(':')[1]) - reference_node['x']) ** 2 +
                                                (float(x[0].split(':')[2]) - reference_node['y']) ** 2))
        return candidate_nodes

    def _process_neighbors(self, node, neighbors):
        """Process the neighbors to check for a valid quadrilateral for breaking."""
        for n1, n2 in combinations(neighbors, 2):
            if self.graph.has_edge(n1, n2):
                neighbors_n1 = list(self.graph.neighbors(n1))
                neighbors_n2 = list(self.graph.neighbors(n2))
                subgraph_a = self._check_neighbors(neighbors_n1, neighbors_n2, (n1, n2), neighbors, node)
                subgraph_b = self._check_neighbors(neighbors_n2, neighbors_n1, (n2, n1), neighbors, node)
                result = next((sg for sg in (subgraph_a, subgraph_b) if sg is not None), None)
                if result:
                    return result
        return None

    @property
    def check(self):
        """Check if the production can be applied to the selected quadrilateral."""
        for node, data in self.graph.nodes(data=True):
            if data.get('label') == 'Q' and data.get('R') == 1:
                neighbors = list(self.graph.neighbors(node))
                if len(neighbors) == 4:
                    result = self._process_neighbors(node, neighbors)
                    if result:
                        return result
        return None

    def apply(self):
        """Apply P17 to the pentagon if possible."""
        result = self.check
        if result:
            q_node, neighbors = result
            self.subgraph.nodes[q_node]['R'] = 1
            self.graph.update(self.subgraph)
            return True
        return False

    def apply_with_reference_node(self, reference_node):
        """Apply P8 to the quadrilateral with a reference node."""
        candidate_nodes = self._find_candidate_nodes(reference_node)

        for node, data in candidate_nodes:
            if data.get('label') == 'Q' and data.get('R') == 1:
                neighbors = list(self.graph.neighbors(node))
                if len(neighbors) == 4:
                    result = self._process_neighbors(node, neighbors)
                    if result:
                        self.graph.nodes[result[0]]['R'] = 1
                        return True
        return False
