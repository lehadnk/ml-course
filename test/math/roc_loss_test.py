import unittest

from src.math.roc_loss import roc_loss, roc_auc_score


class RocLossTest(unittest.TestCase):
    def test_mode(self):
        ys = [0, 0, 0, 1, 1, 1, 0]
        ps = [0.5, 0.1, 0.2, 0.6, 0.2, 0.3, 0.0]

        roc = roc_loss(ys, ps)
        self.assertEqual(roc, [[1, 0], [1, 1], [2, 1], [3, 2], [3, 3], [3, 4]])
        self.assertAlmostEqual(roc_auc_score(ys, ps), 0.79, 2)