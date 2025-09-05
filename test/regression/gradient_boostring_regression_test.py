import math
import unittest

from src.regression.decision_tree_regression import DecisionTreeRegressor
from src.regression.gradient_boosting_regression import GradientBoostingRegressor
from src.regression.linear_regression import LinearRegressor


class GradientBoostingRegressionTest(unittest.TestCase):
    def test_gradient_boostring_regression(self):
        trX = [
            [0.3, 1],
            [0.8, 1],
            [1.2, 1],
            [1.6, 1],
            [1.8, 1],
            [2.2, 1],
            [2.4, 1],
            [2.5, 1],
            [2.7, 1],
        ]

        trY = [4, 5, 6, 4.5, 2.2, 2, 3, 4.2, 5.7]
        ensemble1 = DecisionTreeRegressor()
        ensemble2 = GradientBoostingRegressor([
            DecisionTreeRegressor(),
            DecisionTreeRegressor(),
            DecisionTreeRegressor(),
            LinearRegressor(),
        ])

        ensemble1.learning_rate = 1
        ensemble1.fit(trX, trY)
        ensemble2.learning_rate = 0.1
        ensemble2.fit(trX, trY)

        tX = [
            [0.6, 1],
            [1.5, 1],
            [2.5, 1],
            [0.43, 1],
            [3.0, 1],
            [3.1, 1],
        ]
        tY = [4.7, 5.4, 3.6, 4.3, 4.5, 2.7]

        rmse1, rmse2 = 0, 0
        for x, y in zip(tX, tY):
            rmse1 += (y - ensemble1.predict(x)) ** 2
            rmse2 += (y - ensemble2.predict(x)) ** 2

        rmse1 /= len(tX)
        rmse1 = math.sqrt(rmse1)
        rmse2 /= len(tX)
        rmse2 = math.sqrt(rmse2)

        self.assertGreater(rmse1, rmse2)