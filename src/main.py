"""Komentorivikäyttöliittymä laskimelle"""

from laskin.shunting_yard import tokenize, shunting_yard
from laskin.evaluointi import evaluate


def run():
    """Käynnistää laskimen komentoriviltä"""

    print("Tervetuloa laskimeen! Kirjoita 'lopeta' lopettaaksesi")
    while True:
        expression = input("Anna lauseke:")

        if expression.lower() == "lopeta":
            break

        try:
            tokens = tokenize(expression)
            print(evaluate(shunting_yard(tokens), {}))
        except ValueError as e:
            print(f"Virhe: {e}")


if __name__ == "__main__":
    run()
