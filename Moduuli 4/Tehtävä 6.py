import random

pisteet = int(input("Anna arvottavien pisteiden määrä: "))
pMäärä = 0
kierrokset = 0
while kierrokset < pisteet:
    x = random.randint(-1000,1000) / 1000
    y = random.randint(-1000,1000) / 1000
    if x**2 + y**2 < 1:
        pMäärä += 1
        #En tiennyt mikä on origo tai Monte Carlon laskukaava
    kierrokset += 1
likiarvo = 4 * pMäärä / pisteet
print("Piin likiarvo on:", likiarvo)