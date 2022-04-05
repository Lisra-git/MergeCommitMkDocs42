# Exercices sur la complexité

## Algorithme "avancé" : tri par insertion

!!! question "Question 1"

    Écrire un algorithme appelé `distance` :
    - qui renvoie -1 si deux mots ne sont pas de la même taille
    - qui renvoie le nombre de lettres différentes à la même position sinon.

    !!! example "Exemple"

        `mentor` et `montre` ont une différence de 3.

        `bide` et `aide` ont une différence de 1.

    Quelle est la complexité de votre algorithme ?
    

!!! question "Question 2"
    
    Quelle est la complexité du programme python ci-dessous, où `dictionnaire` est un tableau contenant N mots ?

    ```python
    def gen_graphe(dictionnaire):
    g = Graphe_dico()
    for mot_1 in dictionnaire:
        for mot_2 in dictionnaire:
            if distance(mot_1, mot_2) == 1:
                g.ajouteArc(mot1, mot2)
    return g
    ```

!!! question "Question 3"

    On donne ci-dessous l'algorithme du tri par insertion. 
    
    ```bash
    n ← nombre d'éléments du tableau
    pour i allant de 1 à n-1 inclus:
        valeur_frontiere ← tableau[i]
        j ← i-1
        tant que j>=0 et valeur_frontiere < tableau[j]:
            tableau[j+1] ← tableau[j]
            j ← j-1
        tableau[j+1] ← valeur_frontiere
        renvoyer tableau
    ```

    - Décrire le principe de fonctionnement de cet algorithme.
    - Quel serait le meilleur des cas ? et la complexité dans ce cas ?
    - Quel serait le pire des cas ? et la complexité dans ce cas ?

!!! question "Question 4"

    Soit le tableau `[2, 4, 6, 8, 12, 16, 17, 22, 67, 87, 112, 141, 155, 167, 178]

    Dessiner un arbre représentant toutes les possibilités lorsque l'on recherche un nombre. 
    
    En déduire la complexité de la recherche dichotomique.

!!! question "Question 5"

    Quel est le principe de fonctionnement du tri par sélection ?

    Donner sa complexité.

!!! question "Question 6"

    Quelle est la complexité de la fonction suivante :

    ```python
    def nb_zeros(n):
    resultat = 0
    while n % 10 == 0:
        n = n // 10
        resultat += 1
    return resultat
    ```

!!! question "Question 7"

    Quelle est la complexité de la fonction suivante :

    ```python
    def negatif(image):
    '''renvoie le négatif de l'image sous la forme d'une liste de listes'''
    hauteur_img, largeur_img = hauteur(image), largeur(image)
    nouvelle_image = [[0 for j in range(largeur_img)] for i in range(hauteur_img)]
    for i in range(hauteur_img):
        for j in range(largeur_img):
            nouvelle_image[i][j] = 255 - image[i][j]
    return nouvelle_image
    ```

!!! question "Question 8"

    Quelle est la complexité de la fonction suivante :

    ```python
    def perm_rec(liste, pris):
    if len(pris) == len(liste):
        return [pris.copy()]
    else:
        liste_permutations = []
        for element in liste:
            if element not in pris:
                pris.append(element)
                for permut in perm_rec(liste, pris):
                    liste_permutations.append(permut)
                pris.pop()
        return liste_permutations
    ```