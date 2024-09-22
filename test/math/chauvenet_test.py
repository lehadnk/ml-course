import unittest

from src.math.chauvenet import chauvenet_filter


class ChauvenetTest(unittest.TestCase):
    def test_chauvenet(self):
        vector = [8.02, 8.16, 3.97, 8.64, 0.84, 4.46, 0.81, 7.74, 8.78, 9.26, 20.46, 29.87, 10.38, 25.71]
        result = chauvenet_filter(vector)

        self.assertEquals(result, [8.02, 8.16, 8.64, 8.78])
