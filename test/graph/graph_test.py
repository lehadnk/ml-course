import unittest

from src.distance.manhattan import ManhattanDistanceCalculator
from src.graph.graph import dataset_to_graph, BidirectionalGraph, BidirectionalEdge


class GraphTest(unittest.TestCase):
    def test_get_edges_from(self):
        g = BidirectionalGraph(None)
        g.add_edge(BidirectionalEdge(1, 2, 3))
        g.add_edge(BidirectionalEdge(1, 3, 2))
        g.add_edge(BidirectionalEdge(2, 3, 2))

        edges = g.get_edges_from(1)
        self.assertEqual(2, len(edges))

    def test_get_edges_to(self):
        g = BidirectionalGraph(None)
        g.add_edge(BidirectionalEdge(1, 2, 3))
        g.add_edge(BidirectionalEdge(1, 3, 2))
        g.add_edge(BidirectionalEdge(2, 3, 2))

        edges = g.get_edges_to(3)
        self.assertEqual(2, len(edges))

    def test_get_shortest_edge(self):
        g = BidirectionalGraph(None)
        g.add_edge(BidirectionalEdge(1, 2, 4))
        g.add_edge(BidirectionalEdge(1, 2, 2))
        g.add_edge(BidirectionalEdge(1, 2, 5))

        edge = g.get_shortest_edge(1, 2)
        self.assertEqual(edge.weight, 2)

    def test_get_longest_edge(self):
        g = BidirectionalGraph(None)
        g.add_edge(BidirectionalEdge(1, 2, 4))
        g.add_edge(BidirectionalEdge(1, 2, 2))
        g.add_edge(BidirectionalEdge(1, 2, 5))

        edge = g.get_longest_edge(1, 2)
        self.assertEqual(5, edge.weight)

    def test_dataset_to_graph(self):
        dataset = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
        ]

        graph = dataset_to_graph(dataset, ManhattanDistanceCalculator())

        self.assertEqual(len(graph.get_nodes()), 3)
        self.assertEqual(len(graph.edge_list), 3)
        self.assertEqual(9, graph.get_shortest_edge(0, 1).weight)
        self.assertEqual(9, graph.get_shortest_edge(1, 2).weight)
        self.assertEqual(18, graph.get_shortest_edge(0, 2).weight)

    def test_delete_edges_longer_than(self):
        g = BidirectionalGraph(None)
        g.add_edge(BidirectionalEdge(1, 2, 4))
        g.add_edge(BidirectionalEdge(1, 2, 2))
        g.add_edge(BidirectionalEdge(1, 2, 5))

        g.delete_edges_longer_than(3.9)
        self.assertEqual(1, len(g.get_edges_between(1, 2)))

    def test_is_cyclic(self):
        g1 = BidirectionalGraph(None)
        g1.add_edge(BidirectionalEdge(1, 3, 3))
        g1.add_edge(BidirectionalEdge(2, 3, 3))

        self.assertFalse(g1.is_cyclic())

        g1.add_edge(BidirectionalEdge(1, 2, 3))

        self.assertTrue(g1.is_cyclic())

        g2 = BidirectionalGraph(None)
        g2.add_edge(BidirectionalEdge(7, 6, 3))
        g2.add_edge(BidirectionalEdge(6, 5, 3))
        g2.add_edge(BidirectionalEdge(8, 2, 3))
        g2.add_edge(BidirectionalEdge(0, 1, 3))
        g2.add_edge(BidirectionalEdge(2, 5, 3))
        g2.add_edge(BidirectionalEdge(8, 6, 3))

        self.assertTrue(g2.is_cyclic())