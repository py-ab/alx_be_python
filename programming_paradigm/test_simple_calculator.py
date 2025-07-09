#!/usr/bin/python3
"""
Unit tests for the SimpleCalculator class.
"""

import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    """
    Test cases for the SimpleCalculator class.
    """

    def setUp(self):
        """
        Set up the SimpleCalculator instance before each test.
        """
        self.calc = SimpleCalculator()

    def test_addition(self):
        """
        Test the addition method.
        """
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-1, -1), -2)
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(100, 50), 150)

    def test_subtraction(self):
        """
        Test the subtraction method.
        """
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(3, 5), -2)
        self.assertEqual(self.calc.subtract(0, 0), 0)
        self.assertEqual(self.calc.subtract(10, -5), 15)
        self.assertEqual(self.calc.subtract(-5, 10), -15)

    def test_multiplication(self):
        """
        Test the multiplication method.
        """
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-1, 5), -5)
        self.assertEqual(self.calc.multiply(0, 10), 0)
        self.assertEqual(self.calc.multiply(-2, -3), 6)
        self.assertEqual(self.calc.multiply(10, 10), 100)

    def test_division(self):
        """
        Test the division method.
        """
        self.assertEqual(self.calc.divide(6, 2), 3)
        self.assertEqual(self.calc.divide(10, 5), 2)
        self.assertEqual(self.calc.divide(-10, 2), -5)
        self.assertEqual(self.calc.divide(5, -1), -5)
        self.assertEqual(self.calc.divide(0, 5), 0)

    def test_division_by_zero(self):
        """
        Test the division method with division by zero.
        """
        self.assertIsNone(self.calc.divide(5, 0))
        self.assertIsNone(self.calc.divide(0, 0))
