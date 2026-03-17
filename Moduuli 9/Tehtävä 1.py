class auto:
    def __init__(self, rekisteri, huippu, nopeus, matka ):
        self.rekisteri = rekisteri
        self.huippu = huippu
        self.nopeus = nopeus
        self.matka = matka

matka = 0
nopeus = 0
auto1 = auto("ABC-123", 142,nopeus ,matka)

print(f"{auto1.rekisteri}, huippunopeus {auto1.huippu}, nopeus {auto1.nopeus}, matka {auto1.matka}." )



