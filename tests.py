import unittest

from mymathlib import is_prime


class IsPrimeTests(unittest.TestCase):
    def test_zero(self):
        self.assertFalse(is_prime(0))


    def test_one(self):
        self.assertFalse(is_prime(1))


    def test_two(self):
        self.assertTrue(is_prime(2))


    def test_three(self):
        self.assertTrue(is_prime(3))


    def test_four(self):
        self.assertFalse(is_prime(4))


    def test_eight(self):
        self.assertFalse(is_prime(8))


    def test_nine(self):
        self.assertFalse(is_prime(9))


if __name__ == "__main__":
    unittest.main()
