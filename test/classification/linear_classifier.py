import unittest

from src.classification.linear_classifier import LinearClassifier


class LinearClassifierTest(unittest.TestCase):
    def test_linear_classifier(self):
        X = [[-2], [-1], [0], [1], [2]]
        y = [-1, 1, -1, 1, 1]

        clf = LinearClassifier()
        clf.fit(X, y)
        self.assertEqual(-1, clf.predict([-2]))