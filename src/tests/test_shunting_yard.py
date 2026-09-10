"""Testaa tokenisointia"""

import unittest
from laskin.shunting_yard import tokenize, Token


class TestTokenize(unittest.TestCase):
    """Testaa tokenize-funktiota"""

    def test_tokenize(self):
        """Testaa tokenisointia matemaattiselle lausekkeelle"""
        expression = "3 + 4 * 2 / ( 1 - 5 ) ^ 2 ^ 3"
        expected_tokens = [
            Token("number", 3),
            Token("operator", "+"),
            Token("number", 4),
            Token("operator", "*"),
            Token("number", 2),
            Token("operator", "/"),
            Token("left_parenthesis", "("),
            Token("number", 1),
            Token("operator", "-"),
            Token("number", 5),
            Token("right_parenthesis", ")"),
            Token("operator", "^"),
            Token("number", 2),
            Token("operator", "^"),
            Token("number", 3),
        ]
        self.assertEqual(tokenize(expression), expected_tokens)

    def test_multiple_digit_numbers(self):
        """Testaa tokenisointia useamman numeron luvuilla"""
        expression = "12 + 34 * 56"
        expected_tokens = [
            Token("number", 12),
            Token("operator", "+"),
            Token("number", 34),
            Token("operator", "*"),
            Token("number", 56),
        ]
        self.assertEqual(tokenize(expression), expected_tokens)

    def test_invalid_character(self):
        """Testaa virheellisen merkin käsittelyä"""
        expression = "3 + 4 - $"
        with self.assertRaises(ValueError):
            tokenize(expression)

    def test_function_tokens(self):
        """Testaa funktioiden tokenisointi"""
        expression = "sqrt(4) + sin(0)"
        expected_tokens = [
            Token("function", "sqrt"),
            Token("left_parenthesis", "("),
            Token("number", 4),
            Token("right_parenthesis", ")"),
            Token("operator", "+"),
            Token("function", "sin"),
            Token("left_parenthesis", "("),
            Token("number", 0),
            Token("right_parenthesis", ")"),
        ]
        self.assertEqual(tokenize(expression), expected_tokens)

    def test_min_max_tokens(self):
        """Testaa min ja max funktioiden tokenisointi"""
        expression = "min(1,2) + max(1,2)"
        expected_tokens = [
            Token("function", "min"),
            Token("left_parenthesis", "("),
            Token("number", 1),
            Token("comma", ","),
            Token("number", 2),
            Token("right_parenthesis", ")"),
            Token("operator", "+"),
            Token("function", "max"),
            Token("left_parenthesis", "("),
            Token("number", 1),
            Token("comma", ","),
            Token("number", 2),
            Token("right_parenthesis", ")"),
        ]
        self.assertEqual(tokenize(expression), expected_tokens)

    def test_variable_tokens(self):
        """Testaa muuttujien tokenisointi"""
        expression = "x + y * 2"
        expected_tokens = [
            Token("variable", "x"),
            Token("operator", "+"),
            Token("variable", "y"),
            Token("operator", "*"),
            Token("number", 2),
        ]
        self.assertEqual(tokenize(expression), expected_tokens)
