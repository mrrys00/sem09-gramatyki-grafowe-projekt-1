import pytest
import networkx as nx

from productions.p02.production02 import ProductionP2

def test_production_p2():
    G = nx.Graph()

    G.nodes["v1"]["h"] = 1
    prod = ProductionP2(G)
    assert prod.check() is not None
    prod.apply()
    assert "Q2" in G
