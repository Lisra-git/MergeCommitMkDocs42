def sommer(tableau):
    accumulateur = 0
    for entier in tableau:
        accumulateur = accumulateur + entier
    return accumulateur

def moyenner(tableau, taille):
    somme = sommer(tableau)
    return somme / taille
