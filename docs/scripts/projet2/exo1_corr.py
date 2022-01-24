def ajouter_lettre(T, lettre):
    taille = len(T)
    nouveau_tableau = [0] * (taille+1)
    
    for i in range(taille): nouveau_tableau[i] = T[i]
    nouveau_tableau[len(T)] = lettre
    
    return nouveau_tableau

T1 = ['X', 'F', '+']
lettre = '+'
T2 = ajouter_lettre(T1, lettre)
print(T2)