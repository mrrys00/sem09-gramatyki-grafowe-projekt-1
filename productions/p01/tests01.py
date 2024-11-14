import pytest
import networkx as nx

from productions.p01.production01 import ProductionP1

def test_production_p1():
    G = nx.Graph()

    prod = ProductionP1(G)
    assert prod.check() is not None
    prod.apply()
    assert "Q1" in G
