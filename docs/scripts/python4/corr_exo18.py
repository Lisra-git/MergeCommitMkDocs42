import random

def générer(nombre_bit):
    accumulateur = ""
    for _ in range(nombre_bit):
        accumulateur = accumulateur + str(random.randint(0,1))
    return accumulateur

def décoder(nombre_binaire):
    compteur_0 = 0
    compteur_1 = 0    
    for bit in nombre_binaire:
        if bit == '0':
            compteur_0 = compteur_0 + 1
        else:
            compteur_1 = compteur_1 + 1
    if compteur_1 > compteur_0:
        return '1', compteur_1
    else:
        return '0', compteur_0