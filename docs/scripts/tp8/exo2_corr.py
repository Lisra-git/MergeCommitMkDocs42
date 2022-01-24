import random

def générer_tableau_0(nombre_éléments):
    tableau_de_0 = nombre_éléments * [0]
    return tableau_de_0

def générer_tableau_aléatoire(nombre_éléments, a, b):
    tableau_aléatoire = [random.randint(a,b) for i in range(nombre_éléments)]
    return tableau_aléatoire

T_zéro = générer_tableau_0(3)
print(T_zéro)
T_aléa = générer_tableau_aléatoire(5, 1, 6)
print(T_aléa)