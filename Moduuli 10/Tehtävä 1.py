#Kirjoita Hissi-luokka, joka saa alustajaparametreinaan alimman ja ylimmän kerroksen numeron.
#Hissillä on metodit siirry_kerrokseen, kerros_ylös ja kerros_alas.
#Uusi hissi on aina alimmassa kerroksessa.
#Jos tee luodulle hissille h esimerkiksi metodikutsun h.siirry_kerrokseen(5), metodi kutsuu joko kerros_ylös- tai kerros_alas-metodia niin monta kertaa, että hissi päätyy viidenteen kerrokseen.
#Viimeksi mainitut metodit ajavat hissiä yhden kerroksen ylös- tai alaspäin ja ilmoittavat, missä kerroksessa hissi sen jälkeen on.
#Testaa luokkaa siten, että teet pääohjelmassa hissin ja käsket sen siirtymään haluamaasi kerrokseen ja sen jälkeen takaisin alimpaan kerrokseen.

class Hissi:
    def __init__(self, alin, ylin):
        self.alin = alin
        self.ylin = ylin
        self.kerros = alin


    def siirry_kerrokseen(self,kerros):
        while self.kerros < kerros:
            self.kerros_ylos()

        while self.kerros > kerros:
            self.kerros_alas()

    def kerros_ylos(self):
        print(f"Hissi on kerroksessa {self.kerros}")
        self.kerros += 1
    def kerros_alas(self):
        self.kerros -= 1
        print(f"Hissi on kerroksessa {self.kerros}")

hissi1 = Hissi(1, 8)
hissi1.siirry_kerrokseen(4)

print(f"Hissi on kerroksessa {hissi1.kerros}")