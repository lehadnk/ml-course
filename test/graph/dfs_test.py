import unittest

from src.graph.dfs import deep_first_search
from src.graph.graph import Graph, Node, Edge


class DfsTest(unittest.TestCase):
    def test_dfs(self):
        graph = Graph()
        graph.add_node(Node(1))
        graph.add_node(Node(2))
        graph.add_node(Node(3))
        graph.add_node(Node(4))
        graph.add_node(Node(5))
        graph.add_node(Node(6))

        graph.add_edge(Edge(1, 2, 2))
        graph.add_edge(Edge(1, 3, 2))
        graph.add_edge(Edge(2, 4, 2))
        graph.add_edge(Edge(4, 5, 2))

        dfs = deep_first_search(graph, 1)

        self.assertTrue(1 in dfs)
        self.assertTrue(2 in dfs)
        self.assertTrue(3 in dfs)
        self.assertTrue(4 in dfs)
        self.assertTrue(5 in dfs)
        self.assertFalse(6 in dfs)