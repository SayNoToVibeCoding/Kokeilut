import random

lkm = int(input("Kuinka monta noppaa? "))

summa = 0

for nopan_nro in range(lkm):
    silmaluku = random.randint(1, 6)
    print(f"Noppa {nopan_nro+1}: tulos = {silmaluku}")
    summa += silmaluku
print(f"Silmälukujen summa = {summa}")
