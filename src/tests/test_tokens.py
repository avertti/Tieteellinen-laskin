"""Testaa tokenisointia"""

import unittest
from laskin.shunting_yard import tokenize, Token, shunting_yard


class TestTokenize(unittest.TestCase):
    """Testaa tokenize-funktiota"""

    def test_tokenize(self):
        """Testaa tokenisointia matemaattiselle lausekkeelle"""
        expression = "3 + 4 * 2 / ( 1 - 5 ) ^ 2"
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
        """Testaa funktioiden tokenisoinnin"""
        expression = "sqrt(4) + sin(0) + cos(0) + tan(0)"
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
            Token("operator", "+"),
            Token("function", "cos"),
            Token("left_parenthesis", "("),
            Token("number", 0),
            Token("right_parenthesis", ")"),
            Token("operator", "+"),
            Token("function", "tan"),
            Token("left_parenthesis", "("),
            Token("number", 0),
            Token("right_parenthesis", ")"),
        ]
        self.assertEqual(tokenize(expression), expected_tokens)

    def test_min_max_tokens(self):
        """Testaa min ja max funktioiden tokenisoinnin"""
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
        """Testaa muuttujien tokenisoinnin"""
        expression = "x + y * 2"
        expected_tokens = [
            Token("variable", "x"),
            Token("operator", "+"),
            Token("variable", "y"),
            Token("operator", "*"),
            Token("number", 2),
        ]
        self.assertEqual(tokenize(expression), expected_tokens)

    def test_equal_sign_tokens(self):
        """Testaa yhtäsuuruusmerkin tokenisoinit"""
        expression = "x = 5"
        expected_tokens = [
            Token("variable", "x"),
            Token("equal_sign", "="),
            Token("number", 5),
        ]
        self.assertEqual(tokenize(expression), expected_tokens)

    def test_paranthesis_error_left(self):
        """Testaa epeätasapoinsten sulkuje käsittelyn"""
        expression = "(3 * 2"
        with self.assertRaises(ValueError):
            shunting_yard(tokenize(expression))

    def test_paranthesis_error_right(self):
        """Testaa epeätasapoinsten sulkuje käsittelyn"""
        expression = "3 * 2)"
        with self.assertRaises(ValueError):
            shunting_yard(tokenize(expression))

    def test_comma_error(self):
        """Testaa virheellisen pilkun käsittelyn"""
        with self.assertRaises(ValueError):
            shunting_yard(tokenize("1 + 1, 2"))

    def test_minus_errors(self):
        """Testaa virheellisen miinusmerkin käsittelyn"""
        with self.assertRaises(ValueError):
            shunting_yard(tokenize("3 + - 2"))
        with self.assertRaises(ValueError):
            tokenize("2 + -2")
        with self.assertRaises(ValueError):
            shunting_yard(tokenize("3 + (-) 2"))
        with self.assertRaises(ValueError):
            shunting_yard(tokenize("3--2"))
        with self.assertRaises(ValueError):
            shunting_yard(tokenize("- -3 + 2"))

    def test_operator_errors(self):
        """Testaa virheellisen operaattorin käsittelyn"""
        with self.assertRaises(ValueError):
            shunting_yard(tokenize("+ 3 + 2"))
        with self.assertRaises(ValueError):
            shunting_yard(tokenize("3 + * 2"))
        with self.assertRaises(ValueError):
            shunting_yard(tokenize("3 / "))
        with self.assertRaises(ValueError):
            shunting_yard(tokenize("3 + (^) 2"))
        with self.assertRaises(ValueError):
            shunting_yard(tokenize("3 + 2 -"))
        with self.assertRaises(ValueError):
            shunting_yard(tokenize("2(3)"))

    def test_missing_operator(self):
        """Testaa puuttuvan operaattorin käsittelyä"""
        with self.assertRaises(ValueError):
            shunting_yard(tokenize("3 2 + 1"))
