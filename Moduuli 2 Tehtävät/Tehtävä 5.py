Leiviskä = float(input("Anna Leiviskät:"))
Naula = float(input("Anna Naulat:"))
Luoti = float(input("Anna Luodit:"))
Luoti = 13.3
NaulatLuoti = 32
LeiviskäNaula = 20
Luoteja_yht = Leiviskä * LeiviskäNaula * NaulatLuoti + Naula * NaulatLuoti + Luoti
massa = Luoteja_yht * Luoti
kg = float(massa // 1000)
gramma = massa % 1000
print(f"Massa Nykymittojen Mukaan: = {kg} kg {gramma:.2f} g")


# Arvo jonka antoi oli hieman eri kuin esimerkissä, mutta en ymmärtänyt mistä tämä johtuu.