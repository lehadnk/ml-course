import unittest

from src.regression.decision_tree_regression import DecisionTreeRegressor


class DecisionTreeRegressionTest(unittest.TestCase):
    def test(self):
        X = [
            [1, 6, 0.4, 0.558],
            [2, 7, 0.8, -1.107],
            [3, 8, 1.2, 0.946],
            [4, 9, 1.6, -1.652],
            [5, 10, 2.0, -0.312],
            [6, 11, 2.4, 0.021],
            [7, 5, 2.8, -1.894],
            [8, 6, 3.2, 0.18],
            [9, 7, 3.6, -1.118],
            [10, 8, 4.0, -1.974],
            [11, 9, 4.4, 1.223],
            [12, 10, 4.8, -1.378],
            [13, 11, 5.2, 1.829],
            [14, 5, 5.6, -1.613],
            [15, 6, 6.0, 1.39],
            [16, 7, 6.4, 0.919],
            [17, 8, 6.8, 0.145],
            [18, 9, 7.2, 0.208],
            [19, 10, 7.6, 1.318],
            [20, 11, 8.0, 0.309],
        ]

        Y = [
            2.597,
            3.354,
            3.709,
            3.854,
            10.482,
            10.281,
            5.332,
            5.582,
            3.933,
            4.153,
            4.641,
            9.775,
            10.796,
            7.052,
            7.276,
            8.66,
            10.87,
            11.347,
            16.511,
            17.107,
        ]

        regressor = DecisionTreeRegressor()
        regressor.fit(X, Y)
        y = regressor.predict([13, None, 5.2, 1.829])
        self.assertAlmostEqual(y, 8.37, 2)