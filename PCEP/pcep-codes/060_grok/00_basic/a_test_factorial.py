# test_factorial.py
import unittest
from a_factorial import factorial

class TestFactorial(unittest.TestCase):
    def test_positive_number(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(3), 6)

    def test_zero(self):
        self.assertEqual(factorial(0), 1)

    def test_negative_number(self):
        self.assertIsNone(factorial(-1))

    def test_one(self):
        self.assertEqual(factorial(1), 1)

    def test_too_large(self):  # New test case
        with self.assertRaises(ValueError):
            factorial(101)

if __name__ == "__main__":
    unittest.main()