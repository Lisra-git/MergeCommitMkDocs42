def recherche_dichotomique(tableau : list[int], élément_recherché : int):
    # Attention au nommage de vos variables.
    entier_trouvé = False
    debut = 0
    fin = len(tableau)-1

    while entier_trouvé == False and debut <= fin:
        milieu = (debut + fin) // 2
        if tableau[milieu] == élément_recherché:
            entier_trouvé = True
        elif élément_recherché > L[milieu] :
            debut = milieu+1
        else :
            fin = milieu-1

    return entier_trouvé
