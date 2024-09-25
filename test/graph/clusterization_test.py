import unittest

from src.distance.manhattan import ManhattanDistanceCalculator
from src.graph.clusterization import clusterize_dfs
from src.graph.graph import dataset_to_graph


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
        self.assertEqual(2, len(clusters))
        self.assertEqual(3, len(clusters[0]))
        self.assertEqual(2, len(clusters[1]))