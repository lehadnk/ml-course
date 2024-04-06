import unittest

from src.math.median import median


class MedianTest(unittest.TestCase):
    def test_median1(self):
        vector = [2, 5, 1, 4, 1]
        m = median(vector)
        self.assertEqual(2, m)

    def test_median2(self):
        vector = [2, 5, 1, 4, 4, 1]
        m = median(vector)
        self.assertEqual(3, m)
