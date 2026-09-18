"""Shunting yard algoritmi ja tokenisointi."""

from collections import namedtuple

Token = namedtuple("Token", ["type", "value"])
OperatorInfo = namedtuple("operator_info", ["precedence", "associativity"])

operators = {
    "+": OperatorInfo(0, "L"),
    "-": OperatorInfo(0, "L"),
    "*": OperatorInfo(1, "L"),
    "/": OperatorInfo(1, "L"),
    "^": OperatorInfo(2, "R"),
}

functions = {"sqrt", "sin", "min", "max"}


def tokenize(expression):
    """Tokenisoi matemaattisen lausekkeen

    Args: expression (str): matemaattinen lauseke

    Returns: list: tokenisoitu lauseke"""

    tokens = []
    n = len(expression)
    i = 0

    while i < n:
        character = expression[i]

        if character == " ":
            i += 1

        elif character in set("0123456789"):
            number = ""
            while i < n and expression[i] in set("0123456789"):
                number += expression[i]
                i += 1
            tokens.append(Token("number", int(number)))

        elif character in operators:
            tokens.append(Token("operator", character))
            i += 1

        elif character == "(":
            tokens.append(Token("left_parenthesis", character))
            i += 1

        elif character == ")":
            tokens.append(Token("right_parenthesis", character))
            i += 1

        elif character.isalpha():
            function_name = ""
            while i < n and expression[i].isalnum():
                function_name += expression[i]
                i += 1
            if function_name in functions:
                tokens.append(Token("function", function_name))
            else:
                tokens.append(Token("variable", function_name))

        elif character == ",":
            tokens.append(Token("comma", character))
            i += 1

        else:
            raise ValueError(f"Virheellinen merkki: {character}")

    return tokens


def shunting_yard(tokens):
    """Muunta infix-lausekkeen postfix-muotoon shunting yard algoritmilla"""

    output_queue = []
    token_stack = []

    for token in tokens:
        if token.type == "number" or token.type == "variable":
            output_queue.append(token)

        elif token.type == "function":
            token_stack.append(token)

        elif token.type == "left_parenthesis":
            token_stack.append(token)

        elif token.type == "right_parenthesis":
            while token_stack and token_stack[-1].type != "left_parenthesis":
                output_queue.append(token_stack.pop())
            if not token_stack:
                raise ValueError("Sulut epätasapainossa")
            token_stack.pop()

        elif token.type == "operator":
            while (
                token_stack
                and token_stack[-1].type == "operator"
                and operators[token_stack[-1].value].precedence
                >= operators[token.value].precedence
            ):
                output_queue.append(token_stack.pop())
            token_stack.append(token)

    while token_stack:
        if token_stack[-1].type == "left_parenthesis":
            raise ValueError("Sulut epätasapainossa")
        output_queue.append(token_stack.pop())

    return output_queue
