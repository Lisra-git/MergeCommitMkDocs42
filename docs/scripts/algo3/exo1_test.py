from random import randint

tab1 = [randint(-100, 100) for i in range(10)]

assert tri_insertion([1,5,3]) == sorted([1, 3, 5])
assert tri_insertion(tab1) == sorted(tab1)
assert tri_insertion([]) == []
