# Testausdokumentti



## Kattavuus raportti

![alt text](coverage_2.png)

## Yksikkö testaus

Algoritmin toiminta on testattu perus syötteillä. Laskeminen on testattu peruslaskutoimituksilla (+,-,*,/) ja min, max, sqrt ja sin funktioilla. Muuttujaan arvon sijoittaminen on testattu myös. Tokenisointi on testattu kaikille mahdollisille syötteille. Eri virhe tapauksia on myös testattu.

## Testien toistaminen

Testit voi suorittaa komenolla:

poetry run pytest -v