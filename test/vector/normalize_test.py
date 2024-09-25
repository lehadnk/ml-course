import unittest

from src.math.average import average
from src.math.stdev import stdev
from src.vector.normalize import normalize_using_min_max, normalize_using_avg_and_stdev


class NormalizeTest(unittest.TestCase):
    def test_normalize_using_min_max(self):
        v = [3, 5, 4, 1, 2]

        normalized = normalize_using_min_max(v)

        self.assertEqual([0.5, 1, 0.75, 0, 0.25], normalized)

    def test_normalize_using_avg_and_stdev(self):
        v = [3, 5, 4, 1, 2]
        print(stdev(v))
        normalized = normalize_using_avg_and_stdev(v)
        normalized_avg = average(normalized)
        normalized_stdev = stdev(normalized)
        print(normalized)

        self.assertAlmostEqual(0.0, normalized_avg, 2)
        self.assertEqual(1, normalized_stdev)