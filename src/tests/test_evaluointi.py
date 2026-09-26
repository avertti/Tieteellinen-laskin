"""Testaa evaluointia"""

import unittest
from laskin.shunting_yard import tokenize, shunting_yard
from laskin.evaluointi import evaluate


class TestEvaluointi(unittest.TestCase):
    """Testaa evaluointia"""

    def calculate(self, expression, variables=None):
        """Funktio joka laskee lausekkeen"""
        return evaluate(shunting_yard(tokenize(expression)), variables or {})

    def test_evaluate(self):
        """Testaa eri laskutoimituksia"""
        self.assertEqual(self.calculate(" 1 + 1 "), 2)
        self.assertEqual(self.calculate(" 2 - 1 "), 1)
        self.assertEqual(self.calculate(" 2 * 3 "), 6)
        self.assertEqual(self.calculate(" 4 / 2 "), 2)
        self.assertEqual(self.calculate(" 2 ^ 3 "), 8)

    def test_variables(self):
        """Testaa muuttujien käyttöä"""
        variables = {"x": 2, "y": 3}
        self.assertEqual(self.calculate(" x ", variables), 2)
        self.assertEqual(self.calculate(" y ", variables), 3)
        self.assertEqual(self.calculate(" x + y ", variables), 5)

    def test_functions(self):
        """Tesataa funtkioiden käyttöä"""
        self.assertEqual(self.calculate(" sqrt(4) "), 2)
        self.assertEqual(self.calculate(" sin(0) "), 0)
        self.assertEqual(self.calculate(" min(1, 2) "), 1)
        self.assertEqual(self.calculate(" max(1, 2) "), 2)

    def test_errors(self):
        """Testaa virheiden käsittelyä"""
        with self.assertRaises(ValueError):
            self.calculate(" x + 1 ")


if __name__ == "__main__":
    unittest.main()
