panier_de_fruits = {'pomme' : 0, 'poire' : 0, 'abricot' : 0}

def ajouter_fruit(panier, fruit):
    if fruit not in panier:
        print("Ce fruit n'est pas sur la liste de courses")
    else :
        panier[fruit] = panier[fruit] + 1
    return panier


# Tests
assert ajouter_fruit(panier_de_fruits, 'mandarine') == panier_de_fruits
assert ajouter_fruit(panier_de_fruits, 'pomme')['pomme'] == 1
for i in range(10):
    assert ajouter_fruit(panier_de_fruits, 'poire')['poire'] == i+1