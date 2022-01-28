def convertir_tableau_tableau(tableau : list[list[int]]) -> list[list[int]]:
    tableau_sortie = [[0 for i in range(3)] for j in range(3)]
    for i in range(len(tableau)):
        for j in range(len(tableau)):
            if tableau[i][j] == 1:
                tableau_sortie[i][j] = "\u00D7"
            elif tableau[i][j] == -1:
                tableau_sortie[i][j] = "\u25EF"
            else:
                tableau_sortie[i][j] = " "
    return tableau_sortie

def afficher(tableau: list[list[int]]) -> None:
    for ligne in tableau:
        for valeur in ligne:
            print(valeur, end = "")
        print()

T = [[0,1,-1], [1,-1,1], [0, 0, 1]]
nouveau_tableau = convertir_tableau_tableau(T)
afficher(nouveau_tableau)
print(nouveau_tableau)