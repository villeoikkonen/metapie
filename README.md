# Metapie - reseptikirja mikä vähentää waifun metatyötä. Happy wife, happy life.

*  Sovelluksessa käyttäjät pystyvät jakamaan ruokareseptejään.
*  (TODO) Resepteihin pystyy lisäämään raaka-aineita.
*  Käyttäjä pystyy luomaan tunnuksen ja kirjautumaan sisään sovellukseen.
*  Käyttäjä pystyy lisäämään reseptejä ja muokkaamaan ja poistamaan niitä.
*  Käyttäjä näkee sovellukseen lisätyt reseptit.
*  Käyttäjä pystyy etsimään reseptejä hakusanalla.
*  Käyttäjä pystyy valitsemaan esimerkiksi seuraavia luokitteluja:
    Ruoan tyyppi: alkuruoka, pääruoka tai jälkiruoka
    Ruokavalio: laktoositon, gluteeniton, vegaaninen tai halal
*  (TODO) Käyttäjä pystyy luomaan viikottaisen ruokalistan.
*  Käyttäjä voi tykätä resepteistä.
*  (TODO) Käyttäjä saa ruokalistan perusteella itselleen kauppalistan tarvittavista aineksista.

## Asennus ja käynnistys

Tarvitset Python 3:n, Gitin ja SQLite3:n. Alla olevat komennot
on tarkoitettu Linuxille ja macOS:lle.

### 1. Lataa projekti

```bash
git clone https://github.com/villeoikkonen/metapie.git
cd metapie
```

### 2. Luo ja aktivoi virtuaaliympäristö

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Asenna Flask

```bash
python -m pip install flask
```

### 4. Luo tietokanta

Suorita tämä vain ensimmäisellä asennuskerralla:

```bash
sqlite3 database.db < schema.sql
sqlite3 database.db < init.sql
```

### 5. Käynnistä sovellus

```bash
python -m flask run
```

Avaa selaimessa http://127.0.0.1:5000.
Luo käyttäjätunnus ja kirjaudu sisään, niin voit lisätä reseptejä.

Sammuta sovellus painamalla päätteessä Ctrl+C.

### Käynnistäminen myöhemmin

Siirry projektin kansioon ja suorita:

```bash
source .venv/bin/activate
python -m flask run
```

## Sovelluksen testaaminen

1. Luo käyttäjätunnus ja kirjaudu sisään.
2. Lisää resepti ja valitse sille ruokavalio ja ruokalaji.
3. Kokeile reseptin hakemista, muokkaamista ja käyttäjäsivun avaamista.
4. Kirjaudu ulos ja luo toinen käyttäjätunnus.
5. Arvioi ensimmäisen käyttäjän resepti tykkäykseksi tai inhokiksi.
6. Tarkista reseptin arviomäärät ja oman käyttäjäsivusi tilastot.
7. Kokeile arvion poistamista.
8. Kirjaudu alkuperäisellä tunnuksella ja kokeile reseptin poistamista.