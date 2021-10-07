tableau = [1, 2, 3, 4, 5]
accumulateur = 0

for nombre in tableau:
    accumulateur = accumulateur + nombre
    # accumulateur += nombre   # fonctionne également

print(accumulateur)