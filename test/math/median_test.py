import unittest

from src.math.median import median, quartile25, quartile75, filter_outside_quartile2575


class MedianTest(unittest.TestCase):
    def test_median1(self):
        vector = [2, 5, 1, 4, 1]
        m = median(vector)
        self.assertEqual(2, m)

    def test_median2(self):
        vector = [2, 5, 1, 4, 4, 1]
        m = median(vector)
        self.assertEqual(3, m)

    def test_quartiles(self):
        vector = [-6, 0, 1, 2, 4, 5, 5, 6, 7, 100]
        q25 = quartile25(vector)
        q75 = quartile75(vector)

        self.assertEqual(1, q25)
        self.assertEqual(6, q75)

    def test_filter_outside_quartile2575(self):
        vector = [-6, 0, 1, 2, 4, 5, 5, 6, 7, 100]
        result = filter_outside_quartile2575(vector)

        self.assertEqual([-6, 0, 1, 2, 4, 5, 5, 6, 7], result)