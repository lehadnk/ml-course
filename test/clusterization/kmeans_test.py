import unittest

from src.clusterization.kmeans import KmeansClusterizer
from src.distance.euclid import EuclideanDistanceCalculator


class KmeansTest(unittest.TestCase):
    def test_kmeans(self):
        dataset = [
            (1, 1, 1),
            (2, 1, 1),
            (1, 2, 1),
            (2, 2, 1),

            (15, 4, 3),
            (15, 4, 4),
            (14, 4, 4),

            (25, 13, 12),
            (25, 13, 13),
            (25, 14, 14),
        ]

        kc = KmeansClusterizer(dataset)
        clusters = kc.kmeans_clustering(3, EuclideanDistanceCalculator())

        self.assertEqual(3, len(clusters))