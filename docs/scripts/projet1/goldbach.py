from math import sqrt

def vérifier_nombre(entier):
    """ Vérifie si un nombre entier est strictement supérieur à 1 """
    if entier < 0 or entier == 0 or entier == 1: 
        return False
    else : 
        return True

def est_premier_lent(entier):
    """ 
    Vérifie si un nombre entier est premier, version lente
    """
    diviseur = 2
    if vérifier_nombre(entier): # si le nombre est valide
        # on parcourt tous les diviseurs de 2 à entier
        while diviseur < entier: 
            # on teste la divisibilité de entier par diviseur
            if entier % diviseur == 0:
                return False
            # on incrémente le diviseur
            diviseur = diviseur + 1
        return True
    else: 
        return False

def est_premier(entier):
    """ 
    Vérifie si un nombre entier est premier de manière rapide
    """
    diviseur = 2
    if vérifier_nombre(entier):
        # on parcourt tous les diviseurs de 2 à la racine de entier
        # on fait donc sqrt(entier) fois la boucle
        while diviseur <= sqrt(entier):
            if entier % diviseur == 0:
                return False
            diviseur = diviseur + 1
        return True
    else: 
        return False

def est_nombre_goldbach(entier_pair):
    # on parcourt tous les entiers pairs de 2 à entier_pair
    for n in range(entier_pair):
        # Un nombre de Golbach est de la forme entier_pair = n + n2
        # donc n2 = entier_pair - n avec n et n2 nombres premiers.
        if est_premier(n) and est_premier(entier_pair - n):
            #print(entier_pair, n, entier_pair-n)
            return True, n
    return False, entier_pair

def tester_conjecture_goldbach(nombre_maximum):
    entier_pair = 4
    nombre_de_nombre_goldbach = 0
    nombre_de_passage_boucle = 0
    while entier_pair <= nombre_maximum:
        # on teste si on a un nombre de Goldbach ou non.
        reponse, n_1 = est_nombre_goldbach(entier_pair)
        if reponse :
            print(entier_pair, n_1, entier_pair - n_1)
            nombre_de_nombre_goldbach = nombre_de_nombre_goldbach + 1
        # on rajoute 2 à entier_pair pour qu'il reste pair !
        entier_pair = entier_pair + 2
        nombre_de_passage_boucle += 1
    return nombre_de_nombre_goldbach / nombre_de_passage_boucle

print(est_premier_lent(7))
# print(tester_conjecture_goldbach(100000))


