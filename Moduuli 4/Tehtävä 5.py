kerroin = 0

while True:
    kayttaja = str(input("Anna kayttaja: ").lower())
    salasana = str(input("Anna salasana: ").lower())
    if kerroin == 5:
        print("Viisi väärää yritystä")
        break
    elif kayttaja == "python" and salasana == "rules":
        print("Tervetuloa")
        break
    elif kayttaja != "python" or salasana != "rules":
        print("Pääsy Evätty")
        kerroin = kerroin + 1

