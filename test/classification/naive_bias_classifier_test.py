import unittest

from src.classification.naive_bias_classifier import NaiveBiasClassifier


class NaiveBiasClassifierTest(unittest.TestCase):
    def test_naive_bias_classifier(self):
        classifier = NaiveBiasClassifier()
        classifier.fit([
            [0, 0, 0],
            [0, 0, 0],
            [0, 1, 0],
            [0, 0, 0],
            [0, 1, 1],
            [1, 0, 0],
            [1, 1, 0],
            [1, 1, 1],
            [1, 1, 1],
            [1, 1, 1],
            [1, 0, 1],
            [0, 1, 0],
        ], [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0])
        scores = classifier.get_prediction_scores([0, 0, 0])
        cls = classifier.predict([0, 0, 0])

        self.assertAlmostEqual(scores[0], 0.02, 2)
        self.assertAlmostEqual(scores[1], 0.98, 2)
        self.assertEqual(cls, 1)