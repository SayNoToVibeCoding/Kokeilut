import mysql.connector
from geopy import distance


def hae_kentan_koordinaatit(icao):
    sql = "SELECT latitude_deg, longitude_deg, name FROM airport WHERE ident = %s"

    kursori = yhteys.cursor()
    kursori.execute(sql, (icao,))
    tulos = kursori.fetchone()

    return tulos


# pääohjelma
yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='roni',
    password='roni12345',
    autocommit=True
)

icao1 = input("Anna ensimmäisen kentän ICAO-koodi: ").upper()
icao2 = input("Anna toisen kentän ICAO-koodi: ").upper()

kentta1 = hae_kentan_koordinaatit(icao1)
kentta2 = hae_kentan_koordinaatit(icao2)

if kentta1 and kentta2:
    koordinaatit1 = (kentta1[0], kentta1[1])
    koordinaatit2 = (kentta2[0], kentta2[1])

    etaisyys = distance.distance(koordinaatit1, koordinaatit2).km

    print(f"\n{kentta1[2]} ja {kentta2[2]} välinen etäisyys on {etaisyys:.2f} km")
else:
    if not kentta1:
        print(f"ICAO-koodilla {icao1} ei löytynyt kenttää.")
    if not kentta2:
        print(f"ICAO-koodilla {icao2} ei löytynyt kenttää.")