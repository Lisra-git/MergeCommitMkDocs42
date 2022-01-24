def valider_valeur(T, a, b):
    return all(map(lambda x: a<=x<=b, T))

b1 = ("compter_répétition([1,3,6], 6) == 1", "compter_répétition([8,8,8], 8) == 3", "compter_répétition([1, 8, 1, 8], 8) == 2", "compter_répétition([1,3,99], 100) == 0")

benchmark = [b1, ]