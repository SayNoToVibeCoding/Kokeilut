#Nyt ohjelmoidaan autokilpailu.
#Uuden auton kuljettu matka alustetaan automaattisesti nollaksi.
#Tee pääohjelman alussa lista, joka koostuu kymmenestä toistorakenteella luodusta auto-oliosta.
#Jokaisen auton huippunopeus arvotaan 100 km/h ja 200 km/h väliltä. Rekisteritunnus luodaan seuraavasti "ABC-1", "ABC-2" jne.
#Sitten kilpailu alkaa. Kilpailun aikana tehdään tunnin välein seuraavat toimenpiteet:
#Jokaisen auton nopeutta muutetaan siten, että nopeuden muutos arvotaan väliltä -10 ja +15 km/h väliltä.
#Tämä tehdään kutsumalla kiihdytä-metodia.
#Kaikkia autoja käsketään liikkumaan yhden tunnin ajan. Tämä tehdään kutsumalla kulje-metodia.
#Kilpailu jatkuu, kunnes jokin autoista on edennyt vähintään 10000 kilometriä.
#Lopuksi tulostetaan kunkin auton kaikki ominaisuudet selkeäksi taulukoksi muotoiltuna.
import random
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

    def kulje(self, aika):
        self.matka += self.nopeus * aika

autot = []

for i in range(1, 11):
    rekisteri = f"ABC-{i}"
    huippu = random.randint(100, 200)

    uusi_auto = auto(rekisteri, huippu)
    autot.append(uusi_auto)

kilpailu_kaynnissa = True

while kilpailu_kaynnissa:

    for kisa_autot in autot:
        muutos = random.randint(-10, 15)

        kisa_autot.kiihdytä(muutos)
        kisa_autot.kulje(1)

        if kisa_autot.matka >= 10000:
            kilpailu_kaynnissa = False

print(f"{'Rekisteri'} | {'Huippunopeus'} | {'Nopeus'} | {'Matka'}")

for auto in autot:
    print(f"{auto.rekisteri} | {auto.huippu} | {auto.nopeus} | {auto.matka}")
