def muunnos(gallon):
    gallon = float(gallon)
    lit = (gallon * 3.785)
    return lit

while True:
    syote = input("Syötä gallonamäärä: ")
    syote = float(syote)
    litroiksi = muunnos(syote)
    print(f"Syöttämäsi gallonamäärä {syote:.1f} gal on {litroiksi:.2f} litraa.")
    if syote < 0:
        print("Negatiivinen luku syötetty. Ohjelma lopetetaan.")
        break
