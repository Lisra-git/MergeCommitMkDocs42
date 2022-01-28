def renvoyer_ligne(tableau : list[list[int]], n_ligne : int) -> list[int]:
    if not (0 < n_ligne < len(tableau)):
        return []
    return tableau[n_ligne]

T = [[1,2,3], [4,5,6,7], [8,9]]
nouveau_tableau = renvoyer_ligne(T, 1)
print(nouveau_tableau)