def listansumma(luvut):
    summa = 0
    for luku in luvut:
        summa += luku
    return summa

lista= [4,6,1,7,8,22]

tulos = listansumma(lista)
print(lista, "Lukujen summa on", tulos)