import random

pisteet = int(input("Anna arvottavien pisteiden määrä: "))
pMäärä = 0
silmukat = 0
while silmukat < pisteet:
    x = random.randint(-1000,1000) / 1000
    y = random.randint(-1000,1000) / 1000
    if x**2 + y**2 < 1:
        pMäärä += 1
    silmukat += 1
likiarvo = 4 * pMäärä / pisteet
print("Piin likiarvo on:", likiarvo)