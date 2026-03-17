#Laajenna ohjelmaa siten, että mukana on kulje-metodi, joka saa parametrinaan tuntimäärän.
# Metodi kasvattaa kuljettua matkaa sen verran kuin auto on tasaisella vauhdilla annetussa tuntimäärässä edennyt.
# Esimerkki: auto-olion tämänhetkinen kuljettu matka on 2000 km.
# Nopeus on 60 km/h. Metodikutsu auto.kulje(1.5) kasvattaa kuljetun matkan lukemaan 2090 km.

class auto:
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

    def kulje(self, kuljettu):
        self.matka += self.nopeus * kuljettu


auto1 = auto("ABC-123", 142)

auto1.matka = 2000
auto1.nopeus = 60

auto1.kulje(1.5)

auto1.kiihdytä(30)
auto1.kiihdytä(70)
auto1.kiihdytä(50)

print(f"{auto1.rekisteri}, huippunopeus {auto1.huippu}, nopeus {auto1.nopeus}, kuljettu {auto1.matka}" )

auto1.kulje(1.5)

auto1.kiihdytä(-200)

print(f"{auto1.rekisteri}, huippunopeus {auto1.huippu}, nopeus {auto1.nopeus}, kuljettu {auto1.matka}." )



