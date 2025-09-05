import unittest

from src.regression.linear_regression import LinearRegressor
from src.regression.moore_penrouse_linear_regression import MoorePenrouseLinearRegression


class LinearRegressionTest(unittest.TestCase):
    def test_missing_values(self):
        X = [
            [50, 1],
            [60, 1],
            [70, 1],
            [80, 1],
        ]
        Y = [500, 600, 700, 800]

        regressor = LinearRegressor()
        regressor.fit(X, Y)
        self.assertEqual(500, regressor.predict([50, 1]))
        self.assertEqual(900, regressor.predict([90, 1]))

    def test_moore_penrouse(self):
        X = [
            [1, 1],
            [2, 2],
            [3, 3],
            [4, 4],
        ]
        Y = [1, 2, 3, 4]
        regressor = MoorePenrouseLinearRegression()
        regressor.fit(X, Y)

        self.assertAlmostEqual(3, regressor.predict([3, 3]), 2)
        self.assertAlmostEqual(6, regressor.predict([6, 6]), 2)