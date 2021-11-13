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

        Dans ce cas, on indique quelle est la forme générale de l'élément du tableau et on utilise une boucle `#!python for` à l'intérieur des crochets.

        !!! example "Exemple"
        
            On veut générer un tableau contenant 10 nombres pairs. 
            
            Les nombres pairs sont de la forme $2\times n$.

            ```python 
            tableau_de_pairs = [2*n for n in range(10)]            
            ```

            `#!python 2*n` est la forme générale.

    {{terminal()}}

!!! exo "Exercices d'application directe"

    === {{exercice(False)}}

        Dans l'IDE ci-dessous, créer un tableau `#!python tableau_de_0` contenant 1000 fois le nombre 0 puis, l'afficher avec l'instruction `#!python print`.

        ??? help "Solution"
            
            `#!python tableau_gateau = [0]*1000`
    
    === {{exercice(False)}}

        Dans l'IDE ci-dessous, créer un tableau `#!python tableau_de_a` contenant 25 fois le caractère `#!python "a"` puis, l'afficher avec l'instruction `#!python print`.


    === {{exercice(False)}}

        Dans l'IDE ci-dessous, créer un tableau `#!python tableau_impairs` contenant les 25 premiers nombres impairs. Afficher ce tableau.

        ??? help "Aide"

            Les nombres impairs sont de la forme $2\times n+1$.

    === {{exercice(False)}}

        Dans l'IDE ci-dessous, créer un tableau `#!python tableau_carré` contenant les 100 premiers nombres carrés. Afficher ce tableau.    

    {{IDE()}}

## Parcours d'un tableau

Un tableau est utile dans la mesure où nous pouvons accéder aux éléments un par un. Nous utiliserons ces éléments pour calculer quelque chose (moyenner des notes, sélectionner des données, générer des phrases aléatoires...) ou pour les modifier (cours de bourse, modification de notes...).

### Accès à un élément du tableau

!!! {{cours()}}

    !!! warning "Important"

        On appelle taille d'un tableau son nombre d'éléments. La taille d'un tableau `#!python T` est obtenu avec l'instruction `#!python len(T)`.

    Chaque élément d'un tableau est repéré par un indice commençant à 0 et terminant donc à `#!python len(T) - 1`

    !!! example "Exemple"
        
        Prenons le tableau `#!python T = ['b', 'l', 'a', 'c', 'k']`.

        On peut représenter ce tableau Python dans un tableau :
        
        |indice|0|1|2|3|4|
        |-|-|-|-|-|-|
        |tableau|`#!python 'b'`|`#!python 'l'`|`#!python 'a'`|`#!python 'c'`|`#!python 'k'`|
        |lettre|`#!python T[0]`|`#!python T[1]`|`#!python T[2]`|`#!python T[3]`|`#!python T[4]` ou `#!python T[len(T) - 1]`|

        Pour accéder à la lettre d'indice `#!python 0`, on va donc écrire `#!python T[0]`. 

        Pour accéder à la lettre d'indice `#!python 1`, on va donc écrire `#!python T[1]`. 

        ...

        Pour accéder à la lettre d'indice `#!python i`, on va donc écrire `#!python T[i]`. 

        ...

        Pour accéder à la dernière lettre, on va donc écrire `#!python T[len(T) - 1]`, car `#!python len(T) - 1` est l'indice du dernier élément.       


### Parcours

!!! {{cours()}}
  
    Pour lire les éléments d'un tableau, on utilise toujours une boucle inconditionnelle `#!python for`.

    Deux modes de lecture :

    === "Parcours par valeurs"

        Le parcours par valeurs est utile lorsque l'on souhaite utiliser les valeurs, indépendamment de leurs positions dans le tableau.

        Par exemple :

        {{IDEv("python5/exemple1")}}

        ou, initialisant le tableau avant la boucle :

        {{IDEv("python5/exemple2")}}


    === "Parcours par indice"

        Lorsque la position des éléments est importante, on réalise un parcours par indice.

        On utilise une boucle `#!python for`, avec un indice de boucle `#!python i` allant de 0 jusqu'à la  `#!python len(T)` exclus. 

        Pour cela nous utiliserons la syntaxe : 
        ```python
        for i in range(len(T)):
        ```

        Par exemple :

        {{IDEv("python5/exemple3")}}

        {{IDEv("python5/exemple4")}}

!!! exo "Exercices d'application directe"

    === {{exercice(False)}}

        Dans l'IDE ci-dessous, recopier le tableau suivant : `#!python animaux = ["girafe", "tigre", "singe", "souris"]`. 
        En utilisant les bons indices, afficher `#!python "tigre"` et `#!python "souris"`.

        ??? help "Solution"
            
            ```python 
            animaux = ["girafe", "tigre", "singe", "souris"]

            taille = len(animaux)

            print(animaux[1])
            print(animaux[3])
            # ou print(animaux[taille - 1])
            ```

    === {{exercice(False)}}

        Dans l'IDE ci-dessous, créer un tableau `#!python tableau_de_10` contenant 7 fois le nombre 10 puis, l'afficher, **ligne par ligne**, avec l'instruction `#!python print`. On utilisera un parcours par valeurs.

        ??? help "Solution"
            
            ```python 
            tableau_de_10 = [10]*7

            for nombre in tableau_de_10:
                print(nombre)
            ```

    === {{exercice(False)}}

        Dans l'IDE ci-dessous: 
        
        - [ ] créer un tableau `#!python tableau_de_cubes` contenant les 13 premiers cubes parfaits ($0^3, 1^3, 2^3, 3^3$...). 

        - [ ] créer une variable `#!python taille` donnant le nombre d'éléments du tableau.
        
        - [ ] afficher tous les éléments du tableau ligne par ligne en le parcourant par indice. On affichera également l'indice de l'élément.

        Par exemple, avec le tableau `#!python [4,5,6]`, on aura l'affichage :
        ```bash
        0 4
        1 5
        2 6
        ```

        ??? help "Solution"
            
            ```python 
            tableau_de_cubes = [i**3 for i in range(13)]

            taille = len(tableau_de_cubes)

            for i in range(taille)
                print(i, tableau_de_cubes[i])
            ```

    === {{exercice(False)}}

        Dans l'IDE ci-dessous: 

        - [ ] créer une **variable** `#!python alphabet` de `#!python "a"` à `#!python "z"` contenant toutes les lettres de l'alphabet. Créer un tableau `#!python tableau_alpha` contenant chaque lettre de l'alphabet doublé. 
        
        Exemple : `#!python tableau_alpha = ['aa', 'bb', 'cc'...]`.

        - [ ] créer une variable `#!python taille` donnant le nombre d'éléments du tableau.

        - [ ] afficher ensuite ligne par ligne chaque élément de votre tableau en indiquent son indice.

        ??? help "Aide 1"

            `#!python alphabet = "abcdef..."` puis faire une création de tableau en compréhension avec une boucle `#!python for` parcourant alphabet !

        ??? help "Aide 2"

            Pour écrire une lettre deux fois, on doit la multiplier par 2 !

        ??? help "Solution"
            
            ```python 
            alphabet = "abcdefghijklmnopqrstuvwxyz"

            tableau_alpha = [lettre*2 for lettre in alphabet]
            taille = len(tableau_alpha)

            for i in range(taille)
                print(i, tableau_alpha[i])
            ```

    {{IDE()}}

!!! {{exercice(True)}}

    Nous allons essayer de trouver l'indice de l'élément maximum d'un tableau de nombres `#!python T`. L'exercice consiste à écrire en Python l'algorithme ci-dessous en utilisant ce que vous avez appris sur les tableaux.

    On écrira cet algorithme dans la fonction `#!python trouver_maximum`.

    1. Créer une variable `#!python maximum` et l'initialiser à l'élément n° 0 de `#!python T`. Cette variable représente la valeur du maximum.
    2. Créer une variable `#!python indice_maximum` et l'initialiser à 0. Cette variable représente l'indice du maximum.
    3. On parcourt par indice tous les éléments de `#!python T` :
          1. Si l'élément numéro i de `#!python T` est plus grand que `#!python maximum` :
             -  `#!python maximum` prend la valeur de l'élément numéro i de `#!python T`. 
             -  `#!python indice_maximum` prend la valeur de l'indice i. 
          2. Sinon, on ne fait rien.
    4. On renvoie `#!python indice_maximum`.

    L'appel à un tableau vous est donné. 

    Que devez-vous écrire pour trouver la valeur du maximum une fois son indice obtenu ?

    {{IDE('python5/exo8')}}

!!! {{exercice(True)}}

    Faire la même chose que l'exercice précédent mais cette fois-ci, on ne s'intéresse qu'à la **valeur** du maximum.

    Peut-on retrouver l'indice du maximum ?

    {{IDE('python5/exo9')}}

## Modification d'un tableau

Une partie en TP la semaine prochaine : à venir

## Conclusion