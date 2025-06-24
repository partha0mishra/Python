# test_grade_tracker.py
import unittest
from grade_tracker import calculate_average, get_student_summary

class TestGradeTracker(unittest.TestCase):
    def test_calculate_average(self):
        self.assertEqual(calculate_average([85, 90, 88]), 87.66666666666667)
        self.assertEqual(calculate_average([]), 0)

    def test_get_student_summary(self):
        students = {"Alice": [85, 90, 88], "Bob": [78, 82, 80]}
        self.assertEqual(get_student_summary("Alice", students), ("Alice", 87.66666666666667))
        self.assertIsNone(get_student_summary("Dave", students))

if __name__ == "__main__":
    unittest.main()