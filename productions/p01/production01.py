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
                    return node, neighbors  # Return the node and its neighbors if condition met
        return None

    def apply(self):
        """Apply P1 to divide the quadrilateral."""
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
                        y=(self.graph.nodes[n1]['y'] + self.graph.nodes[n2]['y']) / 2, h=0)
                    midpoints[midpoint] = (n1, n2)

            # Add new quadrilateral elements
            self.graph.add_node(f'Q1', label='Q', R=0)
            for mp, (n1, n2) in midpoints.items():
                self.graph.add_edge(mp, n1, label='E', B=0)
                self.graph.add_edge(mp, n2, label='E', B=0)
                self.graph.add_edge(mp, f'Q1', label='E', B=0)
