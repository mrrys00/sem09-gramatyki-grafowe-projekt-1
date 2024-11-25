from itertools import combinations
from statistics import fmean

from networkx.classes import neighbors

from ..production import Production
from ..utils import visualize_graph


class ProductionP11(Production):
    """
    Production P11:
    Breaking quintilateral int 5 smaller quadrilaterals
    """

    @property
    def check(self):
        """Check if the production can be applied on the selected quintilateral."""
        for node, data in self.graph.nodes(data=True):
            if data.get('label') == 'P' and data.get('R') == 1:
                neighbors = list(self.graph.neighbors(node))
                if len(neighbors) != 5:
                    continue
                if any(self.graph.nodes[n].get('h') != 0 for n in neighbors):
                    continue

                for n1, n2, n3 in combinations(neighbors, 3):
                    if not (self.graph.has_edge(n1, n2) or self.graph.has_edge(n2, n3) or self.graph.has_edge(n3, n1)):
                        def get_common_neighbors_with_label(node1, node2, label):
                            # Find common neighbors
                            neighbors1 = set(self.graph.neighbors(node1))
                            neighbors2 = set(self.graph.neighbors(node2))
                            common_neighbors = neighbors1 & neighbors2

                            # Filter common neighbors by label
                            return [n for n in common_neighbors if self.graph.nodes[n].get('label') == label and n not in neighbors]
                        results = list()
                        results.append(get_common_neighbors_with_label(n1, n2, 'v'))
                        results.append(get_common_neighbors_with_label(n1, n3, 'v'))
                        results.append(get_common_neighbors_with_label(n2, n3, 'v'))

                        def check_one_empty_two_with_distinct_vertex(results):
                            empty_count = sum(1 for res in results if not res)
                            single_element_lists = [res[0] for res in results if len(res) == 1]

                            if empty_count == 1 and len(single_element_lists) == 2 and len(
                                    set(single_element_lists)) == 2:
                                return True, list(set(single_element_lists))

                            return False, ()
                        result,vertices = check_one_empty_two_with_distinct_vertex(results)
                        if result:
                            return self._extract_subgraph(node, neighbors+vertices)

        return None

    def apply(self):
        """Breaking quintilateral int 5 smaller quadrilaterals if possible."""
        result = self.check
        if result:
            q_node, nodes = result
            # Remove the original node and its edges
            neighbors = list(self.graph.neighbors(q_node))
            not_neighbors = [item for item in nodes if item not in neighbors]
            for n in not_neighbors:
                self.subgraph.nodes[n]['h'] = 0
            self.subgraph.remove_node(q_node)
            self.graph.remove_node(q_node)

            # Create new nodes and edges for the divided structure
            midpoints = {}
            for (n1, n2) in combinations(nodes, 2):
                # existing edges
                data = self.subgraph.get_edge_data(n1, n2)
                if data:
                    if n1 in neighbors and n2  in neighbors:
                        midpoint = self._create_midpoint(midpoints, n1, n2)
                        self.subgraph.nodes[midpoint]['h'] = -data['B']


            self._fill_graph(neighbors, midpoints)

            x = fmean([self.subgraph.nodes[neighbor].get('x') for _, neighbor in enumerate(neighbors)])
            y = fmean([self.subgraph.nodes[neighbor].get('y') for _, neighbor in enumerate(neighbors)])
            center_node = f'v:{x}:{y}'

            for n3 in list(midpoints) + not_neighbors:
                self.subgraph.add_edge(n3, center_node, label='E', B=1)

            # Replace subgraph in graph
            self.graph.update(self.subgraph)
