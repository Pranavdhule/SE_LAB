
class StudentGrades:
    def __init__(self):
        """Initialize an empty dictionary to store student names and grades."""
        self.grades = {}

    def add_grade(self, student: str, grade: float) -> None:
        """
        Add or update a student's grade.
        Args:
            student (str): The name of the student.
            grade (float): The grade of the student.
        """
        if not 0 <= grade <= 100:
            raise ValueError("Grade must be between 0 and 100.")
        self.grades[student] = grade

    def get_grade(self, student: str) -> float:
        """
        Get the grade of a specific student.
        Args:
            student (str): The name of the student.
        Returns:
            float: The grade of the student.
        Raises:
            KeyError: If the student is not found.
        """
        if student not in self.grades:
            raise KeyError(f"Student {student} not found.")
        return self.grades[student]

    def average_grade(self) -> float:
        """
        Compute the average grade of all students.
        Returns:
            float: The average grade.
        """
        if not self.grades:
            raise ValueError("No grades available to compute average.")
        return sum(self.grades.values()) / len(self.grades)

    def highest_grade(self) -> tuple:
        """
        Find the student with the highest grade.
        Returns:
            tuple: (student_name, grade)
        """
        if not self.grades:
            raise ValueError("No grades available.")
        student = max(self.grades, key=self.grades.get)
        return student, self.grades[student]

import unittest
from student_grade import StudentGrades

class TestStudentGrades(unittest.TestCase):

    def setUp(self):
        """Set up test data for all test methods."""
        self.grades = StudentGrades()
        self.grades.add_grade("Alice", 85)
        self.grades.add_grade("Bob", 92)
        self.grades.add_grade("Charlie", 78)

    def test_add_grade(self):
        self.grades.add_grade("Daisy", 88)
        self.assertEqual(self.grades.get_grade("Daisy"), 88)
        with self.assertRaises(ValueError):
            self.grades.add_grade("Eve", 105)  # Invalid grade

    def test_get_grade(self):
        self.assertEqual(self.grades.get_grade("Alice"), 85)
        with self.assertRaises(KeyError):
            self.grades.get_grade("Unknown")  # Student not found

    def test_average_grade(self):
        self.assertAlmostEqual(self.grades.average_grade(), (85 + 92 + 78) / 3)
        self.grades.add_grade("Daisy", 88)
        self.assertAlmostEqual(self.grades.average_grade(), (85 + 92 + 78 + 88) / 4)

    def test_highest_grade(self):
        self.assertEqual(self.grades.highest_grade(), ("Bob", 92))
        self.grades.add_grade("Eve", 95)
        self.assertEqual(self.grades.highest_grade(), ("Eve", 95))

    def test_empty_grades(self):
        empty_grades = StudentGrades()
        with self.assertRaises(ValueError):
            empty_grades.average_grade()
        with self.assertRaises(ValueError):
            empty_grades.highest_grade()

if __name__ == "__main__":
    unittest.main()
