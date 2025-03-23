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

    def test_max_limit(self): # Check that it works for 100 which is the max value
        expected = 93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000
        self.assertEqual(factorial(100),expected)

if __name__ == "__main__":
    unittest.main()