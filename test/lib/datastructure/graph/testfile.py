from lib.datastructure.graph.graph import WeightDigraph

import pytest


@pytest.mark.parametrize(
    "G", [
        WeightDigraph()
    ]
)
def test_Graph(G):
    G.addVertex('yumo1')
    G.addVertex('yumo2')
    G.addVertex('yumo3')
    G.addVertex('yumo4')
