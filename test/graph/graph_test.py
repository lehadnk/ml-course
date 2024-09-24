import unittest

from src.distance.manhattan import ManhattanDistanceCalculator
from src.graph.graph import Graph, Node, Edge, dataset_to_graph


class GraphTest(unittest.TestCase):
    def test_get_edges_from(self):
        g = Graph()
        g.add_node(Node(1))
        g.add_node(Node(2))
        g.add_node(Node(3))

        g.add_edge(Edge(1, 2, 3))
        g.add_edge(Edge(1, 3, 2))
        g.add_edge(Edge(2, 3, 2))

        edges = g.get_edges_from(1)
        self.assertEqual(len(edges), 2)

    def test_get_edges_to(self):
        g = Graph()
        g.add_node(Node(1))
        g.add_node(Node(2))
        g.add_node(Node(3))

        g.add_edge(Edge(1, 2, 3))
        g.add_edge(Edge(1, 3, 2))
        g.add_edge(Edge(2, 3, 2))

        edges = g.get_edges_to(3)
        self.assertEqual(len(edges), 2)

    def test_get_shortest_edge(self):
        g = Graph()
        g.add_node(Node(1))
        g.add_node(Node(2))

        g.add_edge(Edge(1, 2, 4))
        g.add_edge(Edge(1, 2, 2))
        g.add_edge(Edge(1, 2, 5))

        edge = g.get_shortest_edge(1, 2)
        self.assertEqual(edge.distance, 2)

    def test_get_longest_edge(self):
        g = Graph()
        g.add_node(Node(1))
        g.add_node(Node(2))

        g.add_edge(Edge(1, 2, 4))
        g.add_edge(Edge(1, 2, 2))
        g.add_edge(Edge(1, 2, 5))

        edge = g.get_longest_edge(1, 2)
        self.assertEqual(edge.distance, 5)

    def test_dataset_to_graph(self):
        dataset = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
        ]

        graph = dataset_to_graph(dataset, ManhattanDistanceCalculator())

        self.assertEqual(len(graph.nodes), 3)
        self.assertEqual(len(graph.edges), 3)
        self.assertEqual(9, graph.get_shortest_edge(0, 1).distance)
        self.assertEqual(9, graph.get_shortest_edge(1, 2).distance)
        self.assertEqual(18, graph.get_shortest_edge(0, 2).distance)

    def test_delete_edges_longer_than(self):
        g = Graph()
        g.add_node(Node(1))
        g.add_node(Node(2))

        g.add_edge(Edge(1, 2, 4))
        g.add_edge(Edge(1, 2, 2))
        g.add_edge(Edge(1, 2, 5))

        g.delete_edges_longer_than(3.9)
        self.assertEqual(1, len(g.get_edges(1, 2)))