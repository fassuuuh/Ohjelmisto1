
class Auto:
    def __init__(self, rekkari, huippunop):
        self.rekkari = rekkari
        self.huippunop = huippunop
        self.hetkinop = 60
        self.kuljettumatka = 2000

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

auto1 = Auto("ABC-123",142)
auto1.kulje(1.5)
print("Kuljettu matka:", auto1.kuljettumatka , "km")


