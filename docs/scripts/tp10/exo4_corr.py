def compter_répétition(T, élément):
    compteur = 0
    for entier in T:
        if entier == élément:
            compteur = compteur + 1
    # une fois le parcours complet du 
    # tableau, on renvoie le compteur
    return compteur