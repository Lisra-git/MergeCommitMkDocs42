<style>
 table {
    border-collapse: collapse;
}

table, th, td {
    border: 1px solid black;
    width:400px;
    text-align:center;
}
</style>

# Algorithmes de tri : tri par insertion

Nous avons étudié un premier algorithme de tri la dernière séance. Cet algorithme est le tri par sélection. Toutefois, cet algorithme est très inefficace : il nous faut donc trouver un algorithme plus rapide. 

Le but de ce TP est d'étudier un deuxième algorithme de tri classique appelé le tri par insertion.


## Algorithme "avancé" : tri par insertion

!!! question "Question 1"

    Le tri par insertion est fondé sur le principe de séparation du tableau à trier en deux parties :

    - une partie gauche toujours triée ;
    - une partie droite à trier.
    
    Entre ces deux parties se situe un élément _frontière_ que nous allons déplacer de la partie à trier vers la partie triée. Cet élément sera placé de telle manière à ce que la partie triée reste toujours triée!
    
    ???+ example "Exemple" 
    
        On démarre du tableau `#!python [3, 8, 2, 9, 5]`.

        À la deuxième étape, on est dans cette situation :
        <table>
            <thead>
                <tr>
                    <th colspan=2>Partie triée</th>
                    <th colspan=3>Partie à trier</th>
                </tr>
                <tr>
                    <th colspan=2></th><th>Frontière</th><th colspan=2></th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>3</td>
                    <td>8</td>
                    <td>2</td>
                    <td>9</td>
                    <td>5</td>
                </tr>
            </tbody>
        </table>

        À la troisième étape, on est dans cette situation :
        <table>
            <thead>
                <tr>
                    <th colspan=3>Partie triée</th>
                    <th colspan=2>Partie à trier</th>
                </tr>
                <tr>
                    <th colspan=3></th><th>Frontière</th><th colspan=1></th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>3</td>
                    <td>2</td>
                    <td>8</td>
                    <td>9</td>
                    <td>5</td>
                </tr>
                <tr>
                    <td>2</td>
                    <td>3</td>
                    <td>8</td>
                    <td>9</td>
                    <td>5</td>
                </tr>
            </tbody>
        </table>

    - Que s'est-il passé à la première étape ?
    - Expliquez ce que vous allez faire pour trier le tableau de l'exemple selon la méthode décrite ci-dessus. Prenez le temps de comprendre chaque étape à l'aide d'une feuille de brouillon.

!!! question "Question 2"
    
    À partir de la question précédente, essayez d'écrire un algorithme qui permet de faire le tri par insertion. 
    
    On ne cherchera pas à écrire cet algorithme en Python et on ne se préoccupera pas forcément des petits détails d'implémentation.

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
    
    - Comparez avec votre proposition et identifiez les différences et les similarités.

    - **À l'aide d'une feuille et d'un crayon** et en recopiant le tableau algorithmique ci-dessous, appliquez cet algorithme sur le tableau T = [10, 3, 7 ,5 ,6, 1]. En particulier, on suivra l'évolution de T à chaque passage dans les différentes boucles.

    | lignes | i | valeur_frontière | j | tableau[j] | test tant que | tableau[j+1]| tableau |
    |-|-|-|-|-|-|-|-|
    |...|...|...|...|...|...|...|...|

!!! question "Question 4"

    - Montrez que la propriété "quand i prend une valeur k quelconque, les valeurs comprises entre 0 et k du tableau sont toujours triés dans l'ordre croissant". Une telle propriété est appelée un invariant de boucle.
    - Conclure sur le fait que notre algorithme réalise bien un tri d'un tableau dans l'ordre croissant.

!!! question "Question 5"

    Convertir l'algorithme en langage Python dans l'éditeur de code ci-dessous : 

    {{IDE("algo3/exo1", MAX = 1000)}}


!!! question "Question 6"

    Tester votre code Python sur [PythonTutor.com](www.pythontutor.com) pour observer le fonctionnement du programme. 

    On fera des tests par exemple pour les tableaux :
    ```python
    tab1 = [1, 5, 12, 8]
    tab2 = [-3, -5, -12, -1]
    tab3 = []
    ```



## Algorithme : complexité et mesure de temps

!!! Question "Question 7"

    - [ ] Indiquez le nombre d'étapes mis par PythonTutor pour trier (par insertion) les cas suivants : 
    L = [4, 2, 8, 7, 9, 3, 11] 
    L = [13, 11, 8, 6, 4, 2, 1]
    L = [1, 4, 5, 6, 9, 13,15]

    - [ ] En déduire quel est le pire des cas et le meilleur des cas pour cet algorithme. 
    - [ ] Quelle est la complexité dans le meilleur des cas ? dans le pire des cas ?

Cette partie est à réaliser en local sur Thonny. 

La librairie `#!python timeit` permet de faire des mesures de vitesse d'exécution. Pour cela, il faut d'abord l'importer à l'aide de l'instruction `#!python import timeit`.


La librairie timeit permet de faire des mesures de vitesse d'exécution (voir Partie 1 pour une explication plus détaillée).
Python possède une fonction de tri interne. Cette fonction s'appelle sorted et s'utilise ainsi : 
`#!python sorted([10, 3, 7 ,5 ,6, 1])`
renvoie
`#!python [1, 3, 5, 6, 7, 10]`.

Pour trier un tableau dans l'ordre inverse, on va utiliser `#!python tab_100_inv = sorted(tab_100, reverse=True)`.

- Créer des tableaux de taille 100, 1000, 10000.
- Dans le pire des cas, réaliser et afficher quelques mesures de temps d'exécution des 3 algorithmes de tri dont nous disposons : tri par sélection, tri par insertion et `#!python sorted`.
- Modifier votre programme de manière à enregistrer les résultats des mesures de temps dans trois tableaux : `#!python temps_insertion`, `#!python temps_sorted` et `#!python temps_sélection`.

!!! example "Exemple de résultat"

    ```python
    taille_tableau = [ 10, 100, 1000, 10000 ]
    temps_naif = []
    temps_sélection = []
    # Mesure de temps de calcul 
    # Obtention des résultats.
    temps_naif = [ 0.0001 , 0.01, 0.1, 1.2 ]
    temps_dichotomique = [ 0.0001 , 0.001, 0.01, 0.2 ]
    ```

- On peut réaliser des graphiques grâce à une librairie appelée matplotlib. À l'aide d'une recherche, trouver comment fonctionne matplotlib. Nous aurons besoin de l'importation : `#!python from matplotlib.pyplot import *`. 
- Réaliser un graphique représentant vos mesures de temps pour les deux algorithmes en fonction de la taille du tableau. On pourra utiliser une échelle logarithmique en abscisse et en ordonnées.