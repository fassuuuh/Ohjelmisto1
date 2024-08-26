sukupuoli = input("Anna sukupuolesi (nainen, mies) : ")

hemoglobiini_arvo = float(input("Anna hemoglobiiniarvo (g/l): "))

if (sukupuoli == "nainen" and  117 <= hemoglobiini_arvo <= 175 ):
    print("Hemoglobiiniarvo on normaali")
elif (sukupuoli == "nainen" and hemoglobiini_arvo > 175 ):
    print("Hemoglobiiniarvo on liian korkea")
elif (sukupuoli == "nainen" and hemoglobiini_arvo < 117 ):
    print("Hemoglobiiniarvo on liian alhainen")


if (sukupuoli == "mies" and  134 <= hemoglobiini_arvo <= 195 ):
    print("Hemoglobiiniarvo on normaali")
elif (sukupuoli == "mies" and hemoglobiini_arvo > 195 ):
    print("Hemoglobiiniarvo on liian korkea")
elif (sukupuoli == "mies" and hemoglobiini_arvo < 134 ):
    print("Hemoglobiiniarvo on liian alhainen")

