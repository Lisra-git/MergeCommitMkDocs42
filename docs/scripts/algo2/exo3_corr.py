def trouver_plus_leger(liste_de_poids: list, i_debut : int = 0) -> list:
    """
    Trouve la valeur la plus petite d'un tableau d'entiers
    et renvoie la position de cette valeur
    Paramètres d'entrée : 
        - liste_de_poids : tableau d'entiers
        - i_debut : paramètre optionnel (valeur par défaut : 0)
    """
    n = len(liste_de_poids)
    minimum_actuel = 1e99
    i_minimum = -1
    for i in range(i_debut, n):
        if liste_de_poids[i] < minimum_actuel:
            minimum_actuel = liste_de_poids[i]
            i_minimum = i
    return i_minimum