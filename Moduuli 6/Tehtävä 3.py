def laskin(gallonat):
    return gallonat * 3.785

while True:
    määrä = float(input("Anna gallonit: "))
    if määrä < 1:
        break
    litrat = laskin(määrä)
    print(f"{määrä} gallonaa on {litrat} litraa")