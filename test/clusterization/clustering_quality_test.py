import unittest

from src.clusterization.clustering_quality import get_clustering_quality
from src.distance.euclid import EuclideanDistanceCalculator


class ClasteringQualityTest(unittest.TestCase):
    def test_clustering_quality(self):
        clusters = [
            [
                [0, 0],
                [1, 1],
                [-1, -1]
            ],
            [
                [4, 4],
                [5, 5],
                [6, 6],
            ]
        ]

        quality = get_clustering_quality(clusters, 2, EuclideanDistanceCalculator())
        self.assertEqual(2, len(quality))
        for q in quality:
            # distance between (0, 0) and (1, 1) is 1.41
            self.assertAlmostEquals((1.41 * 2) / 3, q, 2)