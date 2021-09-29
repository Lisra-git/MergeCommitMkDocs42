# Structures de contrôle : boucles

## Principe

En programmation, un principe important est le **principe DRY**. Cet acronyme signifie **D**on't **R**epeat **Y**ourself. Il suggère qu'un bon programme informatique ne contient pas de répétitions et évite les copier/coller. 

Si votre programme comporte trop de répétitions, il faut utiliser de nouvelles structures permettant d'éviter cela.

!!! example "Utilité des boucles"

    On veut ajouter quatre pièces de 2€ dans une urne. Voici le programme proposé.

    {{IDE('python3/exo1')}}

    - [ ] Affichez le contenu de l'urne dans le terminal.
    - [ ] Complétez le programme ci-dessus afin d'ajouter 2 nouvelles pièces de 2€ (total de 6 pièces). 
    - [ ] Imaginez que l'on veuille maintenant ajouter 5 nouvelles pièces. Complétez le programme ci-dessus. 
    - [ ] Et pour 7296 nouvelles pièces, comment feriez-vous ?

En programmation, on est amené à répéter de nombreuses fois une même instruction ou bloc d'instructions. On introduit donc une nouvelle structure de contrôle appelée **boucles**.

On distingue :

- les boucles conditionnelles ;
- les boucles inconditionnelles.

## Définition générale

!!! {{cours()}}

    Une boucle est une structure de contrôle permettant de répéter un bloc d'instructions selon une certaine condition.

    Ce type d'instructions est essentielle à tout langage de programmation.

!!! tip "Comprendre l'intérêt des boucles"

    === {{exercice(False, 0)}}
        Le programme suivant comporte-t-il une boucle ? 
        ``` linenums="1"
        Faites fondre le chocolat cassé en morceaux avec le beurre.
        Battez les oeufs avec le sucre jusqu'à ce que le mélange blanchisse.
        Ajoutez la farine, le sucre vanillé, et ajoutez le chocolat.
        Versez le tout dans un moule, et enfournez à 180°C pendant 15 min.
        ```

        ??? help "Solution"

            Ce programme ne comporte pas de boucle. Chaque instruction est exécutée une seule fois.

    === {{exercice(False)}}
        Le programme suivant comporte-t-il une boucle ? 
        ``` linenums="1"
        Pour multiplier 12 par un nombre entier n, on fait :
        resultat = 0              # 0 fois
        resultat = resultat + 12  # 1 fois
        resultat = resultat + 12  # 2 fois
        resultat = resultat + 12  # 3 fois
        ...
        resultat = resultat + 12  # n fois
        ```

        ??? help "Solution"

            Ce programme comporte une boucle. Chaque instruction est répétée `n` fois (`n` peut même être égal à 0!).

            La condition est cachée. On continue tant que l'addition n'a pas été répétée `n` fois.

    === {{exercice(False)}}
        Le programme suivant comporte-t-il une boucle ? 
        ``` linenums="1"
        Mettre l'eau dans le sucre et mettre le plein feu pendant 3 minutes.
        À l'aide d'un thermomètre de cuisson, mesurez la température.
        Tant que la température n'est pas supérieure à 127°C, ajoutez 1 minute de cuisson puis mesurez à nouveau la température.
        Une fois la température supérieure à 127°C, retirez du feu.
        ```

        ??? help "Solution"

            Ce programme comporte une boucle. Une instruction (la mesure de température) doit être répétée autant de fois que nécessaire pour dépasser les 127°C. 
            
            La condition est donc `temperature >= 127°C`.

    === {{exercice(False)}}
        Le programme suivant comporte-t-il une boucle ? 
        ``` linenums="1"
        Pensez à un nombre entier positif n.
        Multipliez le nombre 1 par 2, 
        multipliez le nombre obtenu (2) par 3,
        multipliez le nombre obtenu (6) par 4,
        etc.
        multipliez le nombre obtenu par n
        Vous venez de calculer la factorielle du nombre n !
        ```

        ??? help "Solution"

            Ce programme comporte une boucle. On répète une instruction (la multiplication par un nombre) un certain nombre de fois.
            
            La condition est cachée. On continue tant que le nombre par lequel on multiplie est différent de `n`.

    === {{exercice(False)}}
        Le programme suivant comporte-t-il une boucle ? 
        ``` linenums="1"
        Mettre l'eau dans le sucre et mettre le plein feu pendant 3 minutes.
        À l'aide d'un thermomètre de cuisson, mesurez la température.
        Si la température est supérieure à 127°C, ajoutez 50mL d'eau.
        Mesurez à nouveau la température puis retirez du feu.
        ```

        ??? help "Solution"

            Ce programme ne comporte pas de boucle mais une conditionnelle. Chaque instruction est exécutée une seule fois : on remarque d'ailleurs que la seconde mesure de température ne sert à rien !

## Boucles conditionnelles _while_

La structure de contrôle correspondant le plus au graphe de contrôle du paragraphe 2 est la boucle conditionnelle.

!!! {{cours()}}

    !!! tip inline end "_Graphe de controle_"
        ```mermaid
        graph TD;
        A[début code]-->p("condition");
        p-->|Vrai|B[bloc code A]-->p;
        p-->|Faux|C[suite code];
        class p if;
        ```

    En Python, la syntaxe des boucles conditionnelles est la suivante :
    
    ```python
    début code
    while condition :
        bloc code A
    suite code
    ```

    !!! example "Exemple"

        Tester le code ci-dessous :

        {{IDEv('python3/exemple1')}}

    Une boucle conditionnelle `#!python while` nécessite donc **trois** éléments pour fonctionner correctement :

    - Initialisation de la variable d'itération avant la boucle (ligne 1).
    - Condition (expression booléenne) permettant de continuer la boucle ou non (ligne 2).
    - Modification de la variable d'itération (appelé parfois incrémentation) (ligne 4).

    ??? {{ext()}}
        Dans les langages permettant la sortie anticipée de boucle (avec `#!python break`, `#!python return` ou `#!c goto`), les boucles conditionnelles peuvent être vues comme inutiles. 
            
        Ce n'est pas le cas des langages fonctionnels dont nous parlerons en Terminale : prenez donc l'habitude d'utiliser ces boucles conditionnelles pour ne pas dépendre du langage Python en particulier.

!!! tip "Manipuler des boucles conditionnelles"

    === {{exercice(False)}}

        - [ ] Lire le programme ci-dessous et prédire son fonctionnement.
        - [ ] Tester le programme afin de vérifier votre prédiction.

        {{IDEv('python3/exo6')}}

        ??? help "Solution" 

            Il affiche les nombres de 1 à 10 inclus. Il affiche un nombre par ligne. 

    === {{exercice(False)}}

        À l'aide d'une boucle conditionnelle, affichez **sur une seule ligne** les nombres de 1 à 10 exclus. 

        On modifiera le programme de l'exercice précédent.
        
        On utilisera l'[option](https://docs.python.org/fr/3/library/functions.html#print){target="_blank"} `#!python print(..., end = " ")` afin d'éviter qu'un affichage nous ramène à la ligne.

        {{IDEv('python3/exo7')}}

    === {{exercice(False)}}

        À l'aide d'une boucle conditionnelle, affichez **sur une seule ligne** les nombres de 10 à 1 inclus.

        On s'inspirera du programme de l'exercice précédent.

        On utilisera l'[option](https://docs.python.org/fr/3/library/functions.html#print){target="_blank"} `#!python print(..., end = " ")` afin d'éviter qu'un affichage nous ramène à la ligne.

        {{IDEv('python3/exo8')}}

    === {{exercice(False)}}

        - [ ] Lire le programme ci-dessous et prédire son fonctionnement.
        - [ ] Tester le programme afin de vérifier votre prédiction.
        - [ ] Proposer une modification simple permettant de supprimer l'instruction conditionnelle.

        {{IDEv('python3/exo9')}}

        ??? help "Solution" 

            Il affiche les nombres de 1 à 10 inclus. Il affiche un nombre par ligne. 

    === {{exercice(False)}}

        La suite de Syracuse est une suite d'entiers naturels définie simplement : 
    
    === {{exercice(False)}}

        On pose n = 0
        Pour calculer $2^n$, il convient de calculer d'abord $2\times 2$
        Compléter le programme afin qu'il calcule une puissance de 2.

        Que fait le programme suivant ? 

        {{IDEv('python3/exo10')}}

        ??? help "Solution" 

            Il affiche les nombres de 1 à 10 inclus. Il affiche un nombre par ligne. 
    
    === {{exercice(False)}}

        <!-- AJOUTER UN EXERCICE PLUS COMPLEXE !!!! -->

        Que fait le programme suivant ? 

        {{IDEv('python3/exo6')}}

        ??? help "Solution" 

            Il affiche les nombres de 1 à 10 inclus. Il affiche un nombre par ligne. 
    
    === {{exercice(False)}}

        Que fait le programme suivant ? 

        ```python 
        i = 0
        while i < 10:
            print('Jusque là, tout va bien.')
        ```

        ??? help "Solution" 

            Ce programme affiche `#!python 'Jusque là, tout va bien.'` mais ne s'arrête jamais ! En effet, la valeur de la variable de boucle n'est jamais incrémentée et n'atteint donc jamais 10.

!!! danger "Boucles infinies"

    Dans le cadre des boucles conditionnelles, la question de l'arrêt d'un programme se pose.

    Il faut donc toujours se demander si notre expression booléenne sera vérifiée à un moment du programme.

    Dans un éditeur de code (Thonny, VSCodium...), vous pouvez néanmoins toujours stopper l'exécution d'un script Python à l'aide de la combinaison de touches ++ctrl+c++.

## Boucles inconditionnelles _for_

!!! {{cours()}}

    En Python, la syntaxe des boucles inconditionnelles est la suivante :
    
    ```python
    début code
    for variable_boucle in itérable :
        bloc code A
    suite code
    ```

    !!! help "Qu'est-ce qu'un itérable ?"

        Pour nous, il s'agit d'une **chaîne de caractères** ou d'un **tableau**, car ceux-ci sont composés d'éléments que l'on peut épeler : la lettre ou l'élément.

    !!! example "Exemple 1 (important!)"

        - [ ] Tester le code ci-dessous/
        - [ ] Que fait le code ? Est-ce conforme à notre définition d'un itérable ?

        {{IDEv('python3/exemple2')}}

    !!! example "Exemple 2 (important!)"

        - [ ] Tester le code ci-dessous/
        - [ ] Que fait le code ? Est-ce conforme à notre définition d'un itérable ?

        {{IDEv('python3/exemple3')}}

        

    ??? {{ext()}}

        Dans le détail, un itérable peut être créé en Python avec la fonction `#!python iter()`. 
        
        On itère sur l'itérable à l'aide de la fonction `#!python next()`. 

        - [ ] Lancer le code ci-dessous et dans la console de l'éditeur ci-contre, écrire `#!python next(iterable)`.
        - [ ] Répéter cette commande et observer le mot en train d'être épelé. La valeur référencée par la variable `#!python lettre` de la boucle `#!python for` est donc définie grâce à un appel à `#!python next()` d'un itérateur.
        - [ ] Remarquer l'erreur `#!python StopIteration` qui apparaît une fois l'itérable complètement épelé.
        - [ ] Modifier `#!python mot ='python'` en `#!python mot = 12345` et réitérer l'itération. Cela fonctionne-t-il ? 

        {{IDEv('python3/exemple4')}}


!!! {{cours()}}

    Très souvent, `#!python variable_boucle` est nommé `#!python i`.

A venir

Introduire la syntaxe len, range

Donner de nombreux détails sur les chaînes de caractères avec des exos associés

## Exercices récapitulatifs

!!! {{cours()}}

    Quand on ne connaît pas à l'avance le nombre de répétitions, on utilise une boucle conditionnelle.

    Quand on veut épeler des éléments un à un ou que l'on connaît le nombre de répétitions à effectuer, on utilise une boucle inconditionnelle.

!!! {{exercice()}}

    On imagine une puce qui se déplace aléatoirement sur une ligne, en avant ou en arrière, par pas de 1 ou -1. 
    
    Par exemple : 
    
    - si elle est à l'emplacement 0, elle peut sauter à l'emplacement 1 ou -1 ; 
    - si elle est à l'emplacement 2, elle peut sauter à l'emplacement 3 ou 1.

    Avec la boucle de votre choix, simuler le mouvement de cette puce de l'emplacement initial 0 à l'emplacement final 5 (voir le schéma de la figure 3). Combien de sauts sont nécessaires pour réaliser ce parcours ? Relancez plusieurs fois le programme. Trouvez-vous le même nombre de sauts à chaque exécution ?

    ![sauts-de-puce](images/python3/sauts-de-puce.png "Sauts de puce"){: style="width:40%;"}


    !!! help "Générer des nombres aléatoires"
        Afin de générer des nombres aléatoires, nous importons le module `#!python random`. Le programme proposé utilise également l'instruction random.choice([-1, 1]) qui renvoie au hasard la valeur -1 ou 1 avec une probabilité $\dfrac{1}{2}$. 
    
        Nous reverrons la signification de cette syntaxe particulière dans le chapitre sur la [modularité](python6.md).

!!! danger "Résumé"

    Dans ce chapitre, j'ai appris : 
    
    - [ ] blabla
    - [ ] blabla
    - [ ] blabla
    - [ ] blabla
    - [ ] blabla