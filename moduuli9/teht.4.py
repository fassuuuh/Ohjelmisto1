import random
class Auto:
    def __init__(self, rekkari, huippunop):
        self.rekkari = rekkari
        self.huippunop = huippunop
        self.hetkinop = 0
        self.kuljettumatka = 0

    def kiihdyta(self, nopeudenmuutos):
        self.hetkinop += nopeudenmuutos
        if self.hetkinop < 0:
            self.hetkinop = 0
        elif self.hetkinop > self.huippunop:
            self.hetkinop = self.huippunop

    def kulje(self, tuntimaara):
        self.kuljettumatka += tuntimaara * self.hetkinop


# Luo lista autoista
autolista = [Auto(f"ABC-{i}", random.randint(100, 200)) for i in range(1, 11)]

# Kilpailu
kilpailu_kaynnissa = True
while kilpailu_kaynnissa:
    for auto in autolista:
        auto.kiihdyta(random.randint(-10, 15))
        auto.kulje(1)

        # Tarkistetaan, onko joku autoista saavuttanut 10 000 km
        if auto.kuljettumatka >= 10000:
            kilpailu_kaynnissa = False
            break

# Tulostetaan kaikkien autojen tiedot taulukkomuodossa
print(
    f"{'Rekist.tunnus':<12} {'Huippunopeus (km/h)':<18} {'Hetkellinen nopeus (km/h)':<24} {'Kuljettu matka (km)':<20}")
print("-" * 70)
for auto in autolista:
    print(f"{auto.rekkari:<12} {auto.huippunop:<18} {auto.hetkinop:<24} {auto.kuljettumatka:<20}")
