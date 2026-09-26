"""Laskee lausekkeen arvon"""

import math


def evaluate(rpn_output, variables):
    """Laskee lausekkeen arvon

    Args: rpn_output: shunting yardin tuottama lista
    variables: sanakirja, jossa on muuttujien arvot

    Returns: lausekkeen arvo"""

    stack = []

    for token in rpn_output:
        if token.type == "number":
            stack.append(token.value)

        elif token.type == "operator":
            b = stack.pop()
            a = stack.pop()
            if token.value == "+":
                stack.append(a + b)
            elif token.value == "-":
                stack.append(a - b)
            elif token.value == "*":
                stack.append(a * b)
            elif token.value == "/":
                stack.append(a / b)
            elif token.value == "^":
                stack.append(a**b)

        elif token.type == "function":
            if token.value == "sin" or token.value == "sqrt":
                a = stack.pop()
                if token.value == "sin":
                    stack.append(math.sin(a))
                elif token.value == "sqrt":
                    stack.append(math.sqrt(a))
            elif token.value == "max" or token.value == "min":
                b = stack.pop()
                a = stack.pop()
                if token.value == "max":
                    stack.append(max(a, b))
                elif token.value == "min":
                    stack.append(min(a, b))

        elif token.type == "variable":
            if token.value not in variables:
                raise ValueError(f"Muuttujaa {token.value} ei ole määritelty")
            stack.append(variables[token.value])

    return stack[0]
