from abc import ABC, abstractmethod
import networkx as nx

class Production(ABC):
    """Base class for graph productions."""
    def __init__(self, graph: nx.Graph):
        self.graph = graph
        self.subgraph = None

    @abstractmethod
    def check(self):
        """Check if the production can be applied."""
        pass

    @abstractmethod
    def apply(self):
        """Apply the production to modify the graph."""
        pass
