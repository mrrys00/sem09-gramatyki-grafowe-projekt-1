from itertools import combinations

from ..production import Production


class ProductionP16(Production):
    """
    Production P16:
    Marks the pentagon elements as breakable. 
    """

    @property
    def check(self):
        """Checks if the production can be applied to the selected pentagon."""
        for node, data in self.graph.nodes(data=True):
            if data.get("label") == "P" and data.get("R") == 0:
                neighbors = list(self.graph.neighbors(node))
                return self._extract_subgraph(node, neighbors)
        return None

    def apply(self):
        """Apply P16 to mark the pentagon elements as breakable."""

        result = self.check
        if result:
            r_node, neighbors = result
            self.graph.nodes[r_node]['R'] = 1
            return True
        return False
