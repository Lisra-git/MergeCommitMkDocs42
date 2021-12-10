def déterminer_minimum(taille_T1, taille_T2):
    if taille_T2 > taille_T1: return taille_T1
    else: return taille_T2

def distance_hamming(T1, T2):
    taille_T1 = len(T1)
    taille_T2 = len(T2)
    taille_minimum = déterminer_minimum(taille_T1, taille_T2)

    différence = 0
    for indice in range(taille_minimum):
        if T1[indice] != T2[indice]:
            différence = différence + 1

    if taille_T1 > taille_minimum:
        manquant = taille_T1 - taille_minimum
    else:
        manquant = taille_T2 - taille_minimum

    différence = différence + manquant
    return différence

T1 = ['a', 'c', 'b', 'a']
T2 = ['a', 'b', 'b', 'a', 'c', 'd', 'd']

print(distance_hamming(T1, T2))