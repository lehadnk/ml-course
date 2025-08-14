import unittest

from src.tree.gini import gini_impurity


class GiniTest(unittest.TestCase):
    def test_gini(self):
        p1 = [0, 0, 1, 1, 0]
        p2 = [1, 1, 1, 1, 1]
        p3 = [0, 0, 0, 1, 1]
        y = [1, 1, 1, 0, 0]

        self.assertAlmostEqual(0.23, gini_impurity(p1, y), 2)
        self.assertAlmostEqual(0.24, gini_impurity(p2, y), 2)
        self.assertAlmostEqual(0, gini_impurity(p3, y), 2)