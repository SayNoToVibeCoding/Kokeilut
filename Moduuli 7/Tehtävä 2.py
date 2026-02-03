nimet = []

while True:
    uusin = str(input("Anna Nimi (Tyhjä lopettaa): "))
    if uusin in nimet:
        print("Nimi on jo aiemmin syötetty")
    elif uusin =="":
        print("Annetut nimet")
        for nimi in nimet:
            print(nimi)
        break
    else:
        nimet.append(uusin)
        print("Uusi nimi")

