import random

nombre = 10
def générer_tableau_entiers(entier_min, entier_max):
    tableau = [random.randint(entier_min,entier_max) for i in range(nombre)]
    return tableau

tableau_1 = générer_tableau_entiers(-5, 5)
print(tableau_1)