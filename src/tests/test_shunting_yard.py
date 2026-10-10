"""Testaa algoritmia"""

import unittest
from laskin.shunting_yard import tokenize, shunting_yard, Token
from laskin.evaluointi import evaluate


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

    def test_cos_tan(self):
        """Testaa algoritmia cos ja tan syötteillä"""
        equation = shunting_yard(tokenize("cos(0) + tan(0)"))
        self.assertEqual(
            [token.value for token in equation],
            [0, "cos", 0, "tan", "+"],
        )

    def test_variables(self):
        """Testaa algoritmia muuttujien kanssa"""
        equation = shunting_yard(tokenize("x + y * 2"))
        self.assertEqual(
            [token.value for token in equation],
            ["x", "y", 2, "*", "+"],
        )

    def test_operator_precedence(self):
        """Testaa operaattoreiden laskujärjestyksen"""
        equation = shunting_yard(tokenize("2 + 3 * 4"))
        self.assertEqual(
            [token.value for token in equation],
            [2, 3, 4, "*", "+"],
        )

    def test_parentheses_change_precedence(self):
        """Testaa sulkeiden vaikutuksen laskujärjestykseen"""
        equation = shunting_yard(tokenize("(2 + 3) * 4"))
        self.assertEqual(
            [token.value for token in equation],
            [2, 3, "+", 4, "*"],
        )

    def test_right_associative(self):
        """Testaa potenssin oikeanpuoleisen sitovuuden"""
        equation = shunting_yard(tokenize("2 ^ 3 ^ 2"))
        self.assertEqual(
            [token.value for token in equation],
            [2, 3, 2, "^", "^"],
        )

    def test_unary_minus(self):
        """Testaa negatiivisen luvun operaattoria"""
        equation = shunting_yard(tokenize("-(2 + 3)"))
        self.assertEqual(
            [token.value for token in equation],
            [2, 3, "+", "-()"],
        )

    def test_nested_functions(self):
        """Testaa sisäkkäisiä funktioita"""
        equation = shunting_yard(tokenize("max(1, sqrt(4))"))
        self.assertEqual(
            [token.value for token in equation],
            [1, 4, "sqrt", "max"],
        )

    def test_function_errors(self):
        """Testaa virheiden käsittelyä funktioiden kanssa"""
        with self.assertRaises(ValueError):
            shunting_yard(tokenize("min(1)"))
        with self.assertRaises(ValueError):
            shunting_yard(tokenize("max(1)"))
        with self.assertRaises(ValueError):
            shunting_yard(tokenize("sqrt()"))
        with self.assertRaises(ValueError):
            shunting_yard(tokenize("sin()"))
        with self.assertRaises(ValueError):
            shunting_yard(tokenize("min(1, 2, 3)"))
        with self.assertRaises(ValueError):
            shunting_yard(tokenize("max(1, 2, 3)"))
        with self.assertRaises(ValueError):
            shunting_yard(tokenize("sqrt(1, 2)"))
        with self.assertRaises(ValueError):
            shunting_yard(tokenize("sin(1, 2)"))

    def test_parenthesis_errors(self):
        """Testaa epätasapainossa olevat sulkeet"""
        with self.assertRaises(ValueError):
            shunting_yard(tokenize("(1 + 2"))
        with self.assertRaises(ValueError):
            shunting_yard(tokenize("1 + 2)"))

    def test_expression_cannot_end_with_operator(self):
        """Testaa operaattoriin päättyvän lausekkeen"""
        with self.assertRaises(ValueError):
            shunting_yard(tokenize("1 +"))

    def test_integration(self):
        """Testaa integraatiota tokenize, shunting yard ja evaluate välillä"""

        expression = "min(3, 4) + max(1, 2) + sqrt(64) + sin(0) + 2/(3-1)"
        tokens = tokenize(expression)
        rpn_output = shunting_yard(tokens)
        result = evaluate(rpn_output, {})
        self.assertEqual(result, 14)
