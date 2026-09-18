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
