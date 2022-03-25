import timeit                     # mesure de temps de calcul
from matplotlib.pyplot import *   # bibliothèque graphique


def plus_leger(liste_de_poids: list, i_debut : int = 0) -> list:
    """
    Trouve la valeur la plus petite d'un tableau d'entiers
    et renvoie la position de cette valeur
    Paramètres d'entrée : 
        - T : tableau d'entiers
        - i_debut : paramètre optionnel (valeur par défaut : 0)
    """
    n = len(liste_de_poids)
    

    return


def tri_selection_simple(tas_des_poids: list)-> list:
    """
    Réalise un tri par sélection simplifié
    Paramètres d'entrée : 
        - boitePoids : tableaux d'entiers
    """
    n = len(tas_des_poids)
    tas_des_poids_triés = []
    
    for _ in range(0,n):
        indice_leger = plus_leger(tas_des_poids)
        boite_la_plus_legere = tas_des_poids.pop(indice_leger)
        tas_des_poids_triés.append(boite_la_plus_legere)

    return tas_des_poids_triés


def triSelection(boitePoids: list)-> list:
    """
    Réalise un tri par sélection
    Paramètres d'entrée : 
        - boitePoids : tableaux d'entiers
    """
    n = len(boitePoids)
    
    return boitePoids


#--------- Faites vos tests ci-dessous ---------#
listeNombresTriee = tri_selection_simple([10, 3, 7 ,5 ,6, 1]) # trie la liste
print(listeNombresTriee) # affiche la liste



tailleTableau = [ 10**1,10**2,10**3,10**4,10**5,10**6 ]
tempsSelection = []

# Création d'un graphique
# x = [1,2,3,4]
# y = [10, 23, 45, 7]
# plot(x, y, 'x-r')
# show()