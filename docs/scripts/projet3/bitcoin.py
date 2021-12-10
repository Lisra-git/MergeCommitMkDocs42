import timeit
import random

p_easy = 101
p_mid  = 15486869
p_hard = 2276856017

def verification(x, y, p = p_easy, marge=0):
    return (x**2-y) % p <= marge

def racine_approchee(y, p = p_easy, marge = 0):  # racine_approchee
    x = 0
    while not verification(x, y, p, marge):
        x+=1
    return x
    

# print(timeit.timeit("verification(6543210, 8371779, 15486869)", globals=globals()))

# print(timeit.timeit("racine_approchee(17, 101)", globals=globals(), number=5)/5)
# print(timeit.timeit("racine_approchee(8371779, p_mid)", globals=globals(), number=1)/1)
# print(timeit.timeit("racine_approchee(8371779, p_mid, 20)", globals=globals(), number=1)/1)
# print(timeit.timeit("racine_approchee(8371779, p_hard, 20)", globals=globals(), number=1)/1)
# print(racine_approchee(17, 101))
# print(racine_approchee(8371779, p_mid))
# print(racine_approchee(8371779, p_hard, 20))
