# Fonctions

## Principe

!!! example "Utilité des fonctions"

    Le programme suivant permet de convertir une température de degré _Fahrenheit_ vers degré _Celsius_.

    ```python
    temp_fahrenheit = 60
    temp_celsius = temp_fahrenheit - 32 * (5/8)
    ```

    - [ ] Dans le terminal ci-dessous, tester ce programme pour convertir 60 degrés Fahrenheit en degrés Celsius. Afficher la valeur référencée par la variable `#!python temp_celsius`.
    - [ ] On souhaite maintenant convertir 90 et 120 degrés Fahrenheit en degrés Celsius. Ajouter les lignes correspondantes.

    {{terminal()}}

    ??? help "Solution"

        ```python
        temp_fahrenheit = 60
        temp_celsius = temp_fahrenheit - 32 * (5/8)
        print(temps_celsius)
        temp_fahrenheit = 90
        temp_celsius = temp_fahrenheit - 32 * (5/8)
        print(temps_celsius)
        temp_fahrenheit = 120
        temp_celsius = temp_fahrenheit - 32 * (5/8)
        print(temps_celsius)
        ```
        
        On remarque qu'il y a beaucoup de répétitions dans le code. Cela ne va pas être pratique à modifier si on a fait une erreur dans la formule.


Le **principe DRY** est encore ici à l'oeuvre : la structure _fonction_ permet de simplifier un programme en évitant les répétitions inutiles et complexes à débogger.

Remarquons que cette structure rend également le code plus _abstrait_.

!!! tip "Exo à réutiliser"

    Le programme suivant permet de comparer la longueur des deux mots "classique" et "clanique". Il affiche une phrase-réponse comparant le nombre de lettres dans les deux mots. 

    {{IDE('python4/exo1')}}

    Dans le même programme, on souhaite aussi comparer la longueur des mots "moderne" et "baderne". Modifiez le code précédent pour réaliser cela.

    ??? help "Solution"

        {{IDE('python4/corr_exo1')}}


## Définir une fonction

## Passage de paramètres

0 paramètres -> procédure
1 paramètres
passage par mot-clé

## Renvoi de résultats

!!! danger "Important"

    Jusqu'à présent, nos fonctions n'ont servi qu'à faire de **l'affichage** : les résultats de ces fonctions ne peuvent en aucun cas être réutilisés dans un autre calcul !

Indiquer ici la problématique de sortie anticipée

## Variables locales et globales

Global : uniquement pour les constantes pour éviter les EFFETS de BORD 

## Résumé

!!! danger "Résumé"

    Dans ce chapitre, j'ai appris : 
    
    - [ ] blabla
    - [ ] blabla
    - [ ] blabla
    - [ ] blabla
    - [ ] blabla

!!! danger "Une anecdote"

    En 1973, un robot est envoyé sur la Lune pour collecter des données. Celui-ci, une fois arrivé, affiche les données sur son écran avec l'équivalent de `#!python print`. 
    
    Rien n'a été renvoyé sur Terre car l'équivalent de `#!python return` n'a pas été utilisé ! 
    
    En général, on souhaite faire quelque chose de nos données, pas les afficher.