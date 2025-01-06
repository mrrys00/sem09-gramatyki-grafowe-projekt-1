from ..production import Production

class ProductionP7(Production):
    """
    Production P7:
    Virtual Adaptation: Marking Quadrilateral Elements for Splitting
    """

    @property
    def check(self):
        """
        Check if the production can be applied on quadrilateral elements with R == 0.
        """
        for node, data in self.graph.nodes(data=True):
            if data.get('label') == 'Q' and data.get('R') == 0:
                return node
        return None

    def apply(self):
        """
        Apply P7 to mark the quadrilateral for splitting.
        """
        q_node = self.check
        if q_node is not None:
            self.graph.nodes[q_node]['R'] = 1
            return True
        return False
