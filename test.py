# test_main.py
import unittest
from main import generate_matrix  # Імпортуємо функцію з main.py
import numpy as np

class TestGenerateMatrix(unittest.TestCase):

    # Тест на коректний розмір
    def test_valid_input(self):
        matrix = generate_matrix(3)
        self.assertEqual(matrix.shape, (3, 3))  # Перевіряємо, що матриця має розмір 3x3

    # Тест на від'ємне значення
    def test_negative_input(self):
        with self.assertRaises(ValueError):
            generate_matrix(-5)

    # Тест на нульовий розмір
    def test_zero_input(self):
        with self.assertRaises(ValueError):
            generate_matrix(0)

    # Тест на неціле число
    def test_non_integer_input(self):
        with self.assertRaises(ValueError):
            generate_matrix(2.5)

    # Тест на строкове значення
    def test_string_input(self):
        with self.assertRaises(ValueError):
            generate_matrix("три")

if __name__ == "__main__":
    unittest.main()
