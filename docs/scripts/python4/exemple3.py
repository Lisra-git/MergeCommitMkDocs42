import random

def générer_couleur_RGB():
    """ Génère les composantes Rouge, 
    Vert, Bleu entre 0 et 1. """
    rouge = random.random()
    vert = random.random()
    bleu = random.random()
    return rouge, vert, bleu

r, g, b = générer_couleur_RGB()
print(r, g, b)