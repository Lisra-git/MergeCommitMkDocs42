def trouver_plus_leger(liste_de_poids: list) -> list:
    """
    Trouve la valeur la plus petite d'un tableau d'entiers
    et renvoie la position de cette valeur (-1 si la liste est vide)
    Paramètres d'entrée : 
        - liste_de_poids : tableau d'entiers
    """
    n = len(liste_de_poids)
    

    return


def tri_selection_simple(tas_des_poids: list)-> list:
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