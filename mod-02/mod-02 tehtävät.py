käyttäjä = input("Anna nimesi: ")
print("Hauska tavata, " + käyttäjä + "!")

import math
ympyrän_säde = float(input('Anna ympyrän säde:  '))
pinta_ala = (math.pi * ympyrän_säde**2)
print("pinta_ala: " + str(pinta_ala))

suorakulmion_kanta = float(input('Anna suorakulmion kanta:  '))
suorakulmion_korkeus = float(input('Anna suorakulmion korkeus:  '))
suorakulmion_piiri = (suorakulmion_kanta+suorakulmion_korkeus)*2
print("suorakulmion_piiri: " + str(suorakulmion_piiri))

suorakulmion_pinta_ala = (suorakulmion_kanta*suorakulmion_korkeus)
print("suorakulmion_pinta_ala: "+ str(suorakulmion_pinta_ala))


luku_1 = float(input('Anna luku: '))
luku_2 = float(input('Anna luku: '))
luku_3 = float(input('Anna luku: '))
summa = luku_1 + luku_2 + luku_3
print("summa: " + str(summa))
tulo = luku_1 * luku_2 * luku_3
print("tulo: "  + str(tulo))
keskiarvo = (summa/3)
print("keskiarvo: " + str(keskiarvo))

leiviskät = float(input('Anna leiviskät: '))
naulat = float(input('Anna naulat: '))
luodit = float(input('Anna luodit: '))

luoti_massa = luodit * 13.3
naula_massa = 32 * naulat
leiviskä_massa =  leiviskät * 20
leiviskä_massa * 32

print("Massa nykymittojen mukaan: " + str(massa))


import random
numero_1 = (random.randint(0, 9))
numero_2 = (random.randint(0, 9))
numero_3 = (random.randint(0, 9))
print("kolmenumeroinen_koodi: " + str(numero_1) + str(numero_2) + str(numero_3))

num_1 = (random.randint(1,9))
num_2 = (random.randint(1,9))
num_3 = (random.randint(1,9))
num_4 = (random.randint(1,9))
print("nelinumeroinen_koodi: " + str(num_1) + str(num_2) + str(num_3) + str(num_4))



