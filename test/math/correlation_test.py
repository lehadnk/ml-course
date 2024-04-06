import unittest

from src.math.correlation import pearson_correlation_coefficient


class CorrelationTest(unittest.TestCase):
    def test_pearson_correlation(self):
        vector1 = [99, 89, 91, 91, 86, 97]
        vector2 = [56, 58, 64, 51, 56, 53]

        pc = pearson_correlation_coefficient(vector1, vector2)
        return self.assertAlmostEqual(-0.22, pc, 2)
