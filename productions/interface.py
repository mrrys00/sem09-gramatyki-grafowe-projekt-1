from abc import ABC, abstractmethod
import networkx as nx
import matplotlib.pyplot as plt

class Production(ABC):
    """Base class for graph productions."""
    def __init__(self, graph: nx.Graph):
        self.graph = graph

    @abstractmethod
    def check(self):
        """Check if the production can be applied."""
        pass

    @abstractmethod
    def apply(self):
        """Apply the production to modify the graph."""
        pass

    def visualize(self, title="Graph Visualization"):
        """Visualize the current graph."""
        pos = nx.spring_layout(self.graph)
        labels = nx.get_node_attributes(self.graph, "label")
        edge_labels = nx.get_edge_attributes(self.graph, "label")

        plt.figure(figsize=(8, 6))
        nx.draw(self.graph, pos, with_labels=True, labels=labels, node_color="lightblue", node_size=2000)
        nx.draw_networkx_edge_labels(self.graph, pos, edge_labels=edge_labels)
        plt.title(title)
        plt.show()
