import unittest

from src.clusterization.forel import ForelClusterizator
from src.distance.euclid import EuclideanDistanceCalculator


class ForelTest(unittest.TestCase):
    def test_forel_clusterization(self):
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

        clusterizator = ForelClusterizator(dataset)
        dc = EuclideanDistanceCalculator()
        clusters = clusterizator.perform_clustering(7, dc)

        self.assertTrue(3, len(clusters))
        for cluster in clusters:
            distances = dc.distance_to_all(cluster)
            for point_distances in distances:
                for distance in point_distances:
                    self.assertTrue(distance < 4)