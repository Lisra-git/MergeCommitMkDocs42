assert renvoyer_ligne([[1,2,3], [4,5,6,7], [8,9]], 0) == [1,2,3], \
    'renvoyer_ligne([[1,2,3], [4,5,6,7], [8,9]], 0) == [1,2,3]'
assert renvoyer_ligne([[], [4,5,6,7], [8,9]], 2) == [8, 9], \
    'renvoyer_ligne([[], [4,5,6,7], [8,9]], 2) == [8, 9]'
