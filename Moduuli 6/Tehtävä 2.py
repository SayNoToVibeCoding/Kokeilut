import random

def noppa(puolet):
     return random.randint(1,puolet)

max = int(input("Anna nopan maksimiluku: "))

while True:
    luku = noppa(max)
    print("Nopan silmäluku", luku)
    if luku == max:
        break
