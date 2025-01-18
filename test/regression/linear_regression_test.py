import unittest

from src.regression.linear_regression import LinearRegressor
from src.regression.moore_penrouse_linear_regression import MoorePenrouseLinearRegression


class MissingValuesTest(unittest.TestCase):
    def test_missing_values(self):
        data = [
            [50, 1, 500],
            [60, 1, 600],
            [70, 1, 700],
            [80, 1, 800],
        ]

        regressor = LinearRegressor(data)
        self.assertEqual(500, regressor.predict([50, 1]))
        self.assertEqual(900, regressor.predict([90, 1]))

    def test_moore_penrouse(self):
        data = [
            [1, 1, 1],
            [2, 2, 2],
            [3, 3, 3],
            [4, 4, 4],
        ]
        regressor = MoorePenrouseLinearRegression(data)

        self.assertAlmostEqual(3, regressor.predict([3, 3]), 2)
        self.assertAlmostEqual(6, regressor.predict([6, 6]), 2)