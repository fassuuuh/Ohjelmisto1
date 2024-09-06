lista = []
while True:
    syote = input("Syötä kokonaisluku: ")
    if syote == "":
        break
    syote = int(syote)
    lista.append(syote)

def parillinen(lista):
    parilliset = []
    for i in lista:
        if i % 2 == 0:
            parilliset.append(i)
    return parilliset

print(f"Alkuperäinen lista: {lista}")
print(f"Alkuperäinen lista, josta parittomat karsittu pois: {parillinen(lista)}")


