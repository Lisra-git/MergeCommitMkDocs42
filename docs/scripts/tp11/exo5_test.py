assert renvoyer_colonne([[1,2,3], [4,5,7], [8,9,7]], 0) == [1,4,8], \
    'renvoyer_colonne([[1,2,3], [4,5,7], [8,9,7]], 0) == [1,4,8]'
assert renvoyer_colonne([[1,1,0], [4,5,0], [8,9,0]], 2) == [0,0,0], \
    'renvoyer_colonne([[1,1,0], [4,5,0], [8,9,0]], 2) == [0,0,0]'