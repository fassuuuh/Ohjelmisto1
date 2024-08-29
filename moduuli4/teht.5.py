väärät = 0
while väärät < 5 :
    käyttäjätunnus = input("Syötä käyttäjätunnus: ")
    salasana = input("Syötä salasana: ")
    if käyttäjätunnus == "python" and salasana == "rules":
        print("Tervetuloa!")
        break

    if käyttäjätunnus != "python" and salasana != "rules":
        print("Väärä käyttäjätunnus tai salasana!")
    väärät = väärät + 1

    if väärät >= 5:
        print("Pääsy evätty.")
        break
