import random

tableau = [10, 20, 30, 40]
valeur_mini = 0

for nombre in tableau:
    valeur_maxi = nombre
    print(random.randint(valeur_mini, valeur_maxi))
    valeur_mini = valeur_maxi