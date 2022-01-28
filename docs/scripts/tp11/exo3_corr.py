def renvoyer_diagonale_down(tableau : list[list[int]]) -> list[int]:
    taille_tableau = len(tableau) # nombre de lignes
    tableau_sortie = [0] * taille_tableau
    for i in range(taille_tableau):
        tableau_sortie[i] = tableau[i][i]
    return tableau_sortie

# ou en une ligne !
def renvoyer_diagonale_down(tableau : list[list[int]]) -> list[int]:
    return [tableau[i][i] for i in range(len(tableau))]

tableau = [[0, 0, 0], [1, -1, 1], [1, -1, 1]]
diagonale_down = renvoyer_diagonale_down(tableau)
print(diagonale_down)