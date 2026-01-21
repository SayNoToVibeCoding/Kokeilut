isoin = None
pienin = None

while True:
    luku = input("Anna luku (Tyhjä lopettaa): ")
    if luku == "":
        break
    if isoin is None:
        isoin = luku
    elif luku > isoin:
        isoin = luku
    if pienin is None:
        pienin = luku
    elif luku < pienin:
        pienin = luku

print("Isoin Numero on", isoin)
print("Pienin Numero on", pienin)