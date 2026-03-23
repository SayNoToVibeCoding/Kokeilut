from unicodedata import numeric


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
        self.kerros += 1
        print(f"Hissi on kerroksessa {self.kerros}")
    def kerros_alas(self):
        self.kerros -= 1
        print(f"Hissi on kerroksessa {self.kerros}")

class Talo:
    def __init__(self, ylin_kerros, alin_kerros, hissit_Num):
        self.hissit = []
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        for i in range (hissit_Num):
            uusi_hissi = Hissi(alin_kerros, ylin_kerros)
            self.hissit.append(uusi_hissi)

    def aja_hissiä(self, hissitnro, kohdekerros):
        oikea_hissi = self.hissit[hissitnro - 1]

        print(f"Ajetaan hissiä numero {hissitnro}")
        oikea_hissi.siirry_kerrokseen(kohdekerros)

    def palohälytys(self):
        print("PALOHÄLYTYS! Kaikki hissit palaavat alimpaan kerrokseen")

        hissin_numero = 1

        for hissi in self.hissit:
            hissi.siirry_kerrokseen(self.alin_kerros)

            print(f"Hissin {hissin_numero} on kerroksessa {hissi.kerros}")

            hissin_numero += 1

pilvenpiirtäjä = Talo( 10, 1, 3)

pilvenpiirtäjä.aja_hissiä(1,3)
pilvenpiirtäjä.aja_hissiä(2,5)
pilvenpiirtäjä.aja_hissiä(3,7)
pilvenpiirtäjä.palohälytys()