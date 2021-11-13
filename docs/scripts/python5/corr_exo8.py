def trouver_maximum(T):
    maximum = T[0]
    indice_maximum = 0
    for i in range(len(T)):
        if T[i] > maximum:
            maximum = T[i]
            indice_maximum = i
    return indice_maximum

tableau = [4, 5, 3, 9, 12, 5, 3, 1]
indice_max = trouver_maximum(tableau)
print(indice_max)