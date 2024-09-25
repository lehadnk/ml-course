import unittest

from src.distance.euclid import EuclideanDistanceCalculator
from src.distance.manhattan import ManhattanDistanceCalculator
from src.missing_values.missing_values import fill_missing_value_in_row_using_pearson, \
    fill_missing_value_in_row_using_nearest_neighbors


class MissingValuesTest(unittest.TestCase):
    def test_finding_missing_values_using_pearson(self):
        v = fill_missing_value_in_row_using_pearson([
            [99, 89, 91, 91, 86, 97],
            [56, 58, 64, 51, 56, 53],
            [91, 89, 91, 91, 84, 86],
            [160, 157, 165, 170, 157, 175],
            [58, 48, 54, 54, 44, 56]
        ], [None, 51, 91, 165, 54])

        self.assertAlmostEqual(94.21, v, 2)

    def test_finding_missing_values_using_nearest_row_calculated_by_manhattan_distance(self):
        value = fill_missing_value_in_row_using_nearest_neighbors(ManhattanDistanceCalculator(), [
            [5, 5, 5, 3],
            [5, 3, 4, 4],
            [2, 5, 3, 5]
        ], [3, 4, 4, None])

        self.assertEqual(4, value)