def trier(T):
    for i in range(len(T)):
        for j in range(len(T)):
            if T[i] < T[j]:
                T[i], T[j] = T[j], T[i]
    return T

T = [5, 3, 9, 1, 8, 3, -1, 9, 1]
print(T)
T = trier(T)
print(T)