import mysql.connector

def hae_kenttien_lukumaarat(maakoodi):
    sql = "SELECT type, COUNT(*) FROM airport WHERE iso_country = %s GROUP BY type"

    kursori = yhteys.cursor()
    kursori.execute(sql, (maakoodi,))
    tulos = kursori.fetchall()

    if kursori.rowcount > 0:
        print(f"\nLentokentät maassa {maakoodi}:")
        for rivi in tulos:
            print(f"{rivi[0]}: {rivi[1]} kappaletta")
    else:
        print(f"Maakoodilla {maakoodi} ei löytynyt lentokenttiä.")
    return


#pääohjelma
yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='roni',
    password='roni12345',
    autocommit=True
)

maakoodi = input("Anna maakoodi (esim. FI): ").upper()
hae_kenttien_lukumaarat(maakoodi)