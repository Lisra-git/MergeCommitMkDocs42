# Variables

## Éditeur, console, terminal ?

Un terminal est une invite de commandes permettant à l'homme et à la machine de communiquer via un shell.

Pour programmer, il existe deux grands types d'outils :

- la console (aussi appelé interpréteur) permet de réaliser des calculs, des tests rapides ainsi que des programmes courts. On ne sauvegarde pas son travail ;
- l'éditeur de code permet d'écrire un programme complexe dans un langage donné et de sauvegarder son travail. Il est souvent combiné à un interpréteur afin d'exécuter le programme et de le rendre compréhensible par l'ordinateur.

!!! example "Exemple"

    === "Une console"

        Calculez la somme de 134 et de 5677 dans la console. Faites également leur multiplication à l'aide du symbole `*`.

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
        
        Dans la console ci-dessous, tapez : `#!python print("Hello world !")`. Que se passe-t-il ?

        [^id]: la tradition d’utiliser hello world comme premier programme de test a été initiée par le livre `The C Programming Language` de Brian Kernighan et Dennis Ritchie, publié en 1978.

    === {{exercice(False)}}

        Dans la console, affichez la phrase "Bonjour le monde !". 

        ??? help "Aide" 
        
            Avez-vous bien utilisé des guillemets comme dans l'exercice précédent ?

    === {{exercice(False)}}

        Dans la console ci-dessous, réalisez la soustraction de 956 et de 649.

        Utilisez l'instruction `#!python print` pour afficher à nouveau le résultat de cette opération.

        ??? help "Aide" 
        
            Pas de guillemets ici. Voyez-vous quelle est la différence fondamentale entre la soustraction et les phrase des exercices 1 et 2 ?


    {{terminal()}}

!!! warning "Important"

    Vous devez obtenir le même affichage que vous fassiez `#!python 45*4` ou `#!python print(45*4)`. 

    On aurait pu aussi taper "Hello World !" sans `#!python print`.
    
    La console **évalue** des expressions Python puis affiche le résultat de l'évaluation. `#!python print` sera utile dans les programmes plus complexes.

## Notion de variable

Nous évoquons ci-dessous la notion de variable. Celle-ci sera revue en cours en activité débranchée.

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

!!! {{cours()}}

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

            - [x] `#!python nombre_briques` ou `#!python n_briques` ou `#!python n_briques_lait` ou `#!python n_briques_entrepot` sont des noms convenables. `#!python nombrebriques` ou `#!python nBriquesLait` ou `#!python nombre_de_briques_de_lait_dans_entrepot` ne respectent pas le _snake case_ ou sont trop longs.
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


Dans l'éditeur de EduPython, saisissez le code suivant :

**pointsDeVie = 25**

puis, dans la console d'EduPython, tapez : **pointsDeVie**

Après avoir exécuté le programme en cliquant sur le triangle vert, il
est donc possible de connaitre la valeur référencée par une variable
en utilisant le terminal de EduPython.

--- À faire vous-même **4** ---

Modifiez le programme précédent pour attribuer la valeur 15 à la
variable pointsDeForce. La valeur référencée par la variable
pointsDeForce devra ensuite être affichée dans la console.

1)  Variables d'entrée/sortie

On affiche une variable avec l'instruction **print**(**variable**):
c'est une instruction de sortie (output).

--- À faire vous-même **5** ---

En utilisant l'instruction **print**(......), modifier le programme
précédent afin que celui-ci affiche vos points de vie et vos points de
force dans le terminal **directement après l'exécution.**

Une instruction d'entrée importante est
**input(\"infoUtilisateur\")**.

--- À faire vous-même **6** ---

Ajoutez la ligne : **nomJoueur = input(\"Entre ton nom : \")**

Puis, en utilisant **print(\"Bienvenue \",nomJoueur)** ,afficher dans
le terminal une invite de Bienvenue qui change en fonction du nom du
joueur.

--- À faire vous-même **7** ---

À l'aide d'une variable ageJoueur, demandez à l'utilisateur
d'entrer aussi son âge.

Puis, en modifiant le **print**() , afficher dans le terminal
\"Bienvenue\", \"nomJoueur\" et \"3\*ageJoueur\".

L'instruction **3\*ageJoueur** a-t-elle fait ce que vous attendiez ?
Qu'a-t-elle fait ?


1)  Typage des variables

Les données et les variables sont **[typées]{.ul}** dans un langage de
programmation, c'est-à-dire que l'on doit préciser si ce sont des
nombres, des chaines de caractères, des listes\...

En Python le typage est très souple, ce qui facilite l'écriture des
programmes lorsque l'on débute. Néanmoins, il est parfois nécessaire
de le préciser.

L'instruction **type(variable)** permet de savoir quel est le type
d'une variable.

--- À faire vous-même **8** ---

Dans le terminal, affichez le type de pointsDeVie et de ageJoueur.

Les types principaux que nous utiliserons cette année sont :

-   les entiers : type int ;

-   les flottants (approximation des nombres réels par des décimaux) :
    type float ;

-   les chaines de caractères (mots) : type str ;

-   les booléens (True ou False) : type bool.

Nous étudierons dans une séance prochaine d'autres types permettant
de décrire des tableaux :

-   les listes : type list;

-   les dictionnaires : type dict;

-   les n-uplets : type tuple.

On peut changer une variable (transtypage) :

-   en entier en utilisant int(variable) ;

-   en flottant en utilisant float(variable) ;

-   en booléen en utilisant bool(variable) ;

--- À faire vous-même **9** ---

Dans votre programme, ajoutez :

pointsDeMana = 6.5 et persoVivant = True

Affichez les types de ces variables dans le terminal à l'aide de
l'instruction **print**(......).

[Remarque :]{.ul}

On utilise la notation anglo-saxonne avec . pour la virgule, et e pour
\"10 puissance\". Par exemple : 1.5e4 = 15000

--- À faire vous-même 10 ---

Dans votre programme, à partir de la variable ageJoueur et des
opérations de transtypage, créez les variables suivantes :

ageJoueurEntier, ageJoueurReel, ageJoueurBool, ageJoueurList,
ageJoueurTuple

qui seront de type entier, flottant, booléen, liste et tuple.

Affichez ces variables dans le terminal et étudiez les différences
entre ces écritures.

Un peu de mathématiques !

1)  Opérations natives en Python

Python possède des symboles permettant de faire des opérations
arithmétiques.

Il est possible d'effectuer des opérations avec des **nombres**, mais
aussi avec des **variables**.

Les signes utilisés sont classiques : +, - .

--- À faire vous-même **11** ---

Dans le terminal Python, en faisant de **nombreux** tests, découvrez
la signification des symboles \*, / , // , % et \*\*.

--- À faire vous-même **12** ---

Créer un nouveau fichier appelé addition.py.

Écrire un programme qui additionnera le contenu de 2 variables nommées
**a** et **b**. Le résultat de cette opération devra être référencé
par une troisième variable nommée **resultat** (attention, pas
d'accent dans les noms de variable).

Testez votre programme en utilisant la console pour vérifier la valeur
référencée par la variable **resultat**.

--- À faire vous-même **13** ---

Créer un nouveau fichier appelé conversionAge.py.

Ecrire un programme qui demande votre âge en année et le convertit en
nombre de jours.

5)  Bibliothèque math

Il est possible d'effectuer des calculs complexes en utilisant des
racines carrées, des fonctions trigonométrique des logarithmes,...

Pour utiliser ces instructions \"élémentaires\", il est nécessaire
d'ajouter une ligne au début de votre programme : **import math**

Cette ligne permet d'importer (et donc d'utiliser) la bibliothèque
\"math\" qui contient toutes les fonctions mathématiques
\"classiques\".

Voici quelques exemples :

-   math.pow(x,a) permet de calculer x à la puissance a ;

-   math.cos(x) permet de calculer le cosinus de l'angle x (l'angle x
    doit être en radian) ;

-   math.sqrt(x) permet de calculer la racine carrée de x.

Si vous avez besoin d'autres fonctions mathématiques, je vous invite
à consulter la documentation de Python :
<https://docs.python.org/3/library/math.html

--- À faire vous-même **14** ---

En calculant à la main, déterminez les valeurs référencées par les
variables d, e, f, g, h et i après l'exécution du programme suivant :

import math

a = 5

b = 16

c = 3.14 / 2

d = b / a

e = b // a

f = b % a

g = math.pow(a,2)

h = math.sqrt(b)

i = math.sin(c)

Vérifiez vos réponses à l'aide du terminal.

--- À faire vous-même **15** ---

Écrire un programme permettant de répondre à la question suivante :

\"Quel est le type du résultat d'une addition d'un integer et d'un
float ?\"

[Remarque :]{.ul}

-   Il est donc tout à fait possible de \"mélanger\" des nombres entiers
    et des nombres à virgules (\"3.14 / 2\") dans une opération.

-   Attention aux float : dans le terminal essayez de faire 0.1+0.1 puis
    0.1+0.1+0.1\
    Qu'en pensez-vous ?

    Chaine de caractères : vive les strings.

1)  Chaines de caractères

Les chaines de caractères sont des listes de caractères : **\"le
chat\"** est constitué des caractères **'l', 'e', ' ', 'c',
'h', 'a', 't'** .

On peut connaitre la longueur d'une chaine de caractères grâce à :
**len(string)**

--- À faire vous-même **16** ---

Créer un nouveau fichier strings.py :

**maChaine = \"Bonjour le monde !\"**

Vérifiez que la variable maChaine est une chaine de caractères
contenant la phrase \"Bonjour le monde !\"

6)  Concaténation : le signe +

L'utilisation du signe + ne se limite pas à l'addition. Il est aussi
utilisé pour la **concaténation**. Cherchez sur Wikipédia
l'étymologie du mot.

--- À faire vous-même **17** ---

Quelle est la chaîne de caractère référencée par la variable
monExpression après l'exécution du programme ci-dessous ? Validez
votre réponse en testant ce programme dans strings.py.

**a = \"Hello\"**

**b = \"World\"**

**monExpression = a + b**

7)  Chaînes de caractères et variables

Il est aussi possible de concaténer une chaîne de caractères et une ou
plusieurs variables :

--- À faire vous-même **18** ---

Quelle est la valeur de res dans le programme ci-dessous ? Validez
votre réponse en testant ce programme dans strings.py.

**myString1 = \"Bonjour \"**

**myString2 = \"le \"**

**res = myString1 + myString2 + \"monde!\"**

Les 2 variables myString1 et myString2 référencent 2 chaînes de
caractères, nous avons donc bien ici une concaténation.

Mais que se passe-t-il si la variable référence un nombre (entier ou
flottant) ?

--- À faire vous-même **19** ---

Testez le code suivant dans strings.py:

**monNombre = 5**

**res = \"Nombre de personnes : \" + monNombre**

Que constatez-vous ? Pourquoi ?

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Python nous offre 2 solutions :

l'utilisation de la méthode \"str\"

l'utilisation des \"fstring\"

La méthode \"str\" permet de transformer un nombre en chaîne de
caractères. On appelle cela du **transtypage**.

--- À faire vous-même **20** ---

En utilisant la méthode \"str\", corrigez le programme fait au \#19.

Les \"fstring\" (nouveauté de Python 3.6), permettent de résoudre ce
problème de combinaison variable-chaîne de caractères.

--- À faire vous-même **21** ---

Testez le code suivant dans strings.py :

**monAutreNombre = 10**

**res = f\"Nombre de personnes : {monAutreNombre}\"**

[Remarque :]{.ul}

Notez la présence du \"f\" juste avant le guillemet et des accolades
qui encadrent le nom de la variable.

**Checkpoint**

1)  On dispose de la formule suivante pour convertir les degrés
    Fahrenheit en degrés Celsius : $C = \frac{F - 32}{1,8}$, où *F* est
    une température en degrés Fahrenheit et *C* la température
    correspondante en degrés Celsius.

    a.  Ecrire un programme qui convertit en degrés Celsius une
        température rentrée au clavier en degrés Fahrenheit.

    b.  Même question pour la conversion inverse.

2)  Écrire un programme qui permute et affiche les valeurs de trois
    variables *a*, *b*, *c* qui sont entrées au clavier : *a* ==\*b* ,
    *b* ==\*c* , *c* ==\*a*.

3)  Ecrire un programme qui teste si une chaine de caractère est un
    palindrome.\
    Exemple de palindrome :\
    'kayak' ou 'Engage le jeu que je le gagne'

    Structures de contrôle

```{=html}
<!-- --
```
1)  Booléens

Si quelqu'un vous dit que \"4 est égal à 4\", vous lui répondez :
\"ben c'est vrai\". Si maintenant la même personne vous dit que \"7
est égal à 12\", vous lui répondrez bien évidemment que \"c'est faux
!\".

Comme en langage naturel, en Python, ces deux affirmations se noterons
avec un double signe égal : par exemple, 7 == 12.

--- À faire vous-même **22** ---

Dans le terminal, tapez :

**7 == 12 5 \= 4 5 \<= 5 5 != 5 5 \12**

En Python, \" 5 \= 5 \" est appelé une **expression.** Une expression
est soit vraie (True), soit fausse (False).

Dans le dernier TP, nous avons surtout travaillé sur les entiers, les
nombres flottants et les chaînes de caractères. Ici, nous abordons les
**booléens**.

[Rappel :]{.ul} Un booléen est un type de données qui ne peut prendre
que deux valeurs : vrai (True) ou faux (False).

--- À faire vous-même **23** ---

Dans l'éditeur de texte, entrez les valeurs a = 4 et b = 7.

Quel est le résultat attendu après l'exécution de ce programme si
vous saisissez dans la console \"a == b\" ? si vous saisissez \"a !=
b\"

Ajoutez la signification de ces opérateurs sur le formulaire.

On peut connecter des expressions booléennes les unes aux autres à
l'aide des opérateurs logiques **and** (et), **or** (ou) ou **not**
(non).

Nous verrons leur fonctionnement exact dans un prochain chapitre. Pour
l'instant, nous allons remplir les tables de vérités page suivante à
l'aide de tests Python :

--- À faire vous-même **24** ---

Dans l'éditeur de texte, entrez les expressions :

expr1 = (4 \< 10) et expr2 = (12 != 10)

Puis, sur une même ligne, afficher ensuite les valeurs de :

**expr1**, **expr2**, **expr1 or expr2**.

Refaites d'autres tests afin de remplir les trois tables de vérité
ci-dessous.

**[Table de vérité pour le \"ou\"]{.ul}**

**[Table de vérité pour le \"et\"]{.ul}**

**[Table de vérité pour le \"non\"]{.ul}**

[Rem :]{.ul} il est facile de faire n'importe quoi avec des
enchainements d'expressions booléennes. Conservez des expressions
simples.

--- À faire vous-même **25** ---

En testant le programme suivant, trouvez la valeur de c en fonction
des valeurs de a et de b. Bonne chance !

a = int( input(\"Donnez un nombre\") )

b = (a \50)

print( \"b vaut\", b, \", et est de type \", type(b) )

c = ( a == 3 or not(b) or not(a != 25) )

[Remarque importante :]{.ul} Flottants et booléens ne font pas bon
ménage ! Les flottants ne sont qu'une représentation décimale des
réels.

--- À faire vous-même **26** ---

Dans le terminal, trouvez les valeurs des expressions booléennes
suivantes :

A = (3 \* 0.1 == 0.3) A est \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

B = (abs(3 \* 0.1 - 0.3) \< 1e-5) B est
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

n = 1e15

C1 = (1 + 1 / n == 1) C1 est \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

n = 1e16

C2 = (1 + 1 / n == 1) C2 est \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

D = (1 / n == 0) D est \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

[Conclusion :]{.ul} Pour comparer deux flottants, on vérifie s'ils
sont assez proches comme dans l'expression B.

8)  Conditionnelle \"Si ... Alors ...\"

Dans le chapitre 2, nous avons abordé la structure de controle \"Si
... Alors ... Sinon\". En Python, cette structure appelée
conditionnelle s'écrit :

if expressionBooléenne :

blocInstructionA

else :

blocInstructionB

Si l'expression est vraie, alors on fait le bloc d'instructions A.
Sinon, on fait le bloc d'instructions B.

--- À faire vous-même **27** ---

Dans l'éditeur de texte, entrez le programme suivant :

v = float(input('Vitesse du vent (en noeuds)?'))

if v \= 20 :

meteo = 'Sortie en mer annulée'

else:

meteo = 'Sortie en mer maintenue'

print( meteo )

--- À faire vous-même **28** ---

Écrire un programme qui prend en entrée un age.

Si age est supérieur ou égal à 18 ans, la fonction devra renvoyer la
chaîne de caractères \"Bonjour, vous êtes majeur.\". Si age est
inférieur à 18 ans, la fonction devra renvoyer \"Bonjour, tu es
mineur.\"

--- À faire vous-même **29** ---

-   Dans l'éditeur de texte, modifiez le programme \#27 pour obtenir :

v = float(input('Vitesse du vent (en noeuds)?'))

h = float(input('Houle (en m)?'))

varBooleen = (v \= 20 or h \= 5)

if varBooleen **== True** :

meteo = 'Sortie en mer annulée'

else:

meteo = 'Sortie en mer maintenue'

print( meteo )

[Remarque :]{.ul} Dans le programme précédent, a-t-on besoin de
spécifier **== True** ? Pourquoi ? Pour répondre, essayez de
l'enlever dans le programme \#29.

--- À faire vous-même **30** ---

-   Quel est le résultat attendu après l'exécution de ce programme ?

-   Est-il possible d'obtenir tous les messages?

Vérifiez votre réponse en testant ce programme (faire varier a et b)

a = 5

b = 10

if a \5 and b == 10:

varAffiche = \"Toto\"

else:

varAffiche = \"Titi\"

if a \5 or b == 10:

varAffiche = \"Tata\"

else:

varAffiche = \"Tutu\"

print( varAffiche )

[Rem]{.ul} : Attention aux booléens et aux variables opaques...

9)  Conditionnelle \"Si ... SinonSi ... Alors ...\"

Dans le chapitre 2, nous avons également discuté de la structure de
controle \"Si ... SinonSi ... Sinon\". En Python , elle s'écrit :

if expressionBooléenne1 :

blocInstructionA1

elif expressionBooléenne2 :

blocInstructionA2

else :

blocInstructionB

![](media/image4.png){width="3.371745406824147in"
height="3.2762379702537183in"}

--- À faire vous-même **31** ---

Les tarif réduits pour l'entrée à un musée sont :

-   gratuit pour les moins de 5 ans

-   mi-tarif pour les moins de 16 ans

-   mi-tarif pour les plus de 65 ans

-   mi-tarif pour les étudiants.

À l'aide des instructions elif, programmez\
l'algorithme ci-contre afin d'afficher quel\
est le prix que doit payer un visiteur. Les deux\
variables que l'utilisateur devra entrer au\
clavier sont : age et statut.

Tarif sera égal à 10.

--- À faire vous-même **32** ---

On prend a = 10 : testez les trois codes ci-dessous.

if a \< 5:

print(a, \"\< 5\")

if a \2:

print(a, \"\2\")

if a \4:

print(a, \"\4\")

if a \< 5 :

print(a, \"\< 5\")

elif a \2:

print(a, \"\2\")

elif a \4:

print(a, \"\4\")

if a \< 5 :

print(a, \"\< 5\")

elif a \4:

print(a, \"\4\") elif a \2:

print(a, \"\2\")

Que pouvez-vous déduire du test \#32 ?

10) Boucle non bornée

Comme nous l'avons vu dans le Chapitre 2, la boucle est fondamentale
en informatique.

On réalise une boucle **[non bornée]{.ul}** grâce à l'instruction :

while expressionBooléenne :

blocInstructions

Le bloc d'instructions continuera tant que l'expression booléenne
est vraie.

--- À faire vous-même **33** ---

Dans l'éditeur de texte, écrire le programme suivant :

i = 0

while i \< 10:

print(\"i vaut : \", i )

i = i + 1

print(\"C'est enfin terminé.\")

Quel est le résultat attendu après l'exécution de ce programme ?
Vérifiez votre réponse en testant le programme

[Rem]{.ul} : Dans ce programme, i s'appelle le compteur.

--- À faire vous-même **34** ---

Écrire un programme permettant de créer \"un générateur automatique de
punition\" .

Il y aura deux valeurs d'entrée : une chaîne de caractère et un
nombre entier

Exemple :

Si l'utilisateur entre : \"*Je ne dois pas discuter en classe*\" et 3

Le programme devra permettre d'afficher :

*Je ne dois pas discuter en classe*

*Je ne dois pas discuter en classe*

*Je ne dois pas discuter en classe*

--- À faire vous-même **35** ---

Écrire un programme de jeu dont le but est de trouver le nombre 42 par
essais successifs. Tant que le nombre 42 n'a pas été trouvé,
l'utilisateur doit entrer de nouveaux nombres.

Exemple :

Le programme dit : \"Donne un nombre\" --- l'utilisateur entre : 12

Le programme dit : \"Donne un nombre\" --- l'utilisateur entre : 25

Le programme dit : \"Donne un nombre\" --- l'utilisateur entre : 42

Le programme dit : \"Bravo! C'est gagné !\"

11) Boucle bornée

On réalise une boucle **[bornée]{.ul}** grâce à l'instruction :

for element in sequence :

blocInstructions

Contrairement aux boucles non bornées, la borne bornée permet de
parcourir les éléments d'une séquence de **[longueur connue]{.ul}**.

--- À faire vous-même **36** ---

Tester le programme suivant. Que fait-il ?\
En changeant les valeurs de 0 et 8, étudier le fonctionnement de
l'instruction range.

for element in range(0, 8, 1):

print(element, element\*\*2, element\*\*3)

[Remarque :]{.ul} L'instruction range(0, 8, 1) permet de générer tous
les nombres successivement entre
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
.

Même si ce n'est pas complètement exact, on peut dire que range(0, n)
est équivalent à un tableau T avec T = \[0, 1, 2, ......... , n-1\] .

[Définition :]{.ul} Une séquence peut être un tableau ou une chaine de
caractères.

[Exemple :]{.ul}

tableau = \[3, 1, 4, 15, 9, 2\]

sequence = \"aujourd'hui, maman est morte\"

[Rappel :]{.ul} On accède à la taille d'un tableau ou d'une chaine
de caractères avec l'instruction len( ......... ) .

--- À faire vous-même **37** ---

Tester le programme suivant.

varString = \"un chaton\"

for element in varString :

print(element)

[Question :]{.ul} Qu'affiche le programme ci-dessus ?

Un compteur peut également être utilisé pour accéder aux éléments de
notre chaine de caractères :

--- À faire vous-même **38** ---

Testez le programme suivant et répondez aux questions ci-dessous.

varString = \"un chaton\"

longueurString = len(varString)

for i in range( longueurString ) :

element = varString\[i\]

print('Le ', i, 'ème element est: ', element)

Que fait la 2ème ligne ?
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Que signifie range( longueurString ) ?
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Sur la 4ème ligne, identifiez la syntaxe permettant d'obtenir le
i-ème élément :
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

[Remarques importantes :]{.ul}

-   le nom de la variable de boucle est complètement arbitraire ! Dans
    un cas, elle s'appelle **element**, dans l'autre **i**, mais on
    aurait aussi pu l'appeler **totoDansLaCuisine** (mais c'est plus
    long à écrire...).

-   on peut mettre des boucles dans des boucles. Toutefois les variables
    de boucles doivent être différentes les unes des autres.

--- À faire vous-même **39** ---

Testez le programme suivant et comprenez son fonctionnement.

for i in range(5,0,-1) :

for j in range(0,5,1) :

print(i, j)

**Checkpoint**

1)  **[Table de multiplication]{.ul}**

Écrire un programme permettant d'afficher une table de
multiplication. Ce programme devra prendre comme variable d'entrée la
table désirée.

Par exemple si l'on donne le nombre 3 au programme, la fonction devra
permettre d'afficher :

1 x 3 = 3

2 x 3 = 6

\...

\...

10 x 3 = 30

2)  **[Constante de Champernowne]{.ul}**

On appelle constante de Champernowne le nombre
0.123456789101112131415161718192021\... c'est à dire le nombre où on
écrit tous les nombres à la suite les uns des autres.

a)  Écrire un programme qui prend n en entrée et affiche la constante de
    Champernowne jusqu'au nombre n inclus.\
    \
    Par exemple si n=3, il faut afficher 0.123.

b)  Allez sur *Wikipédia* et apprenez-en un peu sur les nombres normaux.
    Vous pouvez aussi regarder sur *Youtube* : All the Numbers -
    Numberphile

```{=html}
<!-- --
```
4)  **[Division enfantine]{.ul}**\
    Écrire un programme permettant de faire des divisions euclidiennes
    comme un enfant de 7 ans.\
    L'utilisateur entre un dividende et un diviseur, puis le programme
    soustrait n fois le diviseur du dividende. On trouve alors le
    quotient et le reste que l'on affiche à l'écran.

[Exemple]{.ul} : dividende 13 et diviseur 6.

13 - 6 = 7 7 - 6 = 1

On a soustrait 6 deux fois donc, quotient = 2 et il reste 1 donc reste
= 1.

5)  **[Recherche d'un maximum]{.ul}**\
    Dans le Chapitre 1, nous avons travaillé sur l'algorithme de
    recherche d'un maximum dans une liste de nombres.\
    \
    Traduisez cet algorithme en un programme Python donnant le maximum
    d'une liste de nombres. Vous écrirez directement cette liste dans
    le programme.

6)  **[Nombre premier]{.ul}**\
    Un nombre premier est un nombre qui a exactement 2 diviseurs qui
    sont 1 et lui même. Le but de cet exercice est de créer un
    algorithme qui dit à un utilisateur si un nombre est premier ou
    pas.\
    \
    Etant donnée la définition, pour savoir si un nombre n est premier
    ou pas, on va tout simplement tester s'il est divisible par un des
    nombres compris entre 2 et n-1. Dès qu'on trouve un diviseur, on
    affiche \"PAS PREMIER\" sinon on affiche \"PREMIER\".\
    L'utilisateur doit rentrer au clavier le nombre à tester.

7)  **[Mastermind]{.ul}**\
    On reprend le programme \#35. À présent, l'utilisateur doit trouver
    un nombre entier aléatoire entre 0 et 100 avec utilisant le moins de
    coup possible.\
    \
    Pour générer un nombre aléatoire en Python, on met sur la première
    ligne de notre code : **from random import \***. Cela importe la
    bibliothèque **random**.\
    Puis, on génère un nombre aléatoire avec : **nbrAlea =
    randint(0,100)**.\
    \
    [Exemple]{.ul} :\
    Le programme dit : \"Donne un nombre\" --- L'utilisateur entre :
    12\
    Le programme répond : \"Non, c'est plus petit\".\
    Le programme dit : \"Donne un nombre\" --- L'utilisateur entre : 8\
    Le programme répond : \"Non, c'est plus grand\".\
    Le programme dit : \"Donne un nombre\" --- L'utilisateur entre : 9\
    Le programme répond : \"Bravo, 9 est le nombre recherché ! Tu as
    gagné en 3 essais !\"

8)  **[Défi]{.ul}**\
    Réécrire le code \#31 en moins de 10 lignes (je l'ai fait avec 98
    caractères espaces compris et 7 lignes...)

    Fonctions

```{=html}
<!-- --
```
1)  Le principe DRY

Tous les langages informatiques sont fondés sur une comme une oeuvre
d'art ou un poème.

Comme je descendais des Fleuves impassibles,

Je ne me sentis plus guidé par les haleurs :

Des Peaux-Rouges criards les avaient pris pour cibles,

Les ayant cloués nus aux poteaux de couleurs.

J'étais insoucieux de tous les équipages,

Porteur de blés flamands ou de cotons anglais.

Quand avec mes haleurs ont fini ces tapages,

Les Fleuves m'ont laissé descendre où je voulais.

Idée de beauté du code. Tous les langages se fondent sur la même
philosophie : DRY (Don't Repeat Yourself).

12) Introduction aux fonctions

Jusqu'à maintenant, un programme se composait de lignes que l'on
lisait les unes à la suite des autres. Cette approche (ou paradigme)
peut poser des problèmes techniques.

--- À faire vous-même **40** ---

Le jour du Black Friday, une personne achète :

\- 25 livres à 12€ hors taxe (TVA est de 5,5%) ;

\- 2 écrans LCD à 540€ hors taxe (TVA est de 20%) ;

\- 1 smartphone à 700€ hors taxe (TVA est de 10%).

Écrire un programme permettant de savoir combien cette personne a
dépensé TTC. On rappelle que le \"Prix TTC = Prix HT + Part TVA\".

[Que se passerait-il si vous deviez rajouter une autre donnée à un
taux de TVA de 15% ? puis une autre de 20% ?]{.ul}

**[Conclusion :]{.ul}** Pour éviter la répétition d'une instruction
et structurer votre code informatique, on peut utiliser un objet
appelé fonction.

Les fonctions permettent de décomposer un programme complexe en une
série de sous-programmes plus simples.

En ce sens, les fonctions sont réutilisables : si nous disposons
d'une **fonction capable de calculer un prix TTC à partir d'un prix
hors taxe et d'un taux de TVA**, nous pouvons l'utiliser partout
dans notre programme sans avoir à faire des copier/coller.

Les fonctions informatiques sont donc comparables à la notion de
fonctions mathématiques.

13) Fonctions

[Définition]{.ul} : Le **prototype** (définition) d'une fonction est
constitué :

-   d'un nom ;

-   d'une liste de paramètres ;

-   de l'ensemble des instructions à réaliser.

Le prototype d'une fonction s'écrit :

**def** nom(param1: type1, param2: type2 \... ) -\typeSortie :

instructions

**return** y

**def** permet de définir une fonction ;

**return** y permet de renvoyer la valeur de la variable y ;

param1, param2 ... sont les paramètres d'entrées ;

type1, type2 ... sont les types des paramètres d'entrées ;

typeSortie est le type de la variable de sortie.

--- À faire vous-même **41** ---

Dans l'éditeur de texte, entrez :

def maFonction(x: int) -\int:

y = 3 \* x + 2

return y

On récupère le résultat de cette fonction pour x=4 en ajoutant :

solution = maFonction(4)

Affichez les résultats de cette fonction pour x=1, x=10, x=100.

**[Rem :]{.ul}** Quelle fonction mathématique est codée ci-dessus ?

--- À faire vous-même **42** ---

On définit la fonction $f(x) = 2x - 5$.

En modifiant la fonction précédente et grâce à une boucle, faites la
somme des f(x) pour x allant de 0 à 121.

--- À faire vous-même **43** ---

Codez en Python la fonction maFonction2 de formule y = ($x^{2}$ + x) %
10. x et y seront des entiers.

Affichez les valeurs de cette fonction pour x = 1, 3, 40 et 145.

Une fonction peut prendre plusieurs paramètres en entrée.

--- À faire vous-même **44** ---

Écrivez dans l'éditeur de texte :

def nouvelleFonction(x: float, a: int, b: int) -\float :

y = a \* x + b

return y

Quel résultat renvoie cette fonction si x=4, a=-2 et b=8 ?
\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Quel résultat renvoie cette fonction si x=-4, a=2 et b=-8 ?
\_\_\_\_\_\_\_\_\_\_\_\_\_\_

--- À faire vous-même **45** ---

Écrivez une fonction qui permette de répondre plus facilement à
l'encadré \#40.

Les deux paramètres d'entrée seront le prix HT et le taux de TVA.

14) Jeux de tests : pré-condition, post-condition

--- À faire vous-même **46** ---

Codez en Python la fonction maFonction2 de formule y = $\sqrt{x}$ + x
% 10. x et y seront des entiers.

Affichez les valeurs de cette fonction pour x = 1, 4,121 et 145.

**[Rem :]{.ul}** Que remarquez-vous pour 145 ? Les types sont-ils
respectés ?

Pour respecter les types demandés et/ou effectuer des tests sur des
fonctions, Python fournit une instruction appelée : assert .

assert permet de vérifier si une condition est vérifiée :

--- À faire vous-même **47** ---

Dans la console, entrez x=2 .

Que se passe-t-il si vous entrez assert(x \1) ?
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Que se passe-t-il si vous entrez assert(x \3) ?
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

--- À faire vous-même **47** ---

Dans le programme 46, après la définition de la fonction, ajoutez la
ligne suivante :

assert ( int(sqrt(x)) == sqrt(x) ).

Affichez à nouveau les valeurs de cette fonction pour x = 1, 4,121 et
145.

**[Rem :]{.ul}** Que remarquez-vous pour 145 ? Les types d'entrée
sont-ils respectés ?

**[Définition]{.ul}** : le test que nous venons d'effectuer
s'appelle une pré-condition.

15) Procédures, fonctions particulières

**[Rem 1 :]{.ul}** Les paramètres ne sont pas obligatoires.

--- À faire vous-même **48** ---

Testez la fonction suivante :

def ma_fon() -\str:

return \"voici une fonction qui ne sert à rien\"

**[Rem 2 :]{.ul}** Une fonction ne renvoie pas forcément de valeur (le
mot clé **return** n'est pas obligatoire). Elle peut par exemple
afficher une chaîne de caractères à l'aide d'un \"print\".

Dans certains langages, on utilise les termes **méthode** ou
**procédure** pour qualifier une fonction \"qui ne renvoie rien\".

--- À faire vous-même **49** ---

Testez la fonction suivante :

def ditBonjour(nom : str, age: str):

phrase = \"Bonjour\", nom, \"vous avez\", age, \"ans.\"

print(phrase)

**Checkpoint**

1)  **[Autour des chaines de caractères]{.ul}**

```{=html}
<!-- --
```
a.  Écrire une fonction « singleton » qui prend un string en paramètre
    et renvoie « vrai » si la liste est égale à \[0\].

b.  Écrire une fonction « même longueur » qui prend deux strings en
    paramètres (= **arguments**) et renvoie vrai si les listes sont de
    même longueur.

c.  Écrire une fonction « appartient » qui prend en entrée un string et
    une lettre et renvoie « vrai » si l'élément appartient à la liste.

d.  Créer une fonction « pluriel » qui rajoute un s au string donné en
    entrée s'il ne se termine pas déjà par s.

```{=html}
<!-- --
```
2)  **[Calcul de pi !]{.ul}**

```{=html}
<!-- --
```
a.  Écrire une fonction « factorielle » qui prend un nombre **n** en
    paramètre et renvoie la valeur de **n!**. On rappelle que
    $n! = n \times (n - 1) \times ... \times 3 \times 2 \times 1$.

```{=html}
<!-- --
```
e.  Écrire une fonction « piApprox » qui prend un nombre **n** en
    paramètre et renvoie la valeur approchée de $\pi$ selon la formule
    :\
    $\pi \approx \left( 2 + 2^{2} \times \frac{(1!)^{2}}{3!} + 2^{3} \times \frac{(2!)^{2}}{5!} + ... + 2^{n + 1} \times \frac{(n!)^{2}}{(2n + 1)!} \right)$\
    On fera varier la valeur de n pour augmenter la précision.

f.  Créer une fonction « checkPi » qui prend pour argument un nombre
    flottant **eps** et qui renvoie la valeur de **n** telle que la
    valeur absolue de piApprox moins pi sous inférieure à **eps**.\
    [Aide :]{.ul} check(1e-2) doit vous renvoyer 7.

```{=html}
<!-- --
```
3)  **[Décryptage]{.ul}**

```{=html}
<!-- --
```
a.  Écrire une fonction « uneLettre » qui prend en paramètres un message
    (type string) et une lettre (type string) et qui renvoie le nombre
    d'apparitions de cette lettre dans ce message.\
    Par exemple : uneLettre('ah lala','a') renvoie 3.

```{=html}
<!-- --
```
g.  Écrire une fonction « histogramme » qui prend en paramètre un
    message (type string) et qui affiche à l'écran le nombre
    d'apparitions de toutes les lettres de l'alphabet.\
    Pour générer l'alphabet, on pourra utiliser :\
    **from string import \*\
    alphabet = ascii_lowercase**\
    \
    Par exemple : \"ababcdaa\" affiche :\
    a : 4\
    b : 2\
    c : 1\
    d : 1

```{=html}
<!-- --
```
4)  **[Problème]{.ul}**

Une société de location de voitures propose à ses clients deux contrats
:

-   Contrat 1 : un forfait de 50€ puis 0,40€ par km parcouru.

-   Contrat 2 : 0,80€ par km parcouru.

a.  Écrire deux fonctions prix1(x) et prix2(x) qui renvoient le prix
    payé avec chaque contrat pour x kilomètres parcourus.

b.  En utilisant les fonctions précédentes, écrire une fonction
    plusAvantageux(x) qui renvoie le numéro du contrat le plus
    avantageux.

```{=html}
<!-- --
```
3)  **[Nombres de Kaprekar]{.ul}**

Un nombre de Kaprekar est un nombre dont l'écriture décimale du carré
de ce nombre peut être séparée en deux nombres (pas forcément de même
taille) dont la somme vaut le nombre initial.

[Exemples :]{.ul}

9 est un nombre de Kaprekar car 9²=81 et on peut séparer 81 en 8 et 1
dont la somme 8+1 = 9.

45 est un nombre de Kaprekar car 45²=2025 et on peut séparer 2025 en
20+25=45.

12 n'est pas un nombre de Kaprekar car 12²=144 et on ne peut pas couper
ce nombre pour trouver 12 (1+44=45, 14+4=18).

4 879 est un nombre de Kaprekar car 4879² = 23804641 et 238 + 04 641 = 4
879.

Créer un programme qui renvoie si un nombre entier **n** est de Kaprekar
ou pas.