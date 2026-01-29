luku = int(input("Anna luku: "))

if luku <= 1:
    print("Numerosi ei ole alkuluku")

else:
    for numero in range(2, luku):
        if luku % numero == 0:
            print("Numerosi ei ole alkuluku")
            break
    else:
        print("Luku on alkuluku")