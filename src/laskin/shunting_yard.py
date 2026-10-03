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
    "-()": OperatorInfo(3, "R"),
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

        # negatiivisten lukujen tokenisointi
        elif character == "-":

            if not tokens or tokens[-1].type in {
                "operator",
                "left_parenthesis",
                "comma",
                "equal_sign",
            }:
                i += 1

                while i < n and expression[i] == " ":
                    i += 1

                if i < n and expression[i] == "-":
                    raise ValueError("Kaksi peräkkäistä miinusmerkkiä ilman sulkuja")

                if i < n and expression[i] in set("0123456789"):
                    number = "-"

                    while i < n and expression[i] in set("0123456789"):
                        number += expression[i]
                        i += 1
                    tokens.append(Token("number", int(number)))

                elif i < n and expression[i] == "(" or expression[i].isalpha():
                    tokens.append(Token("operator", "-()"))

                else:
                    raise ValueError("Virheellinen merkki miinusluvun jälkeen")

            else:
                if i + 1 < n and expression[i + 1] == "-":
                    raise ValueError("Kaksi peräkkäistä miinusmerkkiä ilman sulkuja")

                tokens.append(Token("operator", "-"))
                i += 1

        elif character in operators:
            if not tokens or tokens[-1].type in {
                "operator",
                "left_parenthesis",
                "comma",
                "equal_sign",
            }:
                raise ValueError(f"Operaattori {character} virheellisessä paikassa")
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

        elif character == "=":
            tokens.append(Token("equal_sign", character))
            i += 1

        else:
            raise ValueError(f"Virheellinen merkki: {character}")

    return tokens


def shunting_yard(tokens):
    """Muunta infix-lausekkeen postfix-muotoon shunting yard algoritmilla"""

    if tokens and tokens[-1].type == "operator":
        raise ValueError("Lauseke ei voi päättyä operaattoriin")

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
            if token_stack and token_stack[-1].type == "function":
                output_queue.append(token_stack.pop())

        elif token.type == "operator":
            while (
                token_stack
                and token_stack[-1].type == "operator"
                and (
                    operators[token_stack[-1].value].precedence
                    > operators[token.value].precedence
                    or (
                        operators[token_stack[-1].value].precedence
                        == operators[token.value].precedence
                        and operators[token.value].associativity == "L"
                    )
                )
            ):
                output_queue.append(token_stack.pop())
            token_stack.append(token)

        elif token.type == "comma":
            while token_stack and token_stack[-1].type != "left_parenthesis":
                output_queue.append(token_stack.pop())
            if not token_stack:
                raise ValueError("Pilkku virheellisessä paikassa")

    while token_stack:
        if token_stack[-1].type == "left_parenthesis":
            raise ValueError("Sulut epätasapainossa")
        output_queue.append(token_stack.pop())

    return output_queue
