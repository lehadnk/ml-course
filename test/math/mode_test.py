import unittest

from src.math.mode import mode


class ModeTest(unittest.TestCase):
    def test_mode(self):
        vector = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 2]
        mode_value = mode(vector)

        self.assertEqual(2, mode_value)
