import unittest

from src.distance.max import MaxDistanceCalculator


class ManhattanTest(unittest.TestCase):
    def test_max_distance(self):
        point1 = [0, 1]
        point2 = [3, 6]

        calculator = MaxDistanceCalculator()
        d = calculator.distance_between(point1, point2)

        self.assertEqual(5, d)
