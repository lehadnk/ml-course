import unittest

from src.distance.manhattan import ManhattanDistanceCalculator


class ManhattanTest(unittest.TestCase):
    def test_manhattan(self):
        point1 = [0, 1]
        point2 = [3, 4]

        calculator = ManhattanDistanceCalculator()
        d = calculator.distance_between(point1, point2)

        self.assertEqual(6, d)
