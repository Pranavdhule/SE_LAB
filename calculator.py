

def add(a: float, b: float) -> float:
    return a + b

def subtract(a: float, b: float) -> float:
    return a - b

def multiply(a: float, b: float) -> float:
    return a * b

def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


import unittest
from calculator import add, subtract, multiply, divide

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)
        self.assertAlmostEqual(add(2.5, 3.5), 6.0)

    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(subtract(0, 5), -5)
        self.assertEqual(subtract(-1, -1), 0)
        self.assertAlmostEqual(subtract(5.5, 2.2), 3.3, places=1)

    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-2, 3), -6)
        self.assertEqual(multiply(0, 100), 0)
        self.assertAlmostEqual(multiply(2.5, 4), 10.0)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(-10, 2), -5)
        self.assertAlmostEqual(divide(7, 3), 2.3333, places=4)
        with self.assertRaises(ValueError):
            divide(10, 0)  # Division by zero should raise a ValueError.

if __name__ == "__main__":
    unittest.main()
