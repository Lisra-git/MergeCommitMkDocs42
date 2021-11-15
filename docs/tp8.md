# TP 8 : Exercices sur les tableaux et les fonctions

## Exercice 1 ✪

Écrire une fonction `#!python mesurer` qui prend en paramètre :

- un `#!python tableau` de taille quelconque.

Cette fonction renvoie la taille du tableau.

{{IDEv('tp8/exo1')}}

## Exercice 2 ✪

- [ ] Compléter la fonction `#!python générer_tableau_0` qui prend en paramètre :

    - un entier `#!python nombre_éléments`.

    Cette fonction renvoie un tableau de taille `#!python nombre_éléments` contenant uniquement des 0.

- [ ] Modifier la fonction `#!python générer_tableau_aléatoire` qui prend en paramètres :

    - un entier `#!python nombre_éléments` ;
    - deux entiers `#!python a` et `#!python b`;

    Cette fonction renvoie un tableau de taille `#!python nombre_éléments` contenant des nombres entiers aléatoires entre `#!python a` et `#!python b`.

    Rappel : pour générer des nombres aléatoires entre `#!python a` et `#!python b`, on utilisera `#!python random.randint(a, b)`.

{{IDE('tp8/exo2')}}

## Exercice 3 ✪

Compléter la fonction `#!python vérifier_appartenance` qui prend en paramètres :

- un tableau d'entiers `#!python T` ;
- un entier `#!python x`.

Cette fonction renvoie `#!python True` si la valeur appartient au tableau et `#!python False` sinon.

{{IDEv('tp8/exo3')}}

## Exercice 4 ✪

Écrire une fonction `#!python compter_répétition` qui prend en paramètres :

- un tableau d'entiers `#!python T` ;
- un entier `#!python élément`.

Cette fonction compte le nombre de fois où l'élément `#!python élément` figure dans le tableau `#!python T`.

??? help "Aide"

    On aura sans doute besoin d'un accumulateur comptant le nombre de répétitions...

{{IDEv('tp8/exo4')}}

## Exercice 5 ✪

Écrire une fonction `#!python spiraler` qui prend en paramètres :

- un tableau d'entiers `#!python T`.

Cette fonction dessine une spirale carrée (angle à 90°) dont la longueur est donnée par les valeurs du tableau T.

{{IDEv('tp8/exo5')}}

??? help "Aide"

    On utilisera `#!python turtle.forward(L)` pour avancer d'une longueur L et `#!python turtle.right(A)` pour tourner à droite d'un angle A.

## Exercice 6 ✪✪

Écrire la fonction `#!python trouver_indice` qui prend en paramètres :

- un tableau d'entiers `#!python T` ;
- un entier `#!python x`.

Cette fonction renvoie :

- l'indice `#!python i` de la position du premier entier du tableau égal à `#!python x` ;
- `#!python None` sinon.

{{IDEv('tp8/exo6')}}

## Point cours !

!!! {{cours()}}

    Il est également possible de modifier les valeurs d'un tableaux en accédant à ses éléments **par indice**.

    Ainsi :
    ```python 
    T = [1, 2, 3]
    for i in range(len(T)):
        T[i] = T[i] * 2
    print(T)
    ```

    permet de multiplier par 2 tous les éléments du tableau `#!python T`.

    Essayez cet exemple dans le terminal ci-dessous :

    {{terminal()}}

## Exercice 7 ✪

En vous aidant des commentaires, écrire la fonction `#!python ajouter_lettre` qui prend en paramètres :

- un tableau de lettres `#!python T` de taille `#!python len(T)`;
- une lettre `#!python lettre`.

Cette fonction renvoie un tableau de lettres `#!python T` de taille `#!python len(T) + 1`. 

Par exemple :

```bash
ajouter_lettre(['c', 'a', 't'], 's')
```
renvoie
```bash
['c', 'a', 't', 's']
```

{{IDEv('tp8/exo7')}}

## Exercice 8 ✪

Compléter la fonction `#!python concaténer` qui prend en paramètres :

- un tableau de nombres entiers `#!python T1` de taille `#!python len(T1)`;
- un tableau de nombres entiers `#!python T2` de taille `#!python len(T2)`;

Cette fonction renvoie un tableau d'entiers `#!python T` de taille `#!python len(T1) + len(T2)`. 

Par exemple :

```bash
concaténer([8, 6, 4], [1, 2])
```
renvoie
```bash
[8, 6, 4, 1, 2]
```

{{IDEv('tp8/exo8')}}

## Exercice 9 ✪

Écrire la fonction `#!python prefixe` qui prend en paramètres :

- un tableau de nombres entiers `#!python T1` de taille `#!python len(T1)`;
- un tableau de nombres entiers `#!python T2` de taille `#!python len(T2)`;

Cette fonction renvoie `#!python True` si le tableau `#!python T2` commence par tous les éléments du tableau `#!python T1` dans le même ordre et `#!python False` sinon.

{{IDEv('tp8/exo9')}}

## Exercice 10 ✪✪

Écrire la fonction `#!python suffixe` qui prend en paramètres :

- un tableau de nombres entiers `#!python T1` de taille `#!python len(T1)`;
- un tableau de nombres entiers `#!python T2` de taille `#!python len(T2)`;

Cette fonction renvoie `#!python True` si le tableau `#!python T2` termine par tous les éléments du tableau `#!python T1` dans le même ordre et `#!python False` sinon.

{{IDEv('tp8/exo10')}}

??? help "Aide"

    Pour lire un tableau dans le sens inverse, il faut trouver une formule à appliquer sur les indices du tableau. 

    Par exemple, un tableau de taille 4 va se parcourir ainsi sur l'indice `#!python i` par ordre croissant :

    |i|0|1|2|3|
    |-|-|-|-|-|
    |???|3|2|1|0|

    Quelle sera la formule à écrire à la place des ??? pour obtenir 3 quand i vaut 0; 2 quand i vaut 1 etc.

## Exercice 11 ✪✪

- [ ] Écrire la fonction `#!python déterminer_minimum` qui prend en paramètres :

    - un entier `#!python taille_T1` ;
    - un entier `#!python taille_T2` ;

    Cette fonction renvoie le maximum des deux tailles.

- [ ] Écrire la fonction `#!python distance_hamming` qui prend en paramètres :

    - un tableau de chaîne de caractères `#!python T1` de taille `#!python len(T1)`;
    - un tableau de chaîne de caractères `#!python T2` de taille `#!python len(T2)`;

    Cette fonction renvoie le nombre de lettres qui diffère d'un tableau à l'autre. Si les tableaux sont de taille différente, les caractères en trop seront comptés comme des différences : on utilisera la fonction `#!python déterminer_minimum` pour comparer la taille des tableaux.

    Par exemple :

    ```bash
    distance_hamming(['t', 'o', 't', 'o'], ['t', 'a', 't', 'a'])
    ```
    renvoie
    ```bash
    [8, 6, 4, 1, 2]
    ```

{{IDE('tp8/exo11')}}


## Exercice 12 ✪✪✪

Comme nous le verrons par la suite, les algorithmes de tri de tableaux sont un cas fondamental en théorie informatique. Ils permettent d'aborder la notion d'efficacité au travers de la complexité (~ le coût) d'un algorithme.

Nous proposons ici d'implémenter une méthode de tri très simple.

Prenons le tableau suivant : `#!python [5, 3, 2, 7]` 

???+ warning "Premier passage dans la boucle externe"
    
    Étape `#!python i = 0` : plaçons le plus petit élément à l'**indice 0** du tableau.

    |Passage `#!python j = 0`|**5**|3|2|7| `#!python 5 == 5` → On ne fait rien.|
    |-|-|-|-|-|:-|
    |Passage `#!python j = 1`|5|**3**|2|7| `#!python 3 <= 5` → On échange `#!python T[1]` avec `#!python T[0]` |
    |Passage `#!python j = 2`|3|5|**2**|7| `#!python 2 <= 3` → On échange `#!python T[2]` avec `#!python T[0]`|
    |Passage `#!python j = 3`|2|5|3|**7**| `#!python 7 >= 2` → On ne fait rien.|

    `#!python i = 0` contient l'élément le plus petit.

??? warning "Deuxième passage dans la boucle externe"

    Étape `#!python i = 1` : plaçons le second plus petit élément à l'**indice 1** du tableau.

    |Passage `#!python j = 0`|2|5|3|7| `#!python 2 <= 5` → On ne fait rien.|
    |-|-|-|-|-|:-|
    |Passage `#!python j = 1`|2|**5**|3|7| `#!python 5 == 5` → On ne fait rien |
    |Passage `#!python j = 2`|2|5|**3**|7| `#!python 3 <= 5` → On échange `#!python T[2]` avec `#!python T[1]`|
    |Passage `#!python j = 3`|2|3|5|**7**| `#!python 7 >= 3` → On ne fait rien.|

    `#!python i = 1` contient le deuxième élément le plus petit. Les deux premiers éléments du tableau sont triés dans l'ordre croissant.

L'algorithme comporte donc deux boucles imbriquées l'une dans l'autre. À chaque fois qu'on trouve un nouvel entier plus petit qu' l'entier situé à la position `#!python i`, on l'inverse avec celui situé à la position `#!python j`.

Écrire une fonction `#!python trier` qui prend pour paramètre un tableau `#!python T` et réalise le tri de ce tableau selon l'algorithme ci-dessus. 
La fonction renvoie un tableau trié dans l'ordre croissant.

{{IDEv('tp8/exo12')}}