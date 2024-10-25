class Hissi:
    def __init__(self, alin, ylin):
        self.alin = alin
        self.ylin = ylin
        self.sijainti = self.alin

    def siirry_kerrokseen(self, kerros):
            if kerros < self.alin or kerros > self.ylin:
                print(f"Kerrosta ei ole olemassa. Valitse {self.alin}-{self.ylin}.")

            elif self.sijainti < kerros:
                for i in range(kerros - self.sijainti):
                    hissi.kerros_ylos()

            elif self.sijainti > kerros:
                for i in range(self.sijainti - kerros):
                    hissi.kerros_alas()

    def kerros_ylos(self):
        self.sijainti += 1
        print(f"Hissi on nyt {self.sijainti} kerroksessa.")

    def kerros_alas(self):
        self.sijainti -= 1
        print(f"Hissi on nyt {self.sijainti} kerroksessa.")

hissi = Hissi(0,20)
print("\nHissi menee nyt ylospäin.\n")
hissi.siirry_kerrokseen(7)
print("\nHissi menee nyt alaspäin.\n")
hissi.siirry_kerrokseen(0)

