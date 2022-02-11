from __future__ import annotations
import random

def additionner_tableau(tableau : list[int]) -> int:
    somme = 0
    for valeur in tableau:
        somme = somme + valeur
    return somme

def renvoyer_ligne(tableau : list[list[int]], n_ligne : int) -> list[int]:
    return tableau[n_ligne]

def renvoyer_diagonale_down(tableau : list[list[int]]) -> list[int]:
    taille_tableau = len(tableau) # nombre de lignes
    tableau_sortie = [0] * taille_tableau
    for i in range(taille_tableau):
        tableau_sortie[i] = tableau[i][i]
    return tableau_sortie

# ou en une ligne !
def renvoyer_diagonale_up(tableau : list[list[int]]) -> list[int]:
    return [tableau[i][2-i] for i in range(len(tableau))]


def renvoyer_colonne(tableau : list[list[int]], n_colonne : int) -> list[int]:
    tableau_sortie = [] 
    for i in range(len(tableau)):
        for j in range(len(tableau[i])):
            if j == n_colonne:
                tableau_sortie.append(tableau[i][n_colonne])
    return tableau_sortie

def convertir_tableau_tableau(tableau : list[list[int]]) -> list[list[int]]:
    tableau_sortie = [[0 for i in range(3)] for j in range(3)]
    for i in range(len(tableau)):
        for j in range(len(tableau)):
            if tableau[i][j] == 1:
                tableau_sortie[i][j] = "\u00D7"
            elif tableau[i][j] == -1:
                tableau_sortie[i][j] = "\u25EF"
            else:
                tableau_sortie[i][j] = "\u25AF"
    return tableau_sortie

def afficher(tableau: list[list[int]]) -> None:
    for ligne in tableau:
        for valeur in ligne:
            print(valeur, end = "")
        print()

def poser_jeton(tableau : list[list[int]], n_joueur : int) -> list[list[int]]:
    n_ligne, n_colonne = map(int, input('Positionne ton pion : ').split(','))

    while not(1 <= n_ligne <= 3 and 1 <= n_colonne <= 3):
        print("Ce pion est mal positionné. Repositionnez le correctement au format i,j")
        n_ligne, n_colonne = map(int, input("Positionne ton pion : ").split(','))

    while not(tableau[n_ligne-1][n_colonne-1] == 0):
        print("Petit\u00B7e frippon\u00B7ne, la case est déjà occupée. Repositionnez le pion correctement")
        n_ligne, n_colonne = map(int, input("Positionne ton pion : ").split(','))

    n_ligne = n_ligne - 1
    n_colonne = n_colonne - 1

    tableau[n_ligne][n_colonne] = n_joueur

    return tableau

def finir_partie(plateau):
    somme_colonnes = [additionner_tableau(renvoyer_colonne(plateau, i)) for i in range(3)]
    somme_lignes = [additionner_tableau(renvoyer_ligne(plateau, i)) for i in range(3)]
    somme_diag_up = additionner_tableau(renvoyer_diagonale_up(plateau))
    somme_diag_down = additionner_tableau(renvoyer_diagonale_down(plateau))
    # on crée un grand tableau contenant toutes les sommes :
    resultat_joueur = [somme_diag_up, somme_diag_down]
    for somme in somme_colonnes:
        resultat_joueur.append(somme)
    for somme in somme_lignes:
        resultat_joueur.append(somme)
    return (3 in resultat_joueur) or (-3 in resultat_joueur)

def jouer():
    plateau = [[0]*3 for _ in range(3)]
    afficher(convertir_tableau_tableau(plateau))
    joueur = random.choice([-1, 1]) # on tire au hasard le numéro du joueur qui commence.
    fini = False # booléen pour indiquer si une partie est finie.
    while not fini:
        if joueur == 1: joueur = -1
        else: joueur = 1
        plateau = poser_jeton(plateau, joueur)
        afficher(convertir_tableau_tableau(plateau))
        fini = finir_partie(plateau)
    print(f"Le joueur {joueur} a gagné cet épique duel .")


jouer()