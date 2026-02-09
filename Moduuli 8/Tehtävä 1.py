import mysql.connector

def hae_kentan_tiedot(icao):
    sql = f"SELECT name FROM airport where ident='{icao}'"
    print(sql)
    # kursorin avulla kommunikoidaan tietokannan kanssa
    kursori = yhteys.cursor()
    # suoritetaan sql-lause kursorin avulla
    kursori.execute(sql)
    # haetaan kursorilta kaikki tulosrivit
    tulos = kursori.fetchall()
    # saatiinko tulosrivejä?
    if kursori.rowcount > 0:
        for rivi in tulos:
            print(f"Lentoaseman nimi on: {rivi[0]}")
    else:
        print("ICAO-koodillasi ei löytynyt lentoasemaa.")
    return


# pääohjelma
yhteys = mysql.connector.connect(
    host='127.0.0.1',           # tai 'localhost'. Viittaa sinun omaan koneeseen.
    port= 3306,
    database='flight_game',     # tähän sinun tietokannan nimi
    user='perususer',           # vaihda tähän sinun oma käyttäjätunnus
    password='salainen',        # käyttäjän oikea salasana
    autocommit=True
    )

icao_koodi = input("Anna kentän ICAO-koodi: ")
hae_kentan_tiedot(icao_koodi)
