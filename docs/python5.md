# Tableaux et tuples

## Principe

De nos jours, l'informatique a pour but de collecter et de manipuler des données. Ces données, en nombre très important, doivent pouvoir être organisées dans des structures composites, faciles d'utilisation.

???+ example "Exemple"

    !!! tip inline end "Température"
        |Mois|Temp.|
        |--|--|
        |Jan.|27|
        |Fév.|28|
        |Mars|29|
        |Avril|27|
        |Mai|27|
        |Juin|25|
        |Juil.|24|
        |Août|25|
        |Sept.|25|
        |Oct.|26|
        |Nov.|26|
        |Déc.|28|

    On mesure la température chaque mois de 2020 dans une île du Pacifique et on l'organise dans un tableau.

    On souhaite ensuite utiliser ces données en Python.

    Une première solution est de créer 12 variables pour les 12 mois de l'année :
    ```python
    temp_01 = 27
    temp_02 = 28
    temp_03 = 29
    temp_04 = 27
    temp_05 = 27
    temp_06 = 25
    temp_07 = 24
    temp_08 = 25
    temp_09 = 25
    temp_10 = 26
    temp_11 = 26
    temp_12 = 28    
    ```

    Cette méthode ne respecte absolument pas le principe **DRY**. 
    
    Et que va-t-il se passer si on souhaite maintenant comparer l'année 2020 avec :
    
    ??? exo "l'année 2019 ?"

        On renomme nos variables `#!python temp_01_2020` et `#!python temp_01_2019`. Cela nous fait 24 variables à gérer.

    ??? exo "les années 2019 et 2018 ?" 

        On renomme nos variables `#!python temp_01_2020`, `#!python temp_01_2019` et `#!python temp_01_2018`. Cela nous fait 36 variables à gérer.

    ??? exo "les 50 dernières années ?"

        On part à la pêche. Ça devient ingérable.

Plutôt que d'envisager chacune de ces données comme représentée par une unique variable, nous allons considérer le tableau complet comme une variable[^th].

[^th]: Souvenez-vous : lorsque le principe DRY n'est plus respecté, il faut souvent créer ou faire appel à de nouvelles structures.

## Création d'un tableau

Un tableau est une structure de données qui contient un ensemble de valeurs.

Schématiquement, il existe deux types de tableaux :

- les tableaux statiques dont la taille est fixée ;
- les tableaux dynamiques dont la taille est variable.

!!! {{cours()}}

    Pour créer un tableau de valeurs, on écrit entre crochets chaque valeur, séparée par des virgules.

    Par exemple :

    ```python 
    tableau_lettre = ['a', 'b', 'c', 'd', 'e']
    tableau_entier = [3, 5, 2, 56, 12]
    ```

!!! exo "Exercices d'application directe"

    === {{exercice(False, 0)}}

        Dans le terminal ci-dessous, créer un tableau `#!python tableau_gateau` contenant les trois ingrédients nécessaires à la réalisation d'un bon gateau (`#!python "farine"`, `#!python "sucre"`, `#!python "lait"`).

        ??? help "Solution"
            
            `#!python tableau_gateau = ["farine", "sucre", "lait"]`

    === {{exercice(False)}}

        Dans le terminal ci-dessous, créer un tableau `#!python tableau_impair` contenant les 5 premiers nombres impairs.

        ??? help "Solution"

            `#!python tableau_entier = [1, 3, 5, 7, 9]`

    {{terminal()}}

!!! {{cours()}}

    La méthode ci-dessus n'est pas idéal lorsque l'on souhaite créer des tableaux de grande taille. 
    
    Il existe alors deux méthodes :

    === "Initialisation rapide"

        On initialise rapidement un tableau à l'aide de l'instruction étoile `#!python *` qui permet de dupliquer un élément un nombre fixé de fois.

        Exemple (à essayer dans le terminal):
        ```python 
            tableau_de_1 = [1]*50
            tableau_de_1 = ["a"]*40
        ```

    === "Initialisation en compréhension"

        On initialise de manière **précise** un tableau à l'aide d'une initialisation en compréhension.

        Dans ce cas, on identique quelle est la forme de l'élément du tableau. Par exemple, on veut générer un tableau contenant 10 nombres pairs. 
        
        Les nombres pairs sont de la forme $2\times n$.

        Exemple (à essayer dans le terminal):
        ```python 
            tableau_de_pairs = [2*n for n in range(10)]            
        ```

    {{terminal()}}

!!! exo "Exercices d'application directe"

    === {{exercice(False)}}

        Dans l'IDE ci-dessous, créer un tableau `#!python tableau_de_0` contenant 1000 fois le nombre 0 puis, l'afficher avec l'instruction `#!python print`.

        ??? help "Solution"
            
            `#!python tableau_gateau = [0]*1000`
    
    === {{exercice(False)}}

        Dans l'IDE ci-dessous, créer un tableau `#!python tableau_de_0` contenant 1000 fois le nombre 0 puis, l'afficher avec l'instruction `#!python print`.


    {{IDE()}}

## Parcours d'un tableau

Un tableau est utile dans la mesure où nous pouvons accéder aux éléments un par un. Nous utiliserons ces éléments pour calculer quelque chose (moyenner des notes, sélectionner des données, générer des phrases aléatoires...).

!!! {{cours()}}

    Chaque élément d'un tableau est repéré par un indice commençant à 0.

    Par exemple :

    Pour lire les éléments d'un tableau, on utilise une boucle inconditionnelle `#!python for`.

    Deux modes de lecture :

    === "Lecture par valeurs"

        Par exemple :

        ```python 
        for lettre in ['a', 'b', 'c', 'd', 'e']:
            print(lettre)
        ```
        On peut aussi écrire

        for 
        tableau_entier = [3, 5, 2, 56, 12]
        ```
    === "Lecture par indice"

    {{terminal()}}

## Modification d'un tableau


## Conclusion