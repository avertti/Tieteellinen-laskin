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

        elif token.type == "operator" and token.value == "-()":
            a = stack.pop()
            stack.append(-a)

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
                if b == 0:
                    raise ValueError("Nollalla jakaminen ei ole sallittua")
                stack.append(a / b)
            elif token.value == "^":
                stack.append(a**b)

        elif token.type == "function":
            if token.value in {"sin", "cos", "tan", "sqrt"}:
                if len(stack) < 1:
                    raise ValueError("Funktio tarvitsee yhden argumentin")
                a = stack.pop()
                if token.value == "sin":
                    stack.append(math.sin(a))
                elif token.value == "cos":
                    stack.append(math.cos(a))
                elif token.value == "tan":
                    stack.append(math.tan(a))
                elif token.value == "sqrt":
                    stack.append(math.sqrt(a))

            elif token.value == "max" or token.value == "min":
                if len(stack) < 2:
                    raise ValueError("Funktio tarvitsee kaksi argumenttia")
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
