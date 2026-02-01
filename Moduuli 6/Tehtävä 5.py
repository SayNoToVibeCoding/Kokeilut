def parittomat(lista):
    tulos = []
    for luku in lista:
        if luku % 2 == 0:
            tulos.append(luku)
    return tulos
alku = [1,2,3,4,5,6,7,8,9,10]
karsittu = parittomat(alku)
print("Karsimaton lista", alku)
print("Karsittu lista", karsittu)

