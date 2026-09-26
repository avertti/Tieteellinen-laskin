"""Testaa algoritmia"""

import unittest
from laskin.shunting_yard import tokenize, shunting_yard, Token


class TestShuntingYard(unittest.TestCase):
    """Testaa shunting yard algoritmia"""

    def test_shunting_yard(self):
        """Testaa algoritmia +,-,*,/ ja () syötteillä"""
        equation = shunting_yard(tokenize("3 + 4 * 2 / (3 - 1)"))
        self.assertEqual(
            [token.value for token in equation],
            [3, 4, 2, "*", 3, 1, "-", "/", "+"],
        )

    def test_functions(self):
        """Testaa algoritmia min,max ja sqrt syötteillä"""
        equation = shunting_yard(tokenize("min(3, 4) + max(1, 2) + sqrt(64) + sin(0)"))
        self.assertEqual(
            [token.value for token in equation],
            [3, 4, "min", 1, 2, "max", "+", 64, "sqrt", "+", 0, "sin", "+"],
        )
