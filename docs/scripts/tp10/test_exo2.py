def valider_valeur(T, a, b):
    return all(map(lambda x: a<=x<=b, T))

b1 = ("générer_tableau_0(3) == [0]*3", "générer_tableau_0(100) == [0]*100", "générer_tableau_0(0) == []",)
b2 = ("valider_valeur(générer_tableau_aléatoire(3, 1, 6), 1, 6) == True", \
      "valider_valeur(générer_tableau_aléatoire(3, 1, 1), 1, 1) == True", \
      "valider_valeur(générer_tableau_aléatoire(100, 1, 100), 1, 100) == True",)

benchmark = [b1, b2 ]