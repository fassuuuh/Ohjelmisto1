while True:
    tuumamäärä = float(input("Syötä tuumamäärä: "))
    if tuumamäärä < 0:
        break
    tuuma_sentteinä = tuumamäärä * 2.54
    print(f"Tuumat senttimetreinä: {tuuma_sentteinä:.2f} cm ")

print("Toiminto lopetettu. Syötä positiivinen luku.")