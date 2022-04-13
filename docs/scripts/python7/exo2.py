panier_de_fruits = {'pomme' : 0, 'poire' : 0, 'abricot' : 0}

def ajouter_fruit(panier, fruit):
    pass



# Tests
assert ajouter_fruit(panier_de_fruits, 'mandarine') == panier_de_fruits
assert ajouter_fruit(panier_de_fruits, 'pomme')['pomme'] == 1