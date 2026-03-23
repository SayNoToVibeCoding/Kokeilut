import random

class Auto:
    def __init__(self, rekisteri, huippu,):
        self.rekisteri = rekisteri
        self.huippu = huippu
        self.nopeus = 0
        self.matka = 0

    def kiihdytä(self, muutos):
        self.nopeus += muutos

        if self.nopeus > self.huippu:
            self.nopeus = self.huippu

        if self.nopeus < 0:
            self.nopeus = 0

    def kulje(self, aika):
        self.matka += self.nopeus * aika

class kilpailu:
    def __init__(self, nimi, pituus, autot):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = autot

    def tunti_kuluu(self):
        for kisa_auto in self.autot:
            muutos = random.randint(-10, 15)
            kisa_auto.kiihdytä(muutos)
            kisa_auto.kulje(1)

    def tulosta_tilanne(self):
        print("Rekisteri | Huippunopeus | Nopeus | Matka ")
        for auto in self.autot:
            print(f"{auto.rekisteri} | {auto.huippu} | {auto.nopeus} | {auto.matka}")

    def kilpailu_ohi(self):
        for auto in self.autot:
            if auto.matka >= self.pituus:
                return True
        return False

autot = []

for i in range(1, 11):
    rekisteri = f"ABC-{i}"
    huippu = random.randint(100, 200)

    uusi_auto = Auto(rekisteri, huippu)
    autot.append(uusi_auto)

ralli = kilpailu("Suuri Rallikisa", 8000, autot)

tunnit = 0

while not ralli.kilpailu_ohi():
    ralli.tunti_kuluu()
    tunnit += 1

    if tunnit % 10 == 0:
        print(f"TILANNE {tunnit} tunnin jälkeen!")
        ralli.tulosta_tilanne()

kilpailu_kaynnissa = True

print(f"\nKILPAILU PÄÄTTYI! Aikaa kului {tunnit} tuntia.")
ralli.tulosta_tilanne()

