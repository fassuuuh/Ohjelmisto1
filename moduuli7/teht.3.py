lentoasemat = {}
while True:
    print("\n1 = Syötä uusi lentoasema, 2 = Hae lentoaseman tiedot, 3 = Lopeta toiminnot")
    toiminto = int(input("Valitse toiminto: "))

    def lisays():
        icao = input("Syötä lentoaseman ICAO-koodi: ").upper()
        nimi = input("Syötä lentoaseman nimi: ").upper()
        lentoasemat[icao] = nimi
        print("Lentoasema lisätty.")

    if toiminto != 1 and toiminto != 2 and toiminto != 3:
        print("Virheellinen valinta. Syötä 1, 2 tai 3.")
    elif toiminto == 1:
        lisays()
    elif toiminto == 2:
        icao = input("Syötä lentoaseman ICAO-koodi: ").upper()
        if icao in lentoasemat:
            print(f"Lentoasema on {lentoasemat[icao]}")
        else:
            print("Lentoasemaa ei löydy.")
    elif toiminto == 3:
        print("Lopetetaan ohjelma.")
        break





