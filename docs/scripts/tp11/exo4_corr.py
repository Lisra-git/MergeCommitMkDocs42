def renvoyer_diagonale_up(tableau : list[list[int]]) -> list[int]:
    taille_tableau = len(tableau) # nombre de lignes
    taille_colonne = len(tableau[0]) # nombre de colonnes
    tableau_sortie = [0] * taille_tableau
    for i in range(taille_tableau):
        # i + j == 2:
        tableau_sortie[i] = tableau[i][2-i]
    return tableau_sortie

# ou en une ligne !
def renvoyer_diagonale_up(tableau : list[list[int]]) -> list[int]:
    return [tableau[i][2-i] for i in range(len(tableau))]

tableau = [[0, 0, 0], [1, -1, 1], [1, -1, 1]]
diagonale_down = renvoyer_diagonale_up(tableau)
print(diagonale_down)