import unittest

from src.graph.dfs import deep_first_search
from src.graph.graph import BidirectionalGraph, BidirectionalEdge


class DfsTest(unittest.TestCase):
    def test_dfs(self):
        graph = BidirectionalGraph(None)
        graph.add_edge(BidirectionalEdge(1, 2, 2))
        graph.add_edge(BidirectionalEdge(1, 3, 2))
        graph.add_edge(BidirectionalEdge(2, 4, 2))
        graph.add_edge(BidirectionalEdge(4, 5, 2))
        graph.add_node(6)
        graph.add_node(7)

        dfs = deep_first_search(graph, 1)

        self.assertTrue(1 in dfs)
        self.assertTrue(2 in dfs)
        self.assertTrue(3 in dfs)
        self.assertTrue(4 in dfs)
        self.assertTrue(5 in dfs)
        self.assertFalse(6 in dfs)
        self.assertFalse(7 in dfs)