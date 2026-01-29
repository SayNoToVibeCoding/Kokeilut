kaupungit = []

laskuri = 0
for k in range(5):
    kaupunki = input("Anna Kaupungien nimet (Tyhjä lopettaa): ")
    if kaupunki == "":
        break
    kaupungit.append(str(kaupunki))
for nimi in kaupungit:
    print(nimi)