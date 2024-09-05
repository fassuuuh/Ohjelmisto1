import math
def calculate_square_price(diameter, price):
    diameter = diameter / 100
    r = diameter / 2
    area = math.pi * r**2
    return price/area

"""
print(calculate_square_price(100, 30))
print(calculate_square_price(30, 20))
"""
pizza1_diameter = float(input("Syötä 1.pizzan halkaisija (cm): "))
pizza2_diameter = float(input("Syötä 2.pizzan halkaisija (cm): "))
pizza1_price = float(input("Syötä 1.pizzan hinta: "))
pizza2_price = float(input("Syötä 2.pizzan hinta: "))

pizza1_square_price = calculate_square_price(pizza1_diameter, pizza1_price)
pizza2_square_price = calculate_square_price(pizza2_diameter, pizza2_price)
print(f"Ensimmäisen pizzan neliöhinta on: {pizza1_square_price:.2f}")
print(f"Toisen pizzan neliöhinta on: {pizza2_square_price:.2f}")

if pizza1_square_price < pizza2_square_price:
    print("Ensimmäinen pizza on neliöhinnaltaan halvempi")
elif pizza1_square_price > pizza2_square_price:
    print("Toinen pizza on neliöhinnaltaan halvempi.")
else:
    print("Pizzojen neliöhinta on sama.")

