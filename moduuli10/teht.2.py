class Hissi:
    def __init__(self, alin, ylin):
        self.alin = alin
        self.ylin = ylin
        self.sijainti = self.alin

    def siirry_kerrokseen(self, kerros):
        if kerros < self.alin or kerros > self.ylin:
            print(f"Kerrosta ei ole olemassa. Valitse {self.alin}-{self.ylin}.")
            return

        print(f"Hissi yrittää siirtyä kerrokseen {kerros}.")

        while self.sijainti < kerros:
            self.kerros_ylos()

        while self.sijainti > kerros:
            self.kerros_alas()

    def kerros_ylos(self):
        self.sijainti += 1
        print(f"Hissi on nyt {self.sijainti} kerroksessa.")

    def kerros_alas(self):
        self.sijainti -= 1
        print(f"Hissi on nyt {self.sijainti} kerroksessa.")

class Talo:
    def __init__(self, alin, ylin, hissienmaara):
        self.alin = alin
        self.ylin = ylin
        self.hissienmaara = hissienmaara
        self.hissit = [Hissi(self.alin, self.ylin) for i in range(self.hissienmaara)]

    def aja_hissia(self, hissinro, kohdekerros):
        if hissinro < 0 or hissinro >= self.hissienmaara:
            print(f"Hissi numero {hissinro} ei ole käytettävissä. Valitse hissi 0-{self.hissienmaara - 1}.")
            return
        self.hissit[hissinro].siirry_kerrokseen(kohdekerros)

hissi = Hissi(0,20)
talo1 = Talo(0,20,2)

talo1.aja_hissia(0, 5)
talo1.aja_hissia(0, 0)


