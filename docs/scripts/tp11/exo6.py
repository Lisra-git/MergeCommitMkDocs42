def convertir_tableau_tableau(tableau : list[list[int]]) -> list[list[int]]:
    tableau_sortie = [[0 for i in range(3)] for j in range(3)]
    
    return tableau_sortie

# afficher le tableau Python sous une forme sympathique
def afficher(tableau: list[list[int]]) -> None:
    for ligne in tableau:
        for valeur in ligne:
            print(valeur, end = "")
        print()

T = [[0,1,-1], [1,-1,1], [0, 0, 1]]
nouveau_tableau = convertir_tableau_tableau(T)
afficher(nouveau_tableau)