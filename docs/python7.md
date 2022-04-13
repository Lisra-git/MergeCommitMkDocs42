# Dictionnaires


## Position du problème 

Un tableau Python possède une seule caractéristique : la valeur portée dans le tableau. 

On peut dire que cette valeur est en quelque sorte reliée à une position.

!!!example "Exemple"
    
    Dans le tableau `#!python ["0626130029", "0616248329", "0601118218"]` :
    
    -  `#!python "0616248329"` est à la position 1 ;
    -  `#!python "0601118218"` à la position 2.

    Toutefois, si maintenant je souhaite accéder au nom des personnes associées à ces numéros de téléphone, c'est compliqué. Il faudrait un deuxième tableau contenant des noms de personnes à la même position : `#!python ["Maman", "Papa", "Médor"]`.

Dans un tableau, la position sert donc de clé primaire (pour dans l'exemple, fusionner deux tableaux). 

## Premier contact

Il y a beaucoup plus pratique : le **dictionnaire**.

Comme dans un dictionnaire réel, un dictionnaire Python est composé de deux champs :

- une **clé** ;
- une **valeur**.

!!!example "Exemple"

    Tout de suite, un exemple :

    `#!python un_dico = {"nom": "LaTaupe", "prenom": "René", "naissance": 2009}`

    à comparer avec :

    `#!python un_tableau = ["LaTaupe", "René", 2009]`.

    {{terminal()}}


!!! {{cours()}}

    Quelques généralités sur les dictionnaires :

    - un dictionnaire se caractérise par des accolades {} ;
    - les **clés** sont définies avant les deux points. Les clés peuvent être de n'importe quel type non mutable.
    - la valeur associée à la clé est indiquée après les deux points. Les valeurs peuvent être de n'importe quel type.

!!!example "Exemple"

    Dans l'exemple précédent : 
    
    - quelles sont les clés de `#!python un_dico`?
    - quelles sont les valeurs associées ?

    ???help "Solution"

        La clé `#!python nom` est associée à la valeur `#!python LaTaupe`, à la clé `#!python prenom` est `#!python René` et à la clé `#!python naissance`, `#!python 2009`.

!!! {{cours()}}

    Il est possible d'initialiser un dictionnaire vide puis de le remplir avec les 4 lignes suivantes :

    ```python
    un_dico = {}     # monDico = dict() est une autre syntaxe possible.
    un_dico["nom"] = "LaTaupe"
    un_dico["prenom"] = "René"
    un_dico["naissance"] = 2009
    ```

    Essayez de créer vous-même ce dictionnaire en recopiant ces instructions. 
    {{terminal()}}

!!! exo "Créer des dictionnaires"
    Dans les exercices ci-dessous, créer les dictionnaires demandés.

    === {{exercice(False, 0)}}

        Dictionnaire nommé `#!python genre` qui indique le genre des mots suivants : `#!python table`, `#!python chemin`, `#!python rail`. Le féminin se notera par la lettre `'f'` et le masculin par la lettre `'m'`.

        {{terminal()}}

        ???help "Solution"

            ```python 
            genre = {}
            genre['table'] = 'f'
            genre['chemin'] = 'm'
            genre['rail'] = 'm'
            ```

            ou, en une ligne :
    
            `#!python 
            genre = {'table' : 'f', 'chemin' : 'm', 'rail' : 'm'}
            `


    === {{exercice(False)}}

        Dictionnaire nommé `#!python film` qui indique les caractéristiques de film : 
        
        - `#!python Pulp Fiction` est associé à `#!python ['Tarantino', 1994]`
        - `#!python Kill Bill` est associé à `#!python ['Tarantino', 2003]`
        - `#!python Holy Grail` est associé à `#!python ['Monty Python', 1975]`
  
        {{terminal()}}

        ???help "Solution"

            Remarquez qu'on associe à un clé, un tableau de valeurs.

            ```python 
            genre = {}
            genre['Pulp Fiction'] = ['Tarantino', 1994]
            genre['Kill Bill'] = ['Tarantino', 2003]
            genre['Holy Grail'] = ['Monty Python', 1975]
            ```

            Je déconseille ici la solution sur une ligne, difficile à lire.

## Manipuler des dictionnaires

!!! {{cours()}}

    Pour accéder à la valeur associée à une clé, on utilise la syntaxe : `#!python un_dico[clé]`

    Pour ajouter ou modifier la valeur associée à une clé, on fait simplement : `#!python un_dico[clé] = nouvelle_valeur`

    !!!example "Exemple"
    
        Dans le programme ci-dessous, un dictionnaire a été défini. Sans modifier la ligne de définition,
        
        - afficher la valeur associée à la clé `#!python gamma` ;
        - corriger les valeurs associées aux clés `#!python alpha` et `#!python beta` (respectivement, `#!python a` et `#!python b`).
        - ajouter la clé `#!python delta` associée à `#!python d`.

        {{IDE('python7/exemple1')}}

!!! {{exercice()}}

    On modélise un panier de fruits de la manière suivante : 

    - les clés sont les noms des fruits ;
    - les valeurs sont la quantité de fruit.

    Créer une fonction `#!python liste_de_course` qui prend en paramètres un dictionnaire `#!python panier` et un fruit `#!python fruit` et qui écrit un fruit à acheter dans un dictionnaire. La quantité par défaut est 0. 

    {{IDE('python7/exo1')}}


!!! {{cours()}}

    On peut boucler sur les clés d'un dictionnaire à l'aide de cette syntaxe.

    ```python
    for clé in un_dictionnaire:
        print(clé)
    ```

    !!!example "Exemple"

        - Reprendre votre liste de course obtenue à l'exercice précédent et, à l'aide d'une boucle sur les clé, afficher tous les fruits que vous devez acheter.
        - En ajoutant une instruction, afficher quelles sont les quantités actuellement présentes dans votre panier (cela devrait être 0).

        {{IDE()}}

        ???help "Solution"

            ```python
            for fruit in panier_de_fruits:
                quantité = panier_de_fruits[fruit]
                print(fruit, quantité)
            ```



!!! {{exercice()}}

    Continuons sur ce panier de fruits. 
    
    On peut tester si une clé est présent dans un dictionnaire simplement en le demandant gentiment : `#!python clé in un_dictionnaire`.

    Créer une fonction `#!python ajouter_fruit` qui prend en paramètres un dictionnaire `#!python panier` et un fruit `#!python fruit` et qui ajoute un fruit dans un dictionnaire. Si un fruit est déjà présent dans le panier, la quantité est augmentée de 1. Sinon, on affiche un message d'erreur : `#!python Ce fruit n'est pas sur la liste de courses`.

    {{IDE('python7/exo2')}}


!!! {{exercice()}}

    Continuons encore sur ce panier de fruits. 
    
    En utilisant la fonction `#!python ajouter_fruit` et une boucle, créer une fonction `#!python avalanche_de_fruits` qui prend en paramètres un dictionnaire `#!python panier` et qui ajoute 1 à la quantité de tous les fruits présents dans le dictionnaire `#!python panier`. 

    {{IDE('python7/exo3')}}

## Parcours particuliers

!!! {{cours()}}

    De temps en temps, on souhaite parcourir les valeurs plutôt que les clés. On réalise cette opération à l'aide de la syntaxe suivante :

    ```python
    for valeur in un_dictionnaire.values():
        print(valeur)
    ```

    ???+example "Exemple"

        Faire la moyenne des valeurs du dictionnaire :

        {{IDE('python7/exemple2')}}

        ???help "Solution"

            ```python
            moyenne_FV = {'1G1' : 12, '1G2' : 14.3, '1G3' : 15.6, '1G4' : 11.3}

            moyenne = 0
            for note in moyenne_FV.values():
                moyenne = moyenne + note / len(moyenne_FV)

            print(moyenne)

    De temps en temps, on souhaite parcourir les clés et les valeurs simultanément. On réalise cette opération à l'aide de la syntaxe suivante :

    ```python
    for clé, valeur in un_dictionnaire.items():
        print(clé, valeur)
    ```