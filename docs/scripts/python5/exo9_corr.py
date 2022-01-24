def trouver_maximum(T):
    maximum = T[0]
    for élément in T:
        if élément > maximum:
            maximum = élément
    return maximum

tableau = [4, 5, 3, 9, 12, 5, 3, 1]
maximum = trouver_maximum(tableau)
print(maximum)