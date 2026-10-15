"""Komentorivikäyttöliittymä laskimelle"""

from laskin.shunting_yard import tokenize, shunting_yard
from laskin.evaluointi import evaluate


def show_apua():
    """Tulostaa laskimen hyväksymät laskut ja komennot."""

    print("""Hyväksytyt laskut:
  1. Kokonaisluvut, esimerkiksi 2 + 3
  2. Operaattorit: +, -, *, / ja ^
  3. Sulut ja negatiiviset luvut, esimerkiksi (-2) * (3 + 4)
  4. Funktiot:
     - sin(luku), cos(luku), tan(luku) ja sqrt(luku)
     - min(luku, luku) ja max(luku, luku)
  5. Muuttujat, esimerkiksi x = 10 ja x * 2
""")


def run():
    """Käynnistää laskimen komentoriviltä"""

    variables = {}
    print(
        "Tervetuloa laskimeen! Kirjoita 'lopeta' lopettaaksesi tai 'apua' nähdäksesi sallittuja laskuja"
    )
    while True:
        expression = input("Anna lauseke:")

        if not expression.strip():
            continue

        command = expression.strip().lower()

        if command == "apua":
            show_apua()
            continue

        if command == "lopeta":
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
