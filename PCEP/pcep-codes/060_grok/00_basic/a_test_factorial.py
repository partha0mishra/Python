# test_factorial.py
import unittest
from a_factorial import factorial  # Import the function to test

class TestFactorial(unittest.TestCase):
    def test_positive_number(self):
        self.assertEqual(factorial(5), 120)  # 5! = 5 * 4 * 3 * 2 * 1 = 120
        self.assertEqual(factorial(3), 6)    # 3! = 3 * 2 * 1 = 6

    def test_zero(self):
        self.assertEqual(factorial(0), 1)    # 0! is defined as 1

    def test_negative_number(self):
        self.assertEqual(factorial(-1), "Factorial not defined for negative numbers")

if __name__ == "__main__":
    unittest.main()