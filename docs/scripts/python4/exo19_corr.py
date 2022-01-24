import random

# Cette fonction permet de générer aléatoirement un tableau contenant un nombre 
# fixé d'entiers.

# nombre doit devenir un paramètre !

def générer_tableau_entiers(entier_min, entier_max, nombre):
    tableau = [random.randint(entier_min,entier_max) for i in range(nombre)]
    return tableau

tableau_1 = générer_tableau_entiers(-5, 5, 10)
tableau_2 = générer_tableau_entiers(-5, 5, 20)
print(tableau_1)
print(tableau_2)