class Auto:
    def __init__(self, rekkari, huippunop):
        self.rekkari = rekkari
        self.huippunop = huippunop
        self.hetkinop = 0
        self.kuljettumatka = 0

auto = Auto("ABC-123",142)
print("Rekisteritunnus:", auto.rekkari)
print("Auton huippunopeus:" , auto.huippunop , "km/h")
print("Auton hetkellinen nopeus: " , auto.hetkinop)
print("Auton kuljettu matka: " , auto.kuljettumatka)
