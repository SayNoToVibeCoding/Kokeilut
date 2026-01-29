luvut = []
while True:
    luku = input("Anna seuraava luku tai paina enter lopettaaksesi: ")
    if luku == "":
        break
    luvut.append(int(luku))
luvut.sort(reverse=True)

laskuri = 0
for luku in luvut:
    if laskuri >= 5:
        break
    print(luku)
    laskuri += 1
