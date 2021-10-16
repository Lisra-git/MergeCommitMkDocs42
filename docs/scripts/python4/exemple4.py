phrase = "Turning and turning in the widening gyre"

def trouver_lettre(lettre, texte):
    """ Renvoie True si une lettre apparaît
    dans un texte """
    for caractère in texte:
        print(caractère, lettre, caractère == lettre)
        if caractère == lettre:
            return True # la boucle s'arrête !
    return False

réponse = trouver_lettre("a", phrase)
print("Trouvé ? ", réponse)