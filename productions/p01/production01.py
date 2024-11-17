from ..production import Production

from itertools import combinations
from statistics import fmean

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
                        nodes_to_subgraph = [node] + neighbors
                        self.subgraph = self.graph.__class__()
                        self.subgraph.add_nodes_from((n, self.graph.nodes[n]) for n in nodes_to_subgraph)
                        self.subgraph.add_edges_from(
                            (n, nbr, d)
                            for n, nbrs in self.graph.adj.items()
                            if n in nodes_to_subgraph
                            for nbr, d in nbrs.items()
                            if nbr in nodes_to_subgraph
                        )
                        return node, neighbors  # Return the node and its neighbors if condition met
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
                    print(n1, n2)
                    x = (self.subgraph.nodes[n1]['x'] + self.subgraph.nodes[n2]['x']) / 2
                    y = (self.subgraph.nodes[n1]['y'] + self.subgraph.nodes[n2]['y']) / 2
                    midpoint = f'v:{x}:{y}'
                    old_edge_b = self.subgraph.get_edge_data(n1, n2)['B']
                    if midpoint not in midpoints:
                        self.subgraph.add_node(
                            midpoint, label='v', x=x,y=y, h=1 - old_edge_b)
                        midpoints[midpoint] = (n1, n2)

            # Create new center node
            x = fmean([self.subgraph.nodes[neighbor].get('x') for _, neighbor in enumerate(neighbors)])
            y = fmean([self.subgraph.nodes[neighbor].get('y') for _, neighbor in enumerate(neighbors)])
            center_node = f'v:{x}:{y}'
            self.subgraph.add_node(center_node, label='v', x=x, y=y, h=0)

            # Connect new vertices with center and old ones
            for mp, (n1, n2) in midpoints.items():
                old_edge = self.subgraph.get_edge_data(n1, n2)
                self.subgraph.remove_edge(n1, n2)
                self.graph.remove_edge(n1, n2)
                self.subgraph.add_edge(mp, n1, label='E', B=old_edge['B'])
                self.subgraph.add_edge(mp, n2, label='E', B=old_edge['B'])
                self.subgraph.add_edge(mp, center_node, label='E', B=0)

            # Add new quadrilateral elements
            for node in neighbors:
                neighbors_of_node = list(self.subgraph.neighbors(node))
                x = fmean([self.subgraph.nodes[neighbor].get('x') for neighbor in neighbors_of_node + [node, center_node]])
                y = fmean([self.subgraph.nodes[neighbor].get('y') for neighbor in neighbors_of_node + [node, center_node]])
                q = f'Q:{x}:{y}'
                self.subgraph.add_node(q, label='Q', R=1)
                self.subgraph.add_edge(q, node)
                self.subgraph.add_edge(q, neighbors_of_node[0])
                self.subgraph.add_edge(q, center_node)
                self.subgraph.add_edge(q, neighbors_of_node[1])

            # Replace subgraph in graph
            self.graph.update(self.subgraph)
