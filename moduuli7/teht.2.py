nimet = set()
while True:
    syotto = input("Syötä nimi: ")
    if syotto == "":
        print("Syötit tyhjän merkkijonon. Lopetetaan toiminnot.")
        break

    if syotto in nimet:
        print("Aiemmin syötetty nimi.")
    else:
        print("Uusi nimi.")
        nimet.add(syotto)

for p in nimet:
    print(p)


