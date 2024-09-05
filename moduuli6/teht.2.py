import random
tahkot = int(input("Syötä nopan tahkojen määrä: "))
syote = int(input("Syötä maksimisilmäluku: "))

def heita_noppaa(tahkojen_lukum):
    tm = random.randint(1, tahkojen_lukum)
    return tm

tulos = 0
while tulos != syote:
    tulos = heita_noppaa(tahkot)
    print(tulos)
