pienin = None
suurin = None

while True:
    luku = (input("Anna luku: "))

    if pienin is None or luku < pienin:
        pienin = luku
    if suurin is None or luku > suurin:
        suurin = luku

    if luku == " ":
        print(pienin)
        print(suurin)
        print("Lopetetaan toiminnot.")
        break


