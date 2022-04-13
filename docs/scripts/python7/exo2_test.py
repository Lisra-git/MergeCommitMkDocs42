panier_de_fruits = {}
assert ajouter_fruit(panier_de_fruits, 'mandarine')['mandarine'] == 0
assert ajouter_fruit(panier_de_fruits, 'pomme')['pomme'] == 0
for fruit in ['prune', 'abricot', 'coing']:
    assert ajouter_fruit(panier_de_fruits, fruit)[fruit] == 0