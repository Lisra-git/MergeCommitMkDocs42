import random

départ = 0
arrivée = 5

position_puce = départ
nombre_sauts = 0
while position_puce != arrivée:
    position_puce = position_puce + random.choice([-1, 1])
    nombre_sauts += 1 # ou nombre_sauts = nombre_sauts + 1

print(nombre_sauts)