from itertools import combinations

from ..production import Production


class ProductionP10(Production):
    """
    Production P10:
    Divides a pentagon with 1 hanging node into 5 smaller pentagons
    """

    @property
    def check(self):
        """Check if the production can be applied to the selected pentagon with a hanging node."""
        for node, data in self.graph.nodes(data=True):
            if data.get("label") == "P" and data.get("R") == 1:
                neighbors = list(self.graph.neighbors(node))
                if all(self.graph.nodes[n].get("h") == 0 for n in neighbors):
                    neighbors_edges_cnt = 0
                    for n1, n2 in combinations(neighbors, 2):
                        if self.graph.has_edge(n1, n2):
                            neighbors_edges_cnt += 1
                    print(neighbors_edges_cnt)
                    if neighbors_edges_cnt == 4:
                        print("check passed")
                        return self._extract_subgraph(node, neighbors)
        print("didnt pass check")
        return None

    def apply(self):
        """Apply P10 to divide the pentagon with a hanging node."""
        result = self.check
        if result:
            p_node, neighbors = result
            self.subgraph.remove_node(p_node)
            self.graph.remove_node(p_node)

            delta = max(
                abs(
                    self.subgraph.nodes[neighbors[0]]["x"]
                    - self.subgraph.nodes[neighbors[1]]["x"]
                ),
                abs(
                    self.subgraph.nodes[neighbors[0]]["y"]
                    - self.subgraph.nodes[neighbors[1]]["y"]
                ),
            )

            midpoints = {}
            for n1, n2 in combinations(neighbors, 2):
                if self.subgraph.get_edge_data(n1, n2):
                    self._create_midpoint(midpoints, n1, n2)
                elif (
                    abs(self.subgraph.nodes[n1]["x"] - self.subgraph.nodes[n2]["x"])
                    + abs(self.subgraph.nodes[n1]["y"] - self.subgraph.nodes[n2]["y"])
                    == delta
                ):

                    self.subgraph.add_edge(n1, n2, label="E", B=1)
                    self.graph.add_edge(n1, n2)
                    midpoint = self._create_midpoint(midpoints, n1, n2)

                    hanging_node = next(
                        node
                        for node in self.graph.nodes
                        if self.graph.nodes[node]["x"]
                        == self.subgraph.nodes[midpoint]["x"]
                        and self.graph.nodes[node]["y"]
                        == self.subgraph.nodes[midpoint]["y"]
                    )
                    self.graph.remove_node(hanging_node)

            self._fill_graph(neighbors, midpoints)
            self.graph.update(self.subgraph)


"""
from productions.p10.production10 import ProductionP10

    G = nx.Graph()
    G.add_node("P:5.0:5.0", label="P", R=1)
    G.add_nodes_from(
        [
            ("v:0.0:0.0", {"label": "v", "x": 0.0, "y": 0.0, "h": 0}),
            ("v:5.0:0.0", {"label": "v", "x": 5.0, "y": 0.0, "h": 0}),
            ("v:10.0:0.0", {"label": "v", "x": 10.0, "y": 0.0, "h": 0}),
            ("v:10.0:10.0", {"label": "v", "x": 10.0, "y": 10.0, "h": 0}),
            ("v:0.0:10.0", {"label": "v", "x": 0.0, "y": 10.0, "h": 0}),
            ("v:15.0:5.0", {"label": "v", "x": 15.0, "y": 5.0, "h": 0}),
        ]
    )
    G.add_edges_from(
        [
            ("v:0.0:0.0", "v:5.0:0.0", {"label": "E", "B": 1}),
            ("v:5.0:0.0", "v:10.0:0.0", {"label": "E", "B": 1}),
            ("v:15.0:5.0", "v:10.0:10.0", {"label": "E", "B": 1}),
            ("v:10.0:0.0", "v:15.0:5.0", {"label": "E", "B": 1}),
            ("v:10.0:10.0", "v:0.0:10.0", {"label": "E", "B": 1}),
            ("v:0.0:10.0", "v:0.0:0.0", {"label": "E", "B": 1}),
            ("P:5.0:5.0", "v:0.0:0.0"),
            ("P:5.0:5.0", "v:15.0:5.0"),
            ("P:5.0:5.0", "v:10.0:0.0"),
            ("P:5.0:5.0", "v:10.0:10.0"),
            ("P:5.0:5.0", "v:0.0:10.0"),
        ]
    )

    visualize_graph(G)
    prod10 = ProductionP10(G)
    prod10.apply()
    visualize_graph(G)
"""
