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
