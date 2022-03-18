def recherche_naive(tableau : list[int], élément_recherché : int):
    # Attention au nommage de vos variables.
    nombre_d_etapes = 0
    for élément in tableau:
        nombre_d_etapes += 1
        if élément == élément_recherché:
            return nombre_d_etapes
    return -1