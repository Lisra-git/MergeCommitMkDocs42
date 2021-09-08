# Modularité

## Principe

Pourquoi un _vieux_ langage informatique comme C est-il toujours massivement utilisé alors que COBOL a complètement disparu ? Pourquoi Python est-il devenu un langage si populaire ?

Une des raisons est **l'existence de modules**, appelés aussi librairies, bibliothèques ou packages. Les modules sont des programmes qui contiennent des fonctions _ou classes_ qu'un utilisateur est amené à utiliser à un moment donné. On peut les voir comme des boîtes à outils, permettant de faire des tâches sans avoir besoin de les programmer soit-même.

Un avantage de Python est la [quantité très importante de modules disponibles](https://docs.python.org/fr/3/py-modindex.html){target="_blank"} dans la version standard. Et ne parlons pas [des centaines de milliers de modules](https://pypi.org){target="_blank"} créés par les utilisateurs de Python et simplifiant la vie de milliers d'utilisateurs[^pml]. 

[^pml]: ce site web va chercher une bibliothèque écrite par mes soins ![ici](https://pypi.org/project/pyo-js-turtle/#files){target="_blank"} !

## Importation de modules

Nous avons déjà rencontré les modules `#!python turtle`, `#!python math` et `#!python random` dans les chapitres précédents.

Passons en revue les méthodes permettant d'importer un module.

### Charger un module

!!! {{cours()}}
    L'instruction `#!python import module` donne accès à toutes les "variables" et "fonctions" du module `#!python module`. 

    On appelle une fonction `#!python fonction` du module `#!python module` en écrivant : `#!python module.fonction(param_1, param_2...)`. `#!python param_1`, `#!python param_2`... sont les paramètres de la fonction.

    !!! example "Exemple"
        ```python
        import math
        math.pi # affiche la valeur de pi
        math.cos(math.pi) # affiche la valeu de cos(pi)
        ```

        - [ ] Recopier ce code d'exemple dans le terminal ci-dessous. Les résultats sont-ils conformes à vos attentes ?
        - [ ] Ajouter le calcul du sinus $\sin$ de $\dfrac{\pi}{2}$.
        - [ ] Ajouter le calcul de la racine carrée (fonction `#!python sqrt(...)` de 3.

        {{terminal()}}

!!! {{cours()}}

    Il est parfois fastidieux d'écrire systématiquement le nom du module. On peut alors faire appel à un **alias** qui va remplacer le nom du module.

    L'instruction `#!python import module as md` donne accès à toutes les "variables" et "fonctions" du module `#!python module` renommé par l'alias `#!python md`.

    !!! example "Exemple"

        === "Avec alias"

            ```python
            import matplotlib.pyplot as plt
            plt.figure(1)
            plt.plot([i/2 for i in range(2, 7)], [5, -2, -5, 1, 3])
            plt.show()
            ```

        === "Sans alias"
        
            ```python
            import matplotlib.pyplot
            matplotlib.pyplot.figure(1)
            matplotlib.pyplot.plot([i/2 for i in range(2, 7)], [5, -2, -5, 1, 3])
            matplotlib.pyplot.show()
            ```

!!! tip "Manipuler des modules"

    === {{exercice(False, 0)}}




### Importation de fonctions d'un module

!!! {{cours()}}

    

!!! danger "Importation par wildcard"

    Dans de rares cas, on souhaite utiliser l'intégralité d'un module.

    ??? {{ext()}}

        On peut afficher les méthodes ou variables associées à un programme à l'aide de l'instruction `#!python dir()`.

        Chercher les différences entre les méthodes accessibles lorsque vous recopiez dans le terminal le programme ci-dessous.

        ```python
        dir(), len(dir())
        
        import random
        dir(), len(dir())
        
        from random import *
        dir(), len(dir())
        ```

        {{terminal()}}

        On remarque que seul le nom du module est chargé, pas le contenu.

## Création de modules

{{terminal()}}

Assez rapidement, il deviendra intéressant de créer vos propres modules afin de ne pas réécrire constamment les mêmes programmes.
