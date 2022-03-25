from docs.scripts.algo2.exo1 import trouver_plus_leger


def tri_selection(tas_des_poids: list)-> list:
    """
    Réalise un tri par sélection simplifié
    Paramètres d'entrée : 
        - tas_des_poids : tableaux d'entiers
    """
    n = len(tas_des_poids)
    for i in range(n):
        position_de_la_plus_legere = trouver_plus_leger(tas_des_poids, i)
        tas_des_poids[i], tas_des_poids[position_de_la_plus_legere] \
             = tas_des_poids[position_de_la_plus_legere], tas_des_poids[i]

    return tas_des_poids