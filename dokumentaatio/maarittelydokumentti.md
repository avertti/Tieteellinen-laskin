# Määrittelydokumentti

Opinto-ohjelma: (TKT) Tietojenkäsittelytieteen kandidaantti

Dokumentaation kieli: Suomi

Ohjelmointikieli: Python

## Harjoitustyön ydin

Työn ydin on matemaattisten lausekkeiden tuottaminen ja laskeminen shunting yard algoritmilla. Ytimeen kuuluu myös virheellisten lausekkeiden tunnistus ja niille virheilmoitusten luominen.

## Minkä ongelman ratkaisen

Ohjelma ratkaisee ongelman, jossa käyttäjän kirjoittama matemaattinen lauseke pitää tulkita ja laskea. Ongelma sisältää sekä oikean laskujärjestyksen, sekä virheellisten syötteiden tunnistamisen ja virheilmoituksen antaminen ennen kuin niille yritetään laskea arvoa.

## Toteutettavat algoritmit ja tietorakenteet

- Shunting yard algoritm

- Pino

## Syötteet ja niiden käyttö

- Matemaattinen lauseke, joita jäsennetään ja lasketaan

Lauseke voi sisältää:

  - lukuarvoja ja muuttujia
  - peruslaskutoimituksia 
  - yhden parametrin funktioita (sqrt, sin)
  - kahden parametrin funktioita (min, max)

- Muuttujan sijoitus, lausekkeen arvo tallennetaan muuttujaympäristöön ja on käytettävissä myöhemmin

## Tavoitteena olevat aika- ja tilavaativuudet

- Algoritmi on lineaarinen sekä ajan että tilan suhteen lausekkeen pituuteen nähden

- Aika ja tilavaativuudet ovat siis O(n)




## Lähteet

- Wikipedia: Shunting-yard algorithm (https://en.wikipedia.org/wiki/Shunting-yard_algorithm)

- https://docs.python.org/3/reference/expressions.html (6.17. Operator precedence)
