
class Auto:
    def __init__(self, rekkari, huippunop):
        self.rekkari = rekkari
        self.huippunop = huippunop
        self.hetkinop = 0
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

auto1 = Auto("ABC-123",142)
auto1.kiihdyta(30)
auto1.kiihdyta(70)
auto1.kiihdyta(50)

print("Auton nopeus:", auto1.hetkinop, "km/h")

auto1.kiihdyta(-200)
print("Auton nopeus:", auto1.hetkinop, "km/h")

