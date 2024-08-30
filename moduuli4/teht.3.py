pienin = None
suurin = None

while True:
    luku = (input("Anna luku: "))

    if luku == "":
        print(f"Pienin annettu luku: {pienin}")
        print(f"Suurin annettu luku: {suurin}")
        print("Lopetetaan toiminnot.")
        break

    luku = int(luku)

    if pienin is None or luku < pienin:
        pienin = luku
    if suurin is None or luku > suurin:
        suurin = luku

