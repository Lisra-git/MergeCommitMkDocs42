def recherche_naive(tableau : list[int], élément_recherché : int):
    # Attention au nommage de vos variables.
    for élément in tableau:
        if élément == élément_recherché:
            return True
    return False