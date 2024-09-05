import random
def silmaluku():
    sl = random.randint(1,6)
    return sl

tulos = 0
while tulos != 6:
    tulos = silmaluku()
    print(tulos)
