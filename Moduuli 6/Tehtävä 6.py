import math

def pizzahinta(halkaisija, hinta):
    sade = (halkaisija / 2) / 100
    pinta_ala = math.pi ** sade ** 2
    return hinta / pinta_ala
print("Pizza 1")
a1 = float(input("Anna halkaisija(cm): "))
b1 = float(input("Anna hinta(euro): "))

print("Pizza 2")
a2 = float(input("Anna halkaisija(cm): "))
b2 = float(input("Anna hinta(euro): "))

eka = pizzahinta(a1, b1)
toka =  pizzahinta(a2, b2)
print(f"Pizzan 1 yksikköhinta {eka:.2f} €/m2")
print(f"Pizzan 2 yksikköhinta {toka:.2f} €/m2")

if eka < toka:
    print("Pizza 1 antaa paremman vastineen rahalle.")
elif toka < eka:
    print("Pizza 2 antaa paremman vastineen rahalle.")
else:
    print("Pizzat ovat yhtä edullisia")
