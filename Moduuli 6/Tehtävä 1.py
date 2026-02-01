import random
print("Printtaa nopan silmäluvut kunnes luku on 6")
def noppa():
     return random.randint(1,6)
while True:
    luku = noppa()
    print("Nopan silmäluku", luku)
    if luku == 6:
        break
