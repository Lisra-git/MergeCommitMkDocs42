def poser_jeton(tableau : list[list[int]], n_joueur : int) -> list[list[int]]:
    # Mmmm... Pourquoi ce input et ce split ?
    n_ligne, n_colonne = map(int, input('Positionne ton pion : ').split(','))

    # ca sert à quoi ces lignes 5 et 6 ??
    while not(1 <= n_ligne <= 3 and 1 <= n_colonne <= 3):
        n_ligne, n_colonne = map(int, input("Positionne ton pion : ").split(','))

    # des -1, mais quelle idée ??
    n_ligne = n_ligne - 1
    n_colonne = n_colonne - 1

    # Woah. C'est quoi ça ?
    tableau[n_ligne][n_colonne] = n_joueur

    # Monsieur, c'est obligatoire ce return ?
    return tableau

# print(poser_jeton([[0]*3 for i in range(3)], 1))