import unittest

import ekz

class TestEkz(unittest.TestCase):

    def test_sum_1(self):
        value = ekz.arithmetic_sum(1)
        self.assertEqual(value,1)
    def test_sum_2(self):
        value = ekz.arithmetic_sum(2)
        self.assertEqual(value,4)
    def test_sum_3(self):
        value = ekz.arithmetic_sum(3)
        self.assertEqual(value,7)
    def test_sum_4(self):
        value = ekz.arithmetic_sum(4)
        self.assertEqual(value,10)
    def test_sum_less_or_zero(self):
        self.assertRaises(ValueError, ekz.arithmetic_sum,-1)

if __name__ == '__main__':
    unittest.main()