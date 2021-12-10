def créer_tableau_cyclique(n: int, n_cycle: int) -> list[int]:
    return [i % n_cycle for i in range(n)]

print(créer_tableau_cyclique(10, 3))