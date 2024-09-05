syote = input("Syötä gallonamäärä: ")
def muunnos(gallon):
    gallon = float(gallon)
    lit = (gallon * 3.785)
    return lit

litroiksi = muunnos(syote)
print(f"Syöttämäsi gallonamäärä {syote} on {litroiksi:.1f} litraa.")
