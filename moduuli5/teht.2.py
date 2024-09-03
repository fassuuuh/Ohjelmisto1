luvut = []

luku = (input("Syötä luku tai paina Enter: "))
while luku !="":
    luvut.append(luku)
    luku = (input("Syötä luku tai paina Enter: "))

luvut.sort(reverse=True)
print(luvut)