leiviskät = float(input('Anna leiviskät: '))
naulat = float(input('Anna naulat: '))
luodit = float(input('Anna luodit: '))

luoti_g = 13.3
naula_l = 32
leiviskä_n = 20

kokonais_luodit = (leiviskät * leiviskä_n * naula_l) + (naulat * naula_l) + luodit
kokonais_grammat = kokonais_luodit * luoti_g

kilogrammat = int(kokonais_grammat / 1000)
grammat = (kokonais_grammat % 1000)

print(f"Massa nykymittojen mukaan: {kilogrammat} kilogrammaa ja {grammat:4.2f} grammaa ")
