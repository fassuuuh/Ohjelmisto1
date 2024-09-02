import random

a = int(input("Syötä arpakuutioiden lukumäärä: "))

summa = 0
for i in range(a):
    heitto = random.randint(1,6)
    summa += heitto

print(f"Arpakuutioiden silmälukujen summa on: {summa}")
