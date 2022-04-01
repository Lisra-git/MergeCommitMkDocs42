def tri_insertion(tableau: list)-> list:
    """
    Réalise un tri par insertion
    Paramètres d'entrée : 
        - tableau : tableau d'entiers
    """  
    n = len(tableau)
    for i in range(1, n):
        valeur_frontière = tableau[i]
        j = i - 1
        while j>=0 and valeur_frontière < tableau[j]:
            tableau[j + 1] = tableau[j]
            j = j - 1
        tableau[j + 1] = valeur_frontière

    return tableau


def trouver_plus_leger(liste_de_poids: list) -> list:
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
    for i in range(n):
        if liste_de_poids[i] < minimum_actuel:
            minimum_actuel = liste_de_poids[i]
            i_minimum = i
    return i_minimum


def tri_selection(tas_des_poids: list)-> list:
    """
    Réalise un tri par sélection simplifié
    Paramètres d'entrée : 
        - boitePoids : tableaux d'entiers
    """
    n = len(tas_des_poids)
    tas_des_poids_triés = []
    
    for _ in range(n):
        indice_leger = trouver_plus_leger(tas_des_poids)
        boite_la_plus_legere = tas_des_poids.pop(indice_leger)
        tas_des_poids_triés.append(boite_la_plus_legere)

    return tas_des_poids_triés