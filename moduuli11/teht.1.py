class Julkaisu:
    def __init__(self, name):
        self.name = name

    def tulosta_tiedot(self):
        print(f"Nimi: {self.name}")

class Kirja(Julkaisu):
    def __init__(self, name, kirjoittaja, sivumaara):
        self.kirjoittaja = kirjoittaja
        self.sivumaara = sivumaara
        super().__init__(name)

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"Kirjoittaja: {self.kirjoittaja}\nSivumäärä: {self.sivumaara} ")

class Lehti(Julkaisu):
    def __init__(self, name, paakirjoittaja):
        self.paakirjoittaja = paakirjoittaja
        super().__init__(name)

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"Pääkirjoittaja: {self.paakirjoittaja}")


lehti = Lehti("Aku Ankka","Aki Hyyppä")
kirja = Kirja("Hytti n:o 6","Rosa Liksom", 200)

lehti.tulosta_tiedot()
kirja.tulosta_tiedot()
