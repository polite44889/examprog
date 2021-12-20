import unittest

import ekz


class TestEkz(unittest.TestCase):
    # провіряємо що сума арифметичної прогресії при n=1, => 1
    def test_sum_1(self):
        value = ekz.arithmetic_sum(1)
        self.assertEqual(value,1)
    # провіряємо що сума арифметичної прогресії при n=2, => 4
    def test_sum_2(self):
        value = ekz.arithmetic_sum(2)
        self.assertEqual(value,4)
    # провіряємо що сума арифметичної прогресії при n=3, => 7
    def test_sum_3(self):
        value = ekz.arithmetic_sum(3)
        self.assertEqual(value,7)
    # провіряємо що сума арифметичної прогресії при n=4, => 10
    def test_sum_4(self):
        value = ekz.arithmetic_sum(4)
        self.assertEqual(value,10)
    # провіряємо що якщо n менше або = 0, то повинна бути помилка ValueError
    def test_sum_less_or_zero(self):
        self.assertRaises(ValueError, ekz.arithmetic_sum,-1)

if __name__ == '__main__':
    unittest.main()