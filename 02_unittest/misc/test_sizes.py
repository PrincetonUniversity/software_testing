import unittest
import sizes

class TestThresholds(unittest.TestCase):

    def setUp(self):
        self.b = sizes.Big(85)
        self.m = sizes.Medium(33)
        self.s = sizes.Small(33)

    def test_thres(self):
        self.assertTrue(self.b.check())
        self.assertTrue(self.m.check())
        self.assertFalse(self.s.check())
