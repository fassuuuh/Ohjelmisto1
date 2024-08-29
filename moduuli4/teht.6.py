import math
import random
iterator = 0
N = float(input("Syötä pisteiden määrä: "))
n = 0
while iterator < N:
    iterator += 1
    x = random.random() * 2 - 1
    y = random.uniform(-1,1)
    if x**2 + y**2 < 1:
        print("Osui ympyrän sisälle.")
        n = n + 1
print(f"{N} pisteestä {n} osui yksikköympyrän sisälle.")
Pii = 4 * n / N
print(f"Piin likiarvo on {Pii}.")
print(f"Virhe verrattuna math.pi ({math.pi:.5f}) : {Pii - math.pi:.5f}")

