from ..production import Production
from math import sqrt

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

    def apply_with_reference_node(self, reference_node):
        """
        Apply P7 to mark the quadrilateral for splitting.
        """
        candidate_nodes = list(self.graph.nodes(data=True))
        candidate_nodes.sort(key=lambda x: sqrt((float(x[0].split(':')[1]) - reference_node['x'])**2 + (float(x[0].split(':')[2]) - reference_node['y'])**2))

        for node, data in candidate_nodes:
            if data.get('label') == 'Q' and data.get('R') == 0:
                self.graph.nodes[node]['R'] = 1
                return True

        return False
