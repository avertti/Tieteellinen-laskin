"""Komentorivikäyttöliittymä laskimelle"""

from laskin.shunting_yard import tokenize, shunting_yard
from laskin.evaluointi import evaluate


def run():
    """Käynnistää laskimen komentoriviltä"""

    variables = {}
    print("Tervetuloa laskimeen! Kirjoita 'lopeta' lopettaaksesi")
    while True:
        expression = input("Anna lauseke:")

        if not expression.strip():
            continue

        if expression.lower() == "lopeta":
            break

        try:
            tokens = tokenize(expression)

            if (
                len(tokens) > 2
                and tokens[0].type == "variable"
                and tokens[1].type == "equal_sign"
            ):
                variable_name = tokens[0].value
                varible_value = evaluate(shunting_yard(tokens[2:]), variables)
                variables[variable_name] = varible_value
                print(f"{variable_name} = {varible_value}")
            else:
                print(evaluate(shunting_yard(tokens), variables))

        except ValueError as e:
            print(f"Virhe: {e}")


if __name__ == "__main__":
    run()
