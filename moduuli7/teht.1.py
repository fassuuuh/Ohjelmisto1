vuodenajat = ("kevät", "kesä", "syksy", "talvi")

kuu = int(input("Syötä kuukauden nro (1-12): "))
if kuu <= 5 and kuu >= 3:
    print(f"Vuodenaika on {vuodenajat[0]}.")
elif kuu >= 6 and kuu <= 8:
    print(f"Vuodenaika on {vuodenajat[1]}.")
elif kuu >= 9 and kuu <= 11:
    print(f"Vuodenaika on {vuodenajat[2]}.")
elif kuu == 12 or kuu <= 2:
    print(f"Vuodenaika on {vuodenajat[3]}.")
else:
    print("Virheellinen luku.")



