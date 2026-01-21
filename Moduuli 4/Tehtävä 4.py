import random

while True:
    luku = int(input("Anna luku 1-10 väliltä: "))
    Random = random.randint(1, 10)
    if luku == Random:
        print("Oikein")
        break
    elif luku >= Random:
        print("Liian suuri arvaus")
    elif luku <= Random:
        print("Liian Pieni arvaus")
    print(Random)