# Tableaux et tuples

Reparler de len


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

    

## Terminal, console et éditeur de code


pointsDeMana = 6.5 et persoVivant = True

Affichez les types de ces variables dans le terminal à l'aide de
l'instruction **print**(......).

[Remarque :]{.ul}

On utilise la notation anglo-saxonne avec . pour la virgule, et e pour
\"10 puissance\". Par exemple : 1.5e4 = 15000

--- À faire vous-même 10 ---

Dans votre programme, à partir de la variable ageJoueur et des
opérations de transtypage, créez les variables suivantes :

Il y a 3 minuttes

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