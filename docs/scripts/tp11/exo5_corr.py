def renvoyer_colonne(tableau : list[list[int]], n_colonne : int) -> list[int]:
    # on doit reconstruire un tableau à partir des valeurs
    # extraites ligne par ligne
    # on nn connait pas la taille finale du tableau...
    tableau_sortie = [] 
    for i in range(len(tableau)):
        for j in range(len(tableau[i])):
            if j == n_colonne:
                tableau_sortie.append(tableau[i][n_colonne])
    return tableau_sortie

T = [[1,2,3], [4,5,6], [8,9, 10]]
nouveau_tableau = renvoyer_colonne(T, 1)
print(nouveau_tableau)