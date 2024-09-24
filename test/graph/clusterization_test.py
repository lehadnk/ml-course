import unittest

from src.distance.manhattan import ManhattanDistanceCalculator
from src.graph.clusterization import clusterize_dfs
from src.graph.graph import Graph, Node, dataset_to_graph


class ClusterizationTest(unittest.TestCase):
    def test_clusterization_dfs(self):
        dataset = [
            [1, 1, 1],
            [1, 2, 1],
            [1, 3, 1],
            [5, 4, 6],
            [5, 4, 7],
        ]

        graph = dataset_to_graph(dataset, ManhattanDistanceCalculator())

        clusters = clusterize_dfs(graph, 4)
        self.assertEqual(len(clusters), 2)
        self.assertEqual(len(clusters[0]), 3)
        self.assertEqual(len(clusters[1]), 2)