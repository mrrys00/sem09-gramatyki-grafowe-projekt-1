from ..production import Production

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
                x = (self.graph.nodes[n1]['x'] + self.graph.nodes[n2]['x']) / 2
                y = (self.graph.nodes[n1]['y'] + self.graph.nodes[n2]['y']) / 2
                midpoint = f'v:{x}:{y}'
                old_edge_b = self.graph.get_edge_data(n1, n2)['B']
                if midpoint not in midpoints:
                    self.graph.add_node(
                        midpoint, label='v', x=x,y=y, h=1 - old_edge_b)
                    midpoints[midpoint] = (n1, n2)

            # Create new center node
            x = fmean([self.graph.nodes[neighbor].get('x') for _, neighbor in enumerate(neighbors)])
            y = fmean([self.graph.nodes[neighbor].get('y') for _, neighbor in enumerate(neighbors)])
            center_node = f'v:{x}:{y}'
            self.graph.add_node(center_node, label='v', x=x, y=y, h=0)

            # print(node)
            # print(neighbors)
            # print(midpoints)

            # Connect new vertices with center and old ones
            for mp, (n1, n2) in midpoints.items():
                old_edge = self.graph.get_edge_data(n1, n2)
                self.graph.remove_edge(n1, n2)
                self.graph.add_edge(mp, n1, label='E', B=old_edge['B'])
                self.graph.add_edge(mp, n2, label='E', B=old_edge['B'])
                self.graph.add_edge(mp, center_node, label='E', B=0)

            # Add new quadrilateral elements
            for i, node in enumerate(neighbors):
                neighbors_of_node = list(self.graph.neighbors(node))
                x = fmean([self.graph.nodes[neighbor].get('x') for _, neighbor in enumerate(neighbors_of_node + [center_node])])
                y = fmean([self.graph.nodes[neighbor].get('y') for _, neighbor in enumerate(neighbors_of_node + [center_node])])
                q = f'Q:{x}:{y}'
                self.graph.add_node(q, label='Q', R='0')
                self.graph.add_edge(q, node)
                self.graph.add_edge(q, neighbors_of_node[0])
                self.graph.add_edge(q, neighbors_of_node[1])
                self.graph.add_edge(q, center_node)
                # print(list(self.graph.neighbors(node)))
