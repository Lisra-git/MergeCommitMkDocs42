def additionner_tableau(tableau : list[int]) -> int:
    somme = 0
    for valeur in tableau:
        somme = somme + valeur
    return somme

T = [1, 2, 3]
somme = additionner_tableau(T)
print(somme)