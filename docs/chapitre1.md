# Variables

## Éditeur, console, terminal ?

Un terminal est une invite de commandes permettant à l'homme et à la machine de communiquer de manière interactive.

Pour programmer, il existe deux grands types d'outils :

- la console (aussi appelé interpréteur) permet de réaliser des calculs, des tests rapides ainsi que des programmes courts. On ne sauvegarde pas son travail ;
- l'éditeur de code permet d'écrire un programme complexe dans un langage donné et de sauvegarder son travail. Il est souvent combiné à un interpréteur afin d'exécuter le programme et de le rendre compréhensible par l'ordinateur.

!!! example "Exemple"

    === "Une console"

        - [ ] Calculez la somme de 134 et de 5677 dans la console. Pour valider, appuyez sur ++enter++. 
        - [ ] Faites également leur multiplication à l'aide du symbole `*`.

        {{terminal()}}

    === "Un éditeur de code"

        Lancez le script à l'aide de la flèche.

        {{REPLv('c1/ex1')}}
    

Au fur et à mesure de votre apprentissage, vous utiliserez des éditeurs de code de plus en plus perfectionnés :

1. ce site web ;
2. Thonny ;
3. Vscodium.

## Hello World !

!!! tip "Premiers pas"

    === {{exercice(False, 0)}}

        Créons tout de suite notre premier programme[^id]. 
        
        Dans la console ci-dessous, tapez : `#!python print("Hello world !")` et appuyez sur ++enter++.  Que se passe-t-il ?

        [^id]: la tradition d’utiliser hello world comme premier programme de test a été initiée par le livre `The C Programming Language` de Brian Kernighan et Dennis Ritchie, publié en 1978.

    === {{exercice(False)}}

        Dans la console, affichez la phrase "Bonjour le monde !". 

        ??? help "Aide" 
        
            Avez-vous bien utilisé des guillemets comme dans l'exercice précédent ?

    === {{exercice(False)}}

        Dans la console ci-dessous, réalisez la soustraction de 956 et de 649.

        Utilisez l'instruction `#!python print` pour afficher à nouveau le résultat de cette opération.

        ??? help "Aide" 
        
            On ne peut pas soustraire un affichage avec `#!python print`.
            
            Pas de guillemets ici. Voyez-vous quelle est la différence fondamentale entre la soustraction et les phrase des exercices 1 et 2 ?

    {{terminal()}}

!!! warning "Important"

    Vous devez obtenir le même affichage que vous fassiez `#!python 45*4` ou `#!python print(45*4)`. 

    On aurait pu aussi taper "Hello World !" sans `#!python print`.
    
    La console **évalue** des expressions Python puis affiche le résultat de l'évaluation. `#!python print` sera utile pour débugger les programmes plus complexes.

## Notion de variable

Nous évoquons ci-dessous la notion de variable. Celle-ci sera revue en cours en activité débranchée.

!!! {{cours()}}

    !!! info inline end "En mémoire"
        ```mermaid 
        flowchart TD
        subgraph "Avant"
            I[annee] --> A[2010]
            J[envol] --> A[2010]
        end
        ```

        ```mermaid
        flowchart TD
        subgraph "Après"
            annee --> C[2011]
            annee -.-> |X|A[2010]
            envol --> A[2010]
        end
        ```

    Une variable _représente_ une zone de stockage dans la mémoire de l'ordinateur. Elle permet de stocker une valeur numérique, du texte, un tableau de nombres etc. 

    Un humain accède à ces valeurs grâce à un **nom de variable**.

    L'instruction `#!python =` permet de _relier_ un nom de variable avec sa valeur. Ce lien ne fonctionne que dans un sens : de la droite vers la gauche ou ← .

    ```python
    # annee ← 2010 : permet de relier la variable (nommée annee) à une valeur (ici 2010)    
    annee = 2010
    # envol ← 2010 : permet de relier la variable (nommée envol) à une valeur (ici 2010)
    envol = annee  
    # annee ← annee + 1 : permet d'ajouter 1 à la variable nommée annee : sa valeur devient 2011
    annee = annee + 1
    ```

!!! warning "Vocabulaire"

    === "Déclaration"
        Une déclaration est la création d'une variable d'un certain type. 

        !!! example "Exemple"

            En Fortran 90, on déclare des variables `#!fortran pi` et `#!fortran entier` ainsi :
            ```fortran
            real    :: pi
            integer :: entier
            ```

        ??? danger "Pour aller plus loin"

            Dans de nombreux langages de programmation, la déclaration permet de définir le nombre d'octets à réserver en mémoire, sa représentation interne, l'ensemble des valeurs admissibles et l'ensemble des opérateurs qui peuvent lui être appliqués.
        
    
    === "Initialisation"
        Une initialisation est l'association **initiale** d'un contenu (une valeur) avec une variable déclarée préalablement.

        !!! example "Exemple"

            On initialise les variables `#!fortran pi` et `#!fortran entier` :
            ```fortran
            pi = 3.141592
            entier = 42
            ```            

    === "Affectation"
        Une affectation est l'association d'un contenu (une valeur) avec une variable **déjà initialisée**. 

        !!! example "Exemple"

            On affecte de nouvelles valeurs aux variables `#!fortran pi` et `#!fortran entier` :
            ```fortran
            pi = 6.283184
            entier = 42 * 8
            ```
        
    === "Incrémentation"
        Une incrémentation est l'augmentation régulière de la valeur associée à une variable.

        !!! example "Exemple"
            ```python
            pi = pi + 2   # la variable pi est reliée à l'ancienne valeur de pi augmentée de 2.
            ```

        ??? danger "Pour aller plus loin"
            Ce symbole `=` n'a rien à voir avec le égal mathématique. `#!python a = a + 2` a un sens en Python mais est une proposition logique fausse en Maths.

!!! {{cours()}}
    En Python, la déclaration et l'initialisation se font en même temps. On appelle cela le **typage dynamique**.
    
    Lorsque Python voit `#!python x = 2` : il comprend que x est un entier (déclaration) et que cette variable doit être associée à la valeur 2 (initialisation).

    Par la suite, on peut faire `#!python x = 'Bonjour'` pour associer le mot _Bonjour_ (valeur) à la variable `x`.

    ??? danger "Pour aller plus loin"
        En Python, ces changements de types (passage d'un entier à un mot) se font via le _duck typing_. 

        Pour faire simple, le _duck typing_ permet de faire cela : 

        ![cochon-duck-typing](images/c1/duck_typing.jpg "Duck-typing, très pratique avec assez peu de risques.")


!!! tip "Créer des variables"

    === {{exercice(False)}}

        - [ ] Dans le terminal ci-dessous, créez une variable entière nommée `m` représentant la valeur 7. 
        - [ ] Affichez ensuite cette variable avec le mot-clé Python vu dans la section précédente.

    === {{exercice(False)}}

        - [ ] Dans le terminal ci-dessous, créez une variable réelle nommée `v_init` représentant la valeur 12.7 . 
        - [ ] Affichez ensuite cette variable avec le mot-clé Python vu dans la section précédente.

    === {{exercice(False)}}

        - [ ]  Dans le terminal ci-dessous, créez une variable de type mot nommée `3l3ment` représentant la valeur "Débuter en Python" . 
        - [ ]  Affichez ensuite cette variable avec le mot-clé Python vu dans la section précédente.

        ??? help "Aide"

            Une erreur apparait. Il est interdit de commencer des noms de variables avec des chiffres ou des caractères. Renommez-là !

    === {{exercice(False)}}

        - [ ] Dans le terminal ci-dessous, créez deux variables entières nommées p et q représentant les valeurs 77 et 5. 
        
        - [ ] Affichez d'abord p, puis q avec le mot-clé Python vu dans la section précédente.
        
        - [ ] Comment feriez-vous pour afficher p et q simultanément ?

        !!! help "Astuce"

            En Python, on peut déclarer et initialiser deux variables (ou plus) simultanément. Pour créer `a` et `b`, on ferait : `#!python a, b = 4, 5` .

    === {{exercice(False)}}

        - [ ] Dans le terminal ci-dessous, créez trois variables nommées `n_passager`, `v_moyenne_avion` et `nom_compagnie` représentant les valeurs 237, 977.3, "Air France". 
        - [ ] Affichez simultanément les trois valeurs avec le mot-clé Python vue précédemment.
  
    {{terminal()}}

## Nommage

Dans les exercices précédents, vous avez du remarquer que les variables :

- ne peuvent pas porter n'importe quel nom ;
- pointent vers différents types de données.

!!! {{cours()}}

    En Python, le nom d'une variable doit être choisi parmi les lettres de l'alphabet (minuscule et majuscule étant considérées comme différentes), les chiffres et le symbole `_`. 

    Les espaces ne sont pas autorisés : on utilisera donc l'underscore `_` pour les variables dont le nom est long.

    Le nom d'une variable doit être choisi de façon à être facilement compréhensible par un humain (ni trop court, ni trop détaillé).

    {{REPL('c1/nom_var')}}

    ??? danger "Pour aller plus loin"

        Cette convention de nommage s'appelle le _snake case_ et est préconisé pour Python. 
        
        On écrira donc `#!python nombre_opérations_par_seconde` plutôt que `#!python NombreOpérationParSeconde`.


!!! tip "Vrai/Faux sur le nommage des variables "

    Identifiez les noms de variables valides.

    === "Cocher les identifiants valides"
        - [ ] `pas`
        - [ ] `Roi`
        - [ ] `2ame`
        - [ ] `v413t`
        - [ ] `dix`
        - [ ] `n'œuf`
        - [ ] `huit`
        - [ ] `Sète`
        - [ ] `carte_six`
        - [ ] `_5`
        - [ ] `%4`
        - [ ] `quatre-moins-un`
        - [ ] `2!`
        - [ ] `_`

    === "Solution"
        - [x] `pas`
        - [x] `Roi` ; non conforme au _snake case_ mais valide.
        - [ ] `2ame` ; interdit de commencer par un chiffre.
        - [x] `v413t`
        - [x] `dix`
        - [ ] `n'œuf` ; interdit d'utiliser `'`
        - [x] `huit`
        - [x] `Sète` ; non conforme au _snake case_ mais valide.
        - [x] `carte_six` ; très bon choix !
        - [x] `_5` ; très mal choisi mais valide.
        - [ ] `%4` ; interdit d'utiliser `%`
        - [ ] `quatre-moins-un` ; interdit d'utiliser `-`
        - [ ] `2!` ; interdit d'utiliser `!`
        - [x] `_`

!!! tip "Choisir des noms de variables"

    === {{exercice(False)}}

        - [ ] Dans le terminal ci-dessous, créez une variable entière représentant le nombre de briques de lait stocké dans un entrepot. On l'initialisera à `#!python 10000` briques.
        - [ ] Créez à présent une variable une variable réelle représentant le volume total de toutes ces briques de lait. Pour l'initialiser, on considérera qu'une brique contient `#!python 0.75` L de lait.

        ??? help "Solution"

            - [x] `#!python nombre_briques`, `#!python n_briques`, `#!python n_briques_lait` ou `#!python n_briques_entrepot` sont des noms convenables. 
            - [ ] `#!python nombrebriques`, `#!python nBriquesLait` ou `#!python nombre_de_briques_de_lait_dans_entrepot` ne respectent pas le _snake case_ ou sont trop longs.
            - [x] `#!python volume_total_briques` ou `#!python vol_tot_briques` sont convenables.

    === {{exercice(False)}}

        - [ ] Dans le terminal ci-dessous, créez deux variables entières représentant les coordonnées d'un point A du plan. On initialisera ces variables à `#!python -4` et `#!python 2`.
        - [ ] Créez à présent deux variables représentant les coordonnées d'un vecteur $\vec{u}$ du plan. On initialisera ces variables à `#!python 2` et `#!python -1`.

        ??? help "Solution"

            - [x] `#!python x` et `#!python y` sont appropriés s'il n'y a qu'un seul point. `#!python x_A` et `#!python y_A` sont également convenable. 
            - [x] `#!python vec_x` et `#!python vec_y` sont appropriés s'il n'y a qu'un seul vecteur. `#!python vec_u_x` et `#!python vec_u_y` sont également convenables. Par contre, `#!python vecX`, `#!python VEC_Y` ou `#!python abscisse_vecteur_u` sont à éviter.

    === {{exercice(False)}}

        Dans le terminal ci-dessous, créez une variable de type tableau représentant l'ensemble des températures du lac Léman relevées sur 4 jours. On initialisera un tableau grâce à `#!python [17.7, 18.1, 18.2, 18.8]`.

        ??? help "Solution"

            `#!python temp_lac` ou `#!python temp_lac_léman` sont appropriés. `#!python temp` pourrait être correct mais reste assez vague et `#!python température_lac_léman_4jours` est trop long. 

    {{terminal()}}

## Types de variables

Dans le début du cours, vous avez remarqué que les variables que l'on manipule ne représentent pas toujours la même valeur.

Dans un langage de programmation, les variables sont **typées** : ce sont des entiers, des _réels_, des tableaux etc. Ce type est défini au moment de la déclaration.

!!! {{cours()}}

    Les types principaux en Python sont :

    - les entiers (relatifs) : type `#!python int` ;
    - les flottants (approximation des nombres réels par des décimaux) : type `#!python float`;
    - les chaines de caractères (mots) : type `#!python str` ;
    - les booléens (`#!python True` ou `#!python False`) : type `#!python bool`.  
    Les booléens sont des variables n'ayant que deux valeurs possibles : Vrai ou Faux.

    ??? danger "Pour aller plus loin"
    
        Nous aurons rapidement besoin d'autres types permettant de décrire des ensembles de données :

        - les n-uplets : type `#!python tuple`.
        - les tableaux : type `#!python list`;
        - les dictionnaires : type `#!python dict`;

!!! {{exercice()}}

    En vous aidant des exercices précédents, déterminez les types des variables ci-dessous : 

    === "Question" 

        | Types | int | float | str | bool |
        |:---------|:-------|:-------|:-----|:------|
        | `#!python p = 8` | {{tit('')}} | {{tit('')}} | {{tit('')}} | {{tit('')}} |
        | `#!python nom = "Von Neumann"` | {{tit('')}} | {{tit('')}} | {{tit('')}} | {{tit('')}} |
        | `#!python e = 2.7172` | {{tit('')}} | {{tit('')}} | {{tit('')}} | {{tit('')}} |
        | `#!python p = 8.0` | {{tit('')}} | {{tit('')}} | {{tit('')}} | {{tit('')}} |
        | `#!python huit = "8"` | {{tit('')}} | {{tit('')}} | {{tit('')}} | {{tit('')}} |
        | `#!python r = 0` | {{tit('')}} | {{tit('')}} | {{tit('')}} | {{tit('')}} |
        | `#!python r = -120000` | {{tit('')}} | {{tit('')}} | {{tit('')}} | {{tit('')}} |
        | `#!python arrivé = True` | {{tit('')}} | {{tit('')}} | {{tit('')}} | {{tit('')}} |
        | `#!python huit = "8.0"` | {{tit('')}} | {{tit('')}} | {{tit('')}} | {{tit('')}} |
        | `#!python mort = "False"` | {{tit('')}} | {{tit('')}} | {{tit('')}} | {{tit('')}} |

    === "Solution" 

        | Types | int | float | str | bool | explication |
        |:---------|:-------|:-------|:-----|:------|:------|
        | `#!python p = 8` | {{tit('x')}} | {{tit('')}} | {{tit('')}} | {{tit('')}} ||
        | `#!python nom = "Von Neumann"` | {{tit('')}} | {{tit('')}} | {{tit('x')}} | {{tit('')}} ||
        | `#!python e = 2.7172` | {{tit('')}} | {{tit('x')}} | {{tit('')}} | {{tit('')}} |La virgule des flottants est un point.|
        | `#!python p = 8.0` | {{tit('')}} | {{tit('x')}} | {{tit('')}} | {{tit('')}} |La virgule des flottants est un point.|
        | `#!python huit = "8"` | {{tit('')}} | {{tit('')}} | {{tit('x')}} | {{tit('')}} |Les guillemets indiquent un `#!python str`.|
        | `#!python r = 0` | {{tit('x')}} | {{tit('')}} | {{tit('')}} | {{tit('')}} |`#!python 0` est un entier.|
        | `#!python r = -120000` | {{tit('x')}} | {{tit('')}} | {{tit('')}} | {{tit('')}} |`r` est un entier négatif donc relatif.|
        | `#!python arrivé = True` | {{tit('')}} | {{tit('')}} | {{tit('')}} | {{tit('x')}} |`#!python True` et `#!python False` sont des mots réservés.|
        | `#!python huit = "8.0"` | {{tit('')}} | {{tit('')}} | {{tit('x')}} | {{tit('')}} |Les guillemets indiquent un `#!python str`.|
        | `#!python mort = "False"` | {{tit('')}} | {{tit('')}} | {{tit('x')}} | {{tit('')}} ||

    ??? {{ext()}} 
        Pour connaitre le type d'une variable, on utilise l'instruction `#!python type(......)`. Par exemple, `#!python type(6100)` renvoie `#!python <class 'int'>`.

        {{terminal()}}

On peut changer le type d'une variable[^idp] :

[^idp]: Ce changement de type est appelé transtypage ou _casting_ .

- en entier en utilisant `#!python int(variable)` ;
- en flottant en utilisant `#!python float(variable)` ;
- en chaine de caractères en utilisant `#!python str(variable)`.

!!! info "À quoi ça sert ?"

    Le transtypage sera particulièrement important lorsque nous lirons des fichiers externes. Toutes leurs données seront en effet considérées comme du texte que nous devrons convertir, au besoin, en données numériques.

## Opérations simples

### Opérations sur les types numériques

!!! {{cours()}}
    En Python, pour les types `#!python int` et `#!python float` :
    
    - les quatre opérations mathématiques de base sont obtenues avec `#!python +, -, *, /` ;
    - les puissances sont obtenues avec `#!python **`;
    - les priorités opératoires sont gérées à l'aide des parenthèses `#!python ()`. **Les crochets ou accolades sont interdits !**

    Les flottants sont _plus généraux_ que les entiers. Ainsi, si on additionne un `#!python int` avec un `#!python float`, nous obtiendrons un `#!python float`. La division donne toujours un `#!python float`.

    {{REPLv('c1/op_num')}}

!!! tip "Opérations"

    === {{exercice(False)}}

        On pose $x = 2$. 
        
        - [ ] Multipliez x par lui-même 5 fois.
        - [ ] Multipliez x par lui-même 10 fois.
        - [ ] Multipliez x par lui-même 67 fois.

        ??? help "Solution"
            ```python
            >>> x = 2
            >>> x*x*x*x*x
            32
            >>> x**10
            1024
            >>> x**67
            147573952589676412928
            ```

    === {{exercice(False)}}

        - [ ] On pose $x = 12.5$. Réalisez le programme de calcul suivant :

        - multipliez $x$ par 4
        - ajoutez 10
        - divisez par 6
        
        - [ ] Faites ce calcul en une ligne en utilisant des parenthèses.

        ??? help "Solution"
            ```python
            >>> x = 12.5
            >>> x*4
            50
            >>> 50+10
            60
            >>> 60 / 6
            10.0
            ``` 
            En une ligne : `#!python (x*4 + 10) / 6`. 

    === {{exercice(False)}}

        - [ ] On pose $x = 3$. On va modifier la valeur référencée par la variable $x$. Réalisez le programme de calcul suivant :

        - $x \leftarrow x+3$ (la nouvelle valeur de $x$ est égale à l'ancienne valeur de $x$ augmentée de 3)
        - $x \leftarrow x \times 3$ (la nouvelle valeur de $x$ est égale à l'ancienne valeur de $x$ multipliée par 3) 
        - $x \leftarrow \dfrac{x}{1.5}$ (la nouvelle valeur de $x$ est égale à l'ancienne valeur de $x$ divisée par 1.5)

        - [ ] Faites ce calcul en une ligne grâce aux parenthèses.

        ??? help "Solution"
            Vous devez trouver `#!python 12.0`.

    === {{exercice(False)}}
        Dans la variable `#!python durée`, on donne une durée en heure. Par exemple, `#!python durée = 2900`.

        Écrire une suite d'opérations permettant de convertir cette durée en jour et en semaine. On stockera ces durées dans les variables `#!python durée_jour` et `#!python durée_semaine`.

        ??? help "Solution"
            Vous devez trouver `#!python durée_jour = durée / 24` et `#!python durée_semaine = durée / 24 / 7`.

    === {{exercice(False)}}

        On choisit deux nombres entiers $a = 88$ et $b=12$. 
        
        On va calculer le quotient $q$ et le reste $r$ de la division euclidienne de $a$ par $b$. 
        
        On rappelle que le quotient est la partie entière (avant la virgule) de $\dfrac{a}{b}$ et que $a = b\times q+r$. Par exemple, $8/3 \approx 2.66666$ donc le quotient vaut 2.

        - Calculez $q \leftarrow \dfrac{a}{b}$
        - Convertissez $q$ en entier avec `#!python int(...)`.
        - À partir de $a, b, q$, calculez la valeur de $r$.

        ??? help "Aide"
            En deux étapes, on fait :
            ```python
            q = a / b
            q = int(q)
            ```
            ou en une étape : `#!python q = int(a/b)`.

        ??? help "Solution"
            `#!python q = 7` et `#!python r = 4`.

    === {{exercice(False)}}

        On reprend l'exercice précédent mais on souhaite calculer le quotient $q$ et le reste $r$ en une seule ligne ! 

        ??? help "Aide"    
            Pour initialiser plusieurs variables sur une ligne, on utilise `#!python var1, var2, var3, ... = 1, 'avion', 3.5, ...`.

        ??? help "Solution"
            `#!python q, r = int(a/b), a - b*int(a/b)`.

    {{terminal()}}

En informatique, on calcule régulièrement des quotients et des restes. Plutôt que d'utiliser les formules complexes trouvées à l'exercice précédent, on utilise :

- `#!python a // b` pour calculer le quotient d'une division euclidienne ;
- `#!python a % b` pour calculer le reste d'une division euclidienne.

!!! {{exercice()}}

    === "Question"

        Calculez le quotient et le reste de la division euclidienne de :
        
        - `#!python 9` et `#!python 2` ; 
        - `#!python 81` et `#!python 3` ;
        - `#!python 102` et `#!python 10` ; 
        - `#!python 21.7` et `#!python 7` ; 
        - `#!python 21.7` et `#!python 7.3`.

    === "Solution"

        Calculez le quotient et le reste de la division euclidienne de :
        
        - `#!python q, r = 9 // 2, 9 % 2` donne : `#!python q, r = 4, 1`; 
        - `#!python q, r = 81 // 3, 81 % 3` donne : `#!python q, r = 27, 0` ;
        - `#!python q, r = 102 // 10, 102 % 10` donne : `#!python q, r = 10, 2`; 
        - `#!python q, r = 21.7 // 7, 21.7 % 7` donne : `#!python q, r = 3.0, 0.6999999999999993` (Bizarre ce reste...); 
        - `#!python q, r = 21.7 // 7.3, 21.7 % 7.3` donne : `#!python q, r = 2.0, 7.1`. `//` et `%` fonctionnent entre flottants.

    {{terminal()}}

### Opérations sur les chaines de caractères

Dans un langage humain, le processus d'écriture consiste en l'**ajout** de mots les uns à la suite des autres.

On peut se répéter en **multipliant** nos propos.

!!! {{cours()}}

    En Python, pour le type `#!python str` :
        
    - l'addition de mots s'obtient avec `#!python +` ;
    - la répétition de mots s'obtient avec `#!python *` ;

    {{REPLv('c1/op_str')}}

!!! tip inline end "Paroles"
    ```
    She's crazy like a fool
    What about it Daddy Cool
    I'm crazy like a fool
    What about it Daddy Cool

    Daddy, Daddy Cool
    Daddy, Daddy Cool
    Daddy, Daddy Cool
    Daddy, Daddy Cool
    
    She's crazy like a fool
    What about it Daddy Cool
    I'm crazy like a fool
    What about it Daddy Cool

    Daddy, Daddy Cool
    Daddy, Daddy Cool
    Daddy, Daddy Cool
    Daddy, Daddy Cool
    ```

!!! {{exercice()}}

    === "Question"
        En utilisant le moins de lignes possibles, reproduisez les paroles de cette célèbre chanson.

        {{REPL('c1/chanson_str')}}

    === "Solution"

        Une solution possible : 

        {{REPL('c1/corr_chanson_str')}}

### Opérations interdites

Certaines opérations sont interdites. L'interpréteur Python va alors vous avertir avec un message d'erreur : il faut apprendre à lire ces messages qui souvent vous expliquent ce qui ne fonctionne pas.

!!! example "Exemples"

    === "Exemple 1"
        ```python
        >>> 4 + '4'
        Traceback (most recent call last):
        File "<console>", line 1, in <module>
        TypeError: unsupported operand type(s) for +: 'int' and 'str'
        ```
        Python nous avertit que l'opérande `#!python +` ne permet être appliqué entre un `#!python int` et un `#!python str`, ce qui est logique : on n'ajoute que des mots entre eux.

    === "Exemple 2"
        ```python
        >>> 'Coucou' * 1.2
        Traceback (most recent call last):
        File "<console>", line 1, in <module>
        TypeError: cannot multiply sequence by non-int of type 'float'
        ```
        Python nous avertit qu'un `#!python str` ne peut pas être multiplié par un `#!python float` (un non-`#!python int`.), ce qui est logique : la multiplication est la répétition de mots.

!!! {{exercice()}}

    Expliquez l'erreur que vous obtenez quand vous tapez :

    - `#!python "4" - 2` ;
    - `#!python "Allo ?"**10` ;
    - `#!python "8"*10 / 2`.  
  
    {{terminal()}}

!!! {{exercice()}}

    === "Question"

        Essayez de prédire le résultat de chacune des instructions suivantes, puis vérifiez-le dans le terminal :

        | Expression | Résultat 1 | Résultat 2 | Résultat 3 | Résultat 4 |
        |:---------|:-------|:-------|:-----|------|
        | `#!python (1 + 3) * 4` | {{tit('', '```#!python 16```')}} | {{tit('', '```#!python 16.0```')}} | {{tit('','```#!python 13```')}} | {{tit('', '```#!python unsupported operand type(s) for +: \'int\' and \'int\'```')}}  |
        | `#!python 5 / 2` | {{tit('', '```#!python 2```')}} | {{tit('', '```#!python 2.5```')}} | {{tit('','```#!python 1```')}} | {{tit('', '```#!python 2.0```')}}  |        
        | `#!python "Six" + 3` | {{tit('', '```#!python "Six3"```')}} | {{tit('', '```#!python 63```')}} | {{tit('','```#!python 9```')}} | {{tit('', '```#!python unsupported operand type(s) for +: \'str\' and \'int\'```')}}  |
        | `#!python 'adf' + 'bce'` | {{tit('', '```#!python "abcdef"```')}} | {{tit('', '```#!python \'adfbce\'```')}} | {{tit('','```#!python "adfbce"```')}} | {{tit('', '```#!python unsupported operand type(s) for +: \'str\' and \'str\'```')}}  |
        | `#!python ("La" + "Li") * 3` | {{tit('', '```#!python "LaLiLiLi"```')}} | {{tit('', '```#!python "LaLiLaLiLaLi"```')}} | {{tit('','```#!python "LaLi"*3```')}} | {{tit('', '```#!python cannot multiply sequence by non-int of type \'float\'```')}}  |        
        | `#!python 70 / 7 + 1` | {{tit('', '```#!python 11.0```')}} | {{tit('', '```#!python 11```')}} | {{tit('','```#!python 8.75```')}} | {{tit('', '```#!python 10 + 1```')}}  |        
        | `#!python "(1 + 3)" * 2` | {{tit('', '```#!python "44"```')}} | {{tit('', '```#!python 8```')}} | {{tit('','```#!python "(1+3)(1+3)"```')}} | {{tit('', '```#!python unsupported operand type(s) for *: \'str\' and \'int\'```')}}  |
        | `#!python "Ba" * 4 / 2` | {{tit('', '```#!python "BaBa"```')}} | {{tit('', '```#!python "Ba2"```')}} | {{tit('','```#!python "BaBaBa"```')}} | {{tit('', '```#!python unsupported operand type(s) for /: \'str\' and \'int\'```')}}  |
        | `#!python "Ba" * (4 / 2)` | {{tit('', '```#!python "BaBa"```')}} | {{tit('', '```#!python BaBa```')}} | {{tit('','```#!python "BaBaBaBa"```')}} | {{tit('', '```#!python cannott multiply sequence by non-int of type \'float\'```')}}  |
        | `#!python 89 % 2` | {{tit('', '```#!python 1```')}} | {{tit('', '```#!python True```')}} | {{tit('','```#!python 44```')}} | {{tit('', '```#!python 44.0```')}}  |

    === "Solution"

        Utilisez le cours et le terminal pour comprendre la correction ci-dessous.

        | Expression | Résultat 1 | Résultat 2 | Résultat 3 | Résultat 4 |
        |:---------|:-------|:-------|:-----|------|
        | `#!python (1 + 3) * 4` | {{tit('x', '```#!python 16```')}} | {{tit('', '```#!python 16.0```')}} | {{tit('','```#!python 13```')}} | {{tit('', '```#!python unsupported operand type(s) for +: \'int\' and \'int\'```')}}  |
        | `#!python 5 / 2` | {{tit('', '```#!python 2```')}} | {{tit('x', '```#!python 2.5```')}} | {{tit('','```#!python 1```')}} | {{tit('', '```#!python 2.0```')}}  |        
        | `#!python "Six" + 3` | {{tit('', '```#!python "Six3"```')}} | {{tit('', '```#!python 63```')}} | {{tit('','```#!python 9```')}} | {{tit('x', '```#!python unsupported operand type(s) for +: \'str\' and \'int\'```')}}  |
        | `#!python 'adf' + 'bce'` | {{tit('', '```#!python "abcdef"```')}} | {{tit('x', '```#!python \'adfbce\'```')}} | {{tit('x','```#!python "adfbce"```')}} | {{tit('', '```#!python unsupported operand type(s) for +: \'str\' and \'str\'```')}}  |
        | `#!python ("La" + "Li") * 3` | {{tit('', '```#!python "LaLiLiLi"```')}} | {{tit('x', '```#!python "LaLiLaLiLaLi"```')}} | {{tit('x','```#!python "LaLi"*3```')}} | {{tit('', '```#!python cannot multiply sequence by non-int of type \'float\'```')}}  |        
        | `#!python 70 / 7 + 1` | {{tit('x', '```#!python 11.0```')}} | {{tit('', '```#!python 11```')}} | {{tit('','```#!python 8.75```')}} | {{tit('', '```#!python 10 + 1```')}}  |        
        | `#!python "(1 + 3)" * 2` | {{tit('', '```#!python "44"```')}} | {{tit('', '```#!python 8```')}} | {{tit('x','```#!python "(1+3)(1+3)"```')}} | {{tit('', '```#!python unsupported operand type(s) for *: \'str\' and \'int\'```')}}  |
        | `#!python "Ba" * 4 / 2` | {{tit('', '```#!python "BaBa"```')}} | {{tit('', '```#!python "Ba2"```')}} | {{tit('','```#!python "BaBaBa"```')}} | {{tit('x', '```#!python unsupported operand type(s) for /: \'str\' and \'int\'```')}}  |
        | `#!python "Ba" * (4 / 2)` | {{tit('', '```#!python "BaBa"```')}} | {{tit('', '```#!python BaBa```')}} | {{tit('','```#!python "BaBaBaBa"```')}} | {{tit('x', '```#!python cannott multiply sequence by non-int of type \'float\'```')}}  |
        | `#!python 89 % 2` | {{tit('x', '```#!python 1```')}} | {{tit('', '```#!python True```')}} | {{tit('','```#!python 44```')}} | {{tit('', '```#!python 1.0```')}}  |



    {{terminal()}}

## Résumé

!!! danger "Résumé"

    Dans ce chapitre, j'ai appris : 
    
    - [ ] ce qu'est une variable (nom, valeur)
    - [ ] comment nommer une variable correctement (snake_case)
    - [ ] qu'une variable est _typée_ (`#!python int, float, bool, str`)
    - [ ] qu'on ne peut pas effectuer n'importe quelle opération sur n'importe quelle type de variable
    - [ ] à comprendre _(un peu)_ les messages d'erreur