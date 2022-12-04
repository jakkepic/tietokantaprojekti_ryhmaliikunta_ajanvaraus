# Ryhmäliikunnan ilmoittautumissovellus

Projektityönäni teen sovelluksen 
jossa voi ilmoittautua ryhmäliikuntavuoroihin.

### Tavoitteet:
- Käyttäjä voi luoda tunnuksen ja kirjautua
- Käyttäjä pystyy ilmoitttautumaan ryhmään
- Käyttäjillä voi olla perusoikeudet tai adminrooli
- Admin pystyy luomaan uuden ryhmän
- Ohjelma varmistaa että ryhmään ei ilmoittaudu enemmän osallistujia kun mitä mahtuu liikuntasaliin
- Ohjelma pitää huolen ettei sama käyttäjä ilmoittaudu kahdesti samaan ryhmään

### Nykyinen toiminnallisuus:
Sovellus on vielä hyvin keskeneräinen, mutta sovellusta voi kokeilla paikallisesti flaskin avulla, tai fly.io:lla.

Tällä hetkellä sovelluksessa toimii:
- Kirjautuminen ja tunnuksen luominen


### Testaaminen:
Tällä hetkellä sovellusta voi testata flaskin avulla
1. Tarkista riippuvuudet
2. Avaa postgresql-tietokanta (avaa terminaali ja syötä komento "psql")
3. Avaa sovellus terminaalissa
4. Syötä komento "psql < schema.sql"
5. Käynnistä komennolla flask run