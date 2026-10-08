# Pylint-raportti

Pylint antaa seuraavan raportin sovelluksen .py-tiedostoista.

```(venv) (base) wilmo@Villes-Mac-studio metapie % pylint *.py
************* Module app
app.py:1:0: C0114: Missing module docstring (missing-module-docstring)
app.py:16:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:20:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:25:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:33:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:39:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:39:16: W0613: Unused argument 'error' (unused-argument)
app.py:47:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:55:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:55:14: W0613: Unused argument 'error' (unused-argument)
app.py:63:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:63:19: W0613: Unused argument 'error' (unused-argument)
app.py:73:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:93:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:109:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:114:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:125:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:157:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:168:8: R1705: Unnecessary "else" after "return", remove the "else" and de-indent the code inside it (no-else-return)
app.py:157:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
app.py:180:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:188:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:199:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:206:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:227:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:274:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:285:8: R1705: Unnecessary "else" after "return", remove the "else" and de-indent the code inside it (no-else-return)
app.py:274:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
app.py:293:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:338:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:348:8: R1705: Unnecessary "else" after "return", remove the "else" and de-indent the code inside it (no-else-return)
************* Module config
config.py:1:0: C0114: Missing module docstring (missing-module-docstring)
config.py:1:0: C0103: Constant name "secret_key" doesn't conform to UPPER_CASE naming style (invalid-name)
************* Module db
db.py:1:0: C0114: Missing module docstring (missing-module-docstring)
db.py:4:0: C0116: Missing function or method docstring (missing-function-docstring)
db.py:10:0: C0116: Missing function or method docstring (missing-function-docstring)
db.py:10:0: W0102: Dangerous default value [] as argument (dangerous-default-value)
db.py:17:0: C0116: Missing function or method docstring (missing-function-docstring)
db.py:20:0: C0116: Missing function or method docstring (missing-function-docstring)
db.py:20:0: W0102: Dangerous default value [] as argument (dangerous-default-value)
************* Module ingredients
ingredients.py:1:0: C0114: Missing module docstring (missing-module-docstring)
ingredients.py:3:0: C0116: Missing function or method docstring (missing-function-docstring)
ingredients.py:7:0: C0116: Missing function or method docstring (missing-function-docstring)
ingredients.py:11:0: C0116: Missing function or method docstring (missing-function-docstring)
ingredients.py:19:0: C0116: Missing function or method docstring (missing-function-docstring)
ingredients.py:26:0: C0116: Missing function or method docstring (missing-function-docstring)
ingredients.py:30:0: W0105: String statement has no effect (pointless-string-statement)
************* Module recipes
recipes.py:1:0: C0114: Missing module docstring (missing-module-docstring)
recipes.py:3:0: C0116: Missing function or method docstring (missing-function-docstring)
recipes.py:10:8: R1704: Redefining argument with the local name 'title' (redefined-argument-from-local)
recipes.py:14:0: C0116: Missing function or method docstring (missing-function-docstring)
recipes.py:19:0: C0116: Missing function or method docstring (missing-function-docstring)
recipes.py:40:0: C0116: Missing function or method docstring (missing-function-docstring)
recipes.py:50:0: C0116: Missing function or method docstring (missing-function-docstring)
recipes.py:54:0: C0116: Missing function or method docstring (missing-function-docstring)
recipes.py:66:0: C0116: Missing function or method docstring (missing-function-docstring)
recipes.py:75:8: R1704: Redefining argument with the local name 'title' (redefined-argument-from-local)
recipes.py:78:0: C0116: Missing function or method docstring (missing-function-docstring)
recipes.py:82:0: C0116: Missing function or method docstring (missing-function-docstring)
************* Module seed
seed.py:1:0: C0114: Missing module docstring (missing-module-docstring)
seed.py:11:0: C0103: Constant name "user_count" doesn't conform to UPPER_CASE naming style (invalid-name)
seed.py:12:0: C0103: Constant name "recipe_count" doesn't conform to UPPER_CASE naming style (invalid-name)
seed.py:13:0: C0103: Constant name "votes_per_recipe" doesn't conform to UPPER_CASE naming style (invalid-name)
************* Module users
users.py:1:0: C0114: Missing module docstring (missing-module-docstring)
users.py:5:0: C0116: Missing function or method docstring (missing-function-docstring)
users.py:10:0: C0116: Missing function or method docstring (missing-function-docstring)
users.py:20:0: C0116: Missing function or method docstring (missing-function-docstring)
users.py:25:0: C0116: Missing function or method docstring (missing-function-docstring)
users.py:29:0: C0116: Missing function or method docstring (missing-function-docstring)
************* Module votes
votes.py:1:0: C0114: Missing module docstring (missing-module-docstring)
votes.py:3:0: C0116: Missing function or method docstring (missing-function-docstring)
votes.py:7:0: C0116: Missing function or method docstring (missing-function-docstring)
votes.py:16:0: C0116: Missing function or method docstring (missing-function-docstring)
votes.py:20:0: C0116: Missing function or method docstring (missing-function-docstring)
votes.py:24:0: C0116: Missing function or method docstring (missing-function-docstring)

------------------------------------------------------------------
Your code has been rated at 8.07/10 (previous run: 7.95/10, +0.12)
```

Käydään raportin sisältö läpi ja perustellaan, miksi kyseisiä asioita ei ole korjattu sovelluksessa.

## Docstring-ilmoitukset

Suurin osa raportin ilmoituksista on seuraavan kaltaisia:
```app.py:1:0: C0114: Missing module docstring (missing-module-docstring)
app.py:16:0: C0116: Missing function or method docstring (missing-function-docstring)
```
Sovelluksen kehityksessä on seurattu mallisovelluksen päätöstä, jossa moduuleihin ja funktioihin ei ole docstring-kommentteja.

## Tarpeeton else

Raportissa on seuraavat else-haaroihin liittyvät ilmoitukset:

```app.py:168:8: R1705: Unnecessary "else" after "return", remove the "else" and de-indent the code inside it (no-else-return)
app.py:285:8: R1705: Unnecessary "else" after "return", remove the "else" and de-indent the code inside it (no-else-return)
app.py:348:8: R1705: Unnecessary "else" after "return", remove the "else" and de-indent the code inside it (no-else-return)
```
Jokaisessa tapauksessa kyseessä on koodin selkeyden takia tehty päätös, jossa if-else tuo esiin selkeämmin koodin kaksi vaihtoehtoa toiminnalle.

## Puuttuva palautusarvo

```app.py:157:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
app.py:274:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
```
Kyseiset ilmoitukset johtuvat siitä, että funktiossa on sekä GET että POST. Käytännössä muun laiset request.methodit eivät ole mahdollisia, koska funktion dekoraattorissa on vaatimuksena että metodi on joko GET tai POST.

## Vakion nimi

```config.py:1:0: C0103: Constant name "secret_key" doesn't conform to UPPER_CASE naming style (invalid-name)
seed.py:11:0: C0103: Constant name "user_count" doesn't conform to UPPER_CASE naming style (invalid-name)
seed.py:12:0: C0103: Constant name "recipe_count" doesn't conform to UPPER_CASE naming style (invalid-name)
seed.py:13:0: C0103: Constant name "votes_per_recipe" doesn't conform to UPPER_CASE naming style (invalid-name)
```
Tässä koodin päätasolla määritelty muuttuja tulkitaan vakioksi, jonka nimen tulisi olla kirjoitettu suurilla kirjaimilla. Kuitenkin esimerkkisovelluksen kehittäjän näkemyksen mukaan tässä tilanteessa näyttää paremmalta, että muuttujan nimi on pienillä kirjaimilla.

seed.py puolestaan toimii lähinnä apufunktiona suuren tietomäärän luomiseksi tietokantaan, jolloin sovelluksen kehittäjän näkemyksen mukaan näyttää paremmalta, kun ne ovat pienillä kirjaimilla.

## Vaarallinen oletusarvo

```db.py:10:0: W0102: Dangerous default value [] as argument (dangerous-default-value)
db.py:20:0: W0102: Dangerous default value [] as argument (dangerous-default-value)
```
Esimerkiksi ensimmäinen ilmoitus koskee seuraavaa funktiota:
```def execute(sql, params=[]):
    con = get_connection()
    result = con.execute(sql, params)
    con.commit()
    g.last_insert_id = result.lastrowid
    con.close()
```
Tässä parametrin oletusarvo [] on tyhjä lista. Tässä ongelmaksi voisi tulla, että sama oletusarvona oleva tyhjä listaolio on jaettu kaikkien funktion kutsujen kesken ja jos jossain kutsussa listan sisältöä muutettaisiin, tämä muutos näkyisi myös muihin kutsuihin. Käytännössä tässä tapauksessa tämä ei kuitenkaan haittaa, koska koodi ei muuta listaoliota.

## Käyttämättömät argumentit

Raportissa on seuraavat ilmoitukset käyttämättömistä argumenteista:

```app.py:39:16: W0613: Unused argument 'error' (unused-argument)
app.py:55:14: W0613: Unused argument 'error' (unused-argument)
app.py:63:19: W0613: Unused argument 'error' (unused-argument)
```
Kaikki kolme kohtaa käsittelevät sovelluksen virheilmoituksia, esimerkkinä:

```@app.errorhandler(404)
def not_found(error):
    return render_template(
        "error.html",
        title="Sivua ei löytynyt",
        message="Hakemaasi sivua tai reseptiä ei ole olemassa."
    ), 404
```

Ilmoitukset koskevat 400, 403 ja 500-virheilmoituksien käsittelyä. Nykyisellään sovelluksella ei ole tarvetta useammille ilmoituksille näissä tapauksissa. Virheilmoitusten laajennettavuutta varten säilytetään kuitenkin mahdollisuus tuoda näillekkin virheilmoituksille omat error-messaget.