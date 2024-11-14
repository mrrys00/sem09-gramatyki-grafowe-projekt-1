from ..production import Production

class ProductionP2(Production):
    """
    Production P2:
    Similar to P1 but with a hanging node on one edge
    """

    def check(self):
        """Check if the production can be applied when a hanging node exists on one edge."""
        for node, data in self.graph.nodes(data=True):
            if data.get('label') == 'Q' and data.get('R') == 1:
                neighbors = list(self.graph.neighbors(node))
                hanging_count = sum(1 for n in neighbors if self.graph.nodes[n].get('h') == 1)
                if hanging_count == 1:
                    return node, neighbors
        return None

    def apply(self):
        """Apply P2 to divide the quadrilateral with a hanging node."""
        result = self.check()
        if result:
            node, neighbors = result
            # Remove the original node and its edges
            self.graph.remove_node(node)

            # Create new nodes and edges for the divided structure
            midpoints = {}
            for i, n1 in enumerate(neighbors):
                n2 = neighbors[(i + 1) % len(neighbors)]
                midpoint = f'M{n1}{n2}'
                if midpoint not in midpoints:
                    self.graph.add_node(
                        midpoint, label='v', x=(self.graph.nodes[n1]['x'] + self.graph.nodes[n2]['x']) / 2,
                        y=(self.graph.nodes[n1]['y'] + self.graph.nodes[n2]['y']) / 2, h=1 if i == 0 else 0)
                    midpoints[midpoint] = (n1, n2)

            # Add new quadrilateral elements
            self.graph.add_node(f'Q2', label='Q', R=0)
            for mp, (n1, n2) in midpoints.items():
                self.graph.add_edge(mp, n1, label='E', B=0)
                self.graph.add_edge(mp, n2, label='E', B=0)
                self.graph.add_edge(mp, f'Q2', label='E', B=0)
