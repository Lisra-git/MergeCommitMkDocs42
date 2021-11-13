import random 
jeté_3_dés = [random.randint(1,6) for i in range(3)]

for i in range(len(jeté_3_dés)):
    print(i, jeté_3_dés[i])