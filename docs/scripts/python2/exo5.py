nombre = 48
diviseur = 1

if nombre % 2 == 0 :  # si le reste de la division du nombre par 2 égal 0
    if nombre % 3 == 0 :
        diviseur = 2 * 3
    else :
        diviseur = 2
else :
    if nombre % 3 == 0 :
        diviseur = 3

print(diviseur)