def suffixe(T1, T2):
    taille_T1 = len(T1)
    taille_T2 = len(T2)
    # cas où T2 est plus petit que T1
    # T1 ne peut pas être un préfixe...
    if taille_T2 < taille_T1:
        return False

    for indice in range(taille_T1):
        if T1[taille_T1 - indice - 1] != T2[taille_T2 - indice - 1]:
            return False
        else:
            print("Jusque-là, tout va bien...")
    # on a parcouru tout T1 dans l'ordre inverse
    # et tous les éléments sont les mêmes
    return True

T1 = [1, 8, 8]
T2 = [5, 6, 3, 1, 8, 8]
print(suffixe(T1, T2))
print(suffixe(T2, T1))