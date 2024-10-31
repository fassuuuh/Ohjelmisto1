
class Auto:
    def __init__(self, rekkari, huippunop):
        self.rekkari = rekkari
        self.huippunop = huippunop
        self.hetkinop = 80
        self.kuljettumatka = 0

    def kiihdyta(self, nopeudenmuutos):
        if nopeudenmuutos <= 0:
            self.hetkinop += nopeudenmuutos
            if self.hetkinop <= 0:
                self.hetkinop = 0
        elif nopeudenmuutos >= 1:
            self.hetkinop += nopeudenmuutos
            if self.hetkinop > self.huippunop:
                self.hetkinop = self.huippunop
        return

    def kulje(self, tuntimaara):
        kuljettu = tuntimaara * self.hetkinop
        self.kuljettumatka += kuljettu
        return self.kuljettumatka

class Sähköauto(Auto):
    def __init__(self, rekkari, huippunop, akkukapasiteetti):
        self.akkukapasiteetti = akkukapasiteetti
        super().__init__(rekkari, huippunop)

class Polttomoottoriauto(Auto):
    def __init__(self, rekkari, huippunop, bensatankin_koko):
        self.bensatankin_koko = bensatankin_koko
        super().__init__(rekkari, huippunop)

sähköauto = Sähköauto("ABC-15",180, 52.5 )
moottoriauto = Polttomoottoriauto("ACD-123",165, 32.3)

sähköauto.kulje(3)
moottoriauto.kulje(3)

print("Kuljettu matka:", sähköauto.kuljettumatka , "km")
print("Kuljettu matka:", moottoriauto.kuljettumatka , "km")


