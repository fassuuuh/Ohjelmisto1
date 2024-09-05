lista = []
while True:
    syote = input("Syötä kokonaisluku: ")
    if syote == "":
        break
    syote = int(syote)
    lista.append(syote)

def yht(lista):
    sum(lista)
    return sum(lista)

print(f"Syöttämäsi lukujen summa on {yht(lista)}.")