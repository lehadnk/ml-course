import unittest

from src.classification.gini_classification_tree import GiniClassificationTree


class GiniClassificationTreeTest(unittest.TestCase):
    def test_classification(self):
        classifier = GiniClassificationTree()
        classifier.fit([
            [1, 1, 1, 1],
            [1, 1, 1, 0],
            [1, 1, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 0, 0],
            [0, 1, 0, 1],
            [1, 0, 1, 1],
        ], [0, 1, 0, 1, 0, 1, 0])
        cls = classifier.predict([0, 1, 1, 0])
        self.assertEquals(cls, 1)

        cls = classifier.predict([1, None, 1, 0])
        self.assertEquals(cls, 0)