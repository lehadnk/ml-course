import unittest

from src.math.stdev import stdev


class StdevTest(unittest.TestCase):
    def test_stdev(self):
        vector = [0, 1, 2, 3, 4, 5]
        stdev_value = stdev(vector)
        self.assertAlmostEqual(1.87083, stdev_value, 5)
