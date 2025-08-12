import unittest

from src.classification.knn_classifier import KnnClassifier
from src.distance.euclid import EuclideanDistanceCalculator


class KnnClassifierTest(unittest.TestCase):
    def test_knn_classifier(self):
        k = KnnClassifier(EuclideanDistanceCalculator(), 5)
        k.add([-1, 0], "1")
        k.add([1, 2], "0")
        k.add([2, -2], "0")
        k.add([-3, -1], "1")
        k.add([3, 2], "1")

        self.assertEqual('1', k.classify([0, 0]))