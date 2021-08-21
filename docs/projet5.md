# Projet : création d'une rue

!!! warning "But"

    Le but de ce projet est de travail sur la notion de fonctions. Les fonctions doivent 

## Présentation du projet

On souhaite écrire un programme qui permet de générer aléatoirement le dessin d’une rue d'immeubles, vu de profil. On utilisera pour cela le module `#!python turtle` de Python.

FAIRE LE DESSIN AVEC LE CODE FINAL
{{IDE(projet5/rue_final.py)}}

## Contraintes

Les contraintes urbanistiques sont les suivantes :

- les immeubles ont au minimum un rez-de-chaussée et au maximum 4 étages (5 niveaux) ;
- les immeubles ont une largeur de 140 pixels ;
- les immeubles ont une couleur unique pour toute la façade ;
- chaque niveau (rez-de-chaussée ou étage) a une hauteur de 60 pixels ;
- les rez-de-chaussée n'ont qu'une seule porte ;
- toutes les fenêtres sont identiques, de taille 30 pixels sur 30 pixels ;
- toutes les portes et portes-fenêtres ont une largeur de 30 pixels ;

Tout le reste est libre et donc personnalisable.

## Travail à réaliser

Proposer un programme qui réponde au problème posé en utilisant le module `#!python turtle` de Python. Le but est de réaliser ce travail en faisant appel aux fonctions les plus unitaires possibles.