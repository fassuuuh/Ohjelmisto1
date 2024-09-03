import math

kok_luku = int(input("Syötä kokonaisluku: "))
onko_alkuluku = True

if kok_luku <= 1:
    onko_alkuluku = False
else:
    for i in range(2, math.isqrt(kok_luku)+1):
        if kok_luku % i == 0:
            onko_alkuluku = False
            break

if onko_alkuluku:
    print(f"{kok_luku} on alkuluku")
else:
    print(f"{kok_luku} ei ole alkuluku")


