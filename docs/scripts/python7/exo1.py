panier_de_fruits = {}

def liste_de_course(panier, fruit):
    pass



# Tests
assert liste_de_course(panier_de_fruits, 'mandarine')['mandarine'] == 0
assert liste_de_course(panier_de_fruits, 'pomme')['pomme'] == 0
for fruit in ['prune', 'abricot', 'coing']:
    assert liste_de_course(panier_de_fruits, fruit)[fruit] == 0    