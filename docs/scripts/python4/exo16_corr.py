def trouver_répétition(lettre, texte):
    compteur_lettre = 0
    for caractère in texte:
        if lettre == caractère:
            compteur_lettre = compteur_lettre + 1
        if compteur_lettre > 1:
            return True
    # fin de la boucle. On n'a pas trouvé deux occurrences.
    return False

adn = "ACCACGAC"
print(trouver_répétition("A", adn))