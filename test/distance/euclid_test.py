import unittest

from src.distance.euclid import EuclideanDistanceCalculator


class EuclidTest(unittest.TestCase):

    def test_euclidean_distance(self):
        point1 = [1, 0]
        point2 = [3, 4]

        calculator = EuclideanDistanceCalculator()
        d = calculator.distance_between(point1, point2)

        self.assertAlmostEqual(d, 4.47, 2)
