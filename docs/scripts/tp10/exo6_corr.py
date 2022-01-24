def trouver_indice(T, x):
    for indice in range(len(T)):
        # si x est trouvé dans le tableau
        if T[indice] == x: 
            # on renvoie l'indice
            return indice
    # on a fini de parcourir T et
    # x n'est pas trouvé
    return None

T = [2, 4, 5, 7, 12, 7, 5]
indice = trouver_indice(T, 5)
print(indice)