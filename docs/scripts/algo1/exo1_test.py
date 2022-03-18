assert recherche_dichotomique([1,2,3], 1) == True
assert recherche_dichotomique([8,12,13,22,67,69], 22) == True
assert recherche_dichotomique([8,12,13,22,67,69,125,127], 23) == False
assert recherche_dichotomique([1,2,3], 0) == False
assert recherche_dichotomique([], 0) == False