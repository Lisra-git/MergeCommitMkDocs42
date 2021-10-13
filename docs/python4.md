# Fonctions

Ce chapitre est la **pierre angulaire** de tout langage informatique !

## Principe

!!! exo "Pourquoi les fonctions ?"

    Les lignes suivantes permettent de convertir une température de degré _Fahrenheit_ vers degré _Celsius_.

    ```python
    temp_fahrenheit = 60
    temp_celsius = temp_fahrenheit - 32 * (5/8)
    ```

    - [ ] Dans le terminal ci-dessous, tester ce programme pour convertir 60 degrés Fahrenheit en degrés Celsius. Afficher la valeur référencée par la variable `#!python temp_celsius`. **Pro tip** : dans la console, utiliser la touche ++tab++ pour compléter un mot dont vous aurez écrit le début. `#!python temp_f` + ++tab++ doit écrire `#!python temp_fahrenheit`.
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
        
        On remarque qu'il y a beaucoup de répétitions dans le code, même si nous avons utilisé des variables. Notez que l'on pourrait éventuellement utiliser une boucle : 

        ```python
        for temp_fahrenheit in [60, 90, 120]:
            temp_celsius = temp_fahrenheit - 32 * (5/8)
            print(temps_celsius)
        ```

        Il est toutefois difficile de comprendre ce que fait ce programme.

Le **principe DRY** va encore être ici à l'oeuvre : la structure _fonction_ va permettre de simplifier un programme en évitant les répétitions inutiles et complexes à débogger. Cette structure va rendre également le code plus _abstrait_.

!!! {{cours()}}

    Une _fonction_ permet de créer des blocs d'instructions que nous pouvons réutilisons quand nous le souhaitons. C'est une boite noire indépendante du reste d'un programme :

    - nous pouvons la tester et contrôler son fonctionnement de manière indépendante ;
    - elle découpe le problème en sous-problème plus simple à résoudre ;
    - nous pouvons la réutiliser dans d'autres programmes.

    ???+ example "Exemple"

        Pour construire une voiture, on ne fait pas tout en même temps :
        
        - on a par exemple besoin de convertir de l'énergie thermique (ou électrique) en énergie mécanique. Pour cela, on "crée" une fonction nommée `#!python convertir_énergie_thermique_en_énergie_mécanique` qu'on appelle aussi le moteur ;
        - la conversion de l'énergie thermique en énergie mécanique va fonctionner car le moteur a été testé de manière indépendante lors du développement du modèle de voiture ;
        - on le réutilise ensuite pour la production à la chaîne.

    Nous nommerons nos _fonctions_ avec des noms d'action : `#!python calculer_moyenne`, `#!python trier_tableau` ou `#!python afficher_résultats`.


## Définir une fonction

!!! {{cours()}}

    Pour définir une fonction en Python, on utilise la syntaxe suivante :
    ```python 
    def nom_de_la_fonction(parametre1, parametre2, ... ):
        ... instructions ...
        ... instructions ...
        ... instructions ...
        return résultat1, résultat2, ...
    ```

    Une fois `#!python def`inie, la fonction appelée `#!python nom_de_la_fonction` peut être utilisée n'importe où dans le programme.

    En Python, l'indentation des instructions appartenant à la fonction est **obligatoire**.

    !!! danger "Important"
    
        `#!python return` est l'instruction permettant de renvoyer des résultats en dehors de la fonction. 
        
        Toute variable non renvoyée par `#!python return` sera perdue dans la boîte noire !


Nous allons tout de suite étudier divers cas particuliers importants.

## Exemple de fonctions

!!! danger "Important"
    
    Dans ma grande bonté, je vous propose quelquefois des fonctions vides (on appelle cela un prototype). Pour éviter une erreur, le mot-clé `#!python pass` est utilisé : il indique à Python de ne rien faire. Quand vous commencez à écrire la fonction, supprimez `#!python pass`.


### Fonction sans paramètres

Les fonctions sans paramètres sont des **raccourcis** pour éviter de retaper plusieurs fois les mêmes instructions. Leur utilité est très limitée : si vous les utilisez, ce sera pour des utilisations très spécifiques.

!!! exo "Exercice"

    === {{exercice(False, 0)}}

        On donne la fonction ci-dessous.

        - [ ] Exécuter le programme.
        - [ ] Dans la console, écrire `#!python compter()` (on dit que vous **appelez** la fonction `#!python compter()`).
        - [ ] Observer le résultat et comprendre ce qu'il s'est passé.
        - [ ] Dans la console, faire deux autres appels à la fonction `#!python compter()`. Que remarquez-vous ?

        {{IDEv("python4/exemple1")}}

        ??? help "Remarque"

            Quand vous avez appelé la fonction dans la console, Python a regardé quelque part dans la mémoire s'il existait une fonction appelée `#!python compter()`. Il l'a trouvé car nous avons exécuté le programme : ensuite la fonction se déroule. 
            
            Cette fonction affiche des informations et ne renvoie aucune valeur : on lui demande de renvoyer la valeur `#!python None`.


    === {{exercice(False)}}

        On donne la fonction ci-dessous.

        - [ ] Sans l'exécuter, dire ce que permet de faire la fonction écrite dans l'éditeur.
        - [ ] Exécuter le programme.
        - [ ] Dans la console, afficher la valeur de `#!python vitesse_lumière`.
        - [ ] Modifier le programme en remplaçant la ligne 5 par `#!python vitesse_lumière = c`. Exécuter le programme et comprendre l'erreur affichée.

        {{IDEv("python4/exo2")}}

        ??? help "Remarque importante"

            Une variable peut référencer la valeur renvoyée par une fonction. C'est ce que fait : `#!python vitesse_lumière = calculer_célérité()`. 
            
            Remarquez toutefois que lorsque vous avez écrit `#!python vitesse_lumière = c`, vous avez obtenu une erreur : `#!python NameError: name 'c' is not defined`. Cela signifie que la variable `#!python c` n'existe pas en dehors de la fonction.

    === {{exercice(False)}}

        La course des Animaux est un jeu qui permet de déplacer trois types d'animaux sur un plateau : 
        
        - le Zèbre a 1 chance sur 2 de se déplacer de 6 cases ou de reculer d'une case ;
        - le Lion a 1 chance sur 2 de se déplacer de 5 cases ou de ne pas se déplacer du tout ;
        - l'Éléphant a 1 chance sur 4 de se déplacer de 4 cases, et sinon, il se déplace de 2 cases.  
         
        En vous inspirant de la fonction ci-dessous, écrire une fonction `#!python calculer_déplacement_lion` et `#!python calculer_déplacement_éléphant` permettant de calculer le déplacement du Lion et de l'Éléphant.

        {{IDE("python4/exo3")}}

    === {{exercice(False)}}

        - [ ] Compléter la fonction `#!python placer_aléatoirement`. Elle renvoie :  
            - un entier aléatoire `#!python x` compris entre 0 et 700 ;
            - un entier aléatoire `#!python y` compris entre 0 et 400. 
        - [ ] Compléter la fonction `#!python choisir_couleur`. Elle renvoie :
            - `#!python 'red'` si n vaut 0 ; 
            - `#!python 'green'` si n vaut 1 ; 
            - `#!python 'blue'` si n vaut 2 ; 
            - `#!python 'purple'` si n vaut 3.
        - [ ] Exécuter le script. Dans la console, appeler la fonction `#!python créer_tache` et observer le résultat. Comprendre l'affichage.
        - [ ] Dans la console, faire une boucle inconditionnelle appelant 10 fois la fonction `#!python créer_tache`.
             
        {{IDEv("python4/exo4")}}

!!! {{cours()}}

    Ce

### Fonction avec paramètres


0 paramètres -> procédure
1 paramètres
passage par mot-clé

### Et si on n'a rien à renvoyer ?


### Paramètres multiples

    !!! {{cours()}}



## Utilisation de `#!python return`

!!! {{cours()}}

    Il est possible de mettre plusieurs `#!python return` dans une seule fonction.

    Dans ce cas, `#!python return` est comme un siège éjectable : dès que le programme voit une instruction commençant par `#!python return`, la fonction s'arrête !

    ???+ example "Exemple"

        dd

!!! danger "Danger mortel"

    N'oubliez pas le `#!python return` ! Si vous n'utilisez que des `#!python print`, vous ne faîtes que de **l'affichage** : les résultats de ces fonctions ne pourront en aucun cas être réutilisés dans un autre calcul !

!!! exo "Exercices sur `#!python return`"

    === {{exercice(False)}}

    === {{exercice(False)}}


## Variables locales et globales

!!! {{cours()}}

    On appelle portée d'une variable l'ensemble des endroits du programme où elle existe.
    Most frequently, name resolution relies on an "inner-to-outer context" rule, such as the Python LEGB (Local, Enclosing, Global, Built-in) rule: names implicitly resolves to the narrowest relevant context. In some cases name resolution can be explicitly specified, such as by the global and nonlocal keywords in Python; in other cases the default rules cannot be overridden.
Global : uniquement pour les constantes pour éviter les EFFETS de BORD 



!!! exo "Exo à réutiliser"

    Le programme suivant permet de comparer la longueur des deux mots "classique" et "clanique". Il affiche une phrase-réponse comparant le nombre de lettres dans les deux mots. 

    {{IDE('python4/exo1')}}

    Dans le même programme, on souhaite aussi comparer la longueur des mots "moderne" et "baderne". Modifiez le code précédent pour réaliser cela.

    ??? help "Solution"

        {{IDE('python4/corr_exo1')}}

## Documentation d'une fonction

!!! {{cours()}}

    Nommer clairement une fonction est fondamental mais il convient également de **documenter** toutes les fonctions que vous faites.

    Documenter permet d'expliquer aux personnes qui ne sont pas familières avec vos fonctions de les comprendre : 

    - que fait-elle ?
    - de quels types sont les paramètres ?
    - un petit exemple.

    Attention à ne pas trop documenter !

    ???+ example "Exemple"

        === "Trop de documentation"
            ```python
            def calculer_carré(x):
                """Calcule le carré d'un nombre

                Paramètres :
                x -- flottant ou entier

                Exemple :
                nombre = calculer_carré(2.0)
                """
                return x**2
            ```

        === "Documentation correcte"
            ```python
            def calculer_carré(x):
                """Calcule le carré d'un nombre flottant ou entier"""
                return x**2
            ```

        === "Trop peu de documentation"
            ```python
            def f(x):
                return x**2
            ```

    Souvent... **Vous** allez être la personne nécessitant la documentation. Rien de plus frustrant que de revenir sur un de vos codes non documenté et de passer quelques heures à retrouver comment il fonctionne.

    ![Thor vous apprend à documenter](images/python4/Thor.jpeg "Écoutez Thor"){: style="width:40%"}
    ![Frodon vous apprend à documenter](images/python4/Frodo.jpeg "Écoutez Frodon"){: style="width:45.2%"}

!!! exo "Exercice"

    === {{exercice(False)}}

        def appartenir_cercle(x, y, R):


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