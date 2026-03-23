#Jatka edellisen tehtävän ohjelmaa siten, että teet Talo-luokan.
# Talon alustajaparametreina annetaan alimman ja ylimmän kerroksen numero sekä hissien lukumäärä.
# Talon luonnin yhteydessä talo luo tarvittavan määrän hissejä.
# Hissien lista tallennetaan talon ominaisuutena.
# Kirjoita taloon metodi aja_hissiä, joka saa parametreinaan hissin numeron ja kohdekerroksen.
# Kirjoita pääohjelmaan lauseet talon luomiseksi ja talon hisseillä ajelemiseksi.


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

        print(f"\n--- Ajetaan hissiä numero {hissitnro} ---")
        oikea_hissi.siirry_kerrokseen(kohdekerros)

pilvenpiirtäjä = Talo( 10, 1, 3)

pilvenpiirtäjä.aja_hissiä(1,3)
pilvenpiirtäjä.aja_hissiä(2,5)
pilvenpiirtäjä.aja_hissiä(3,7)
