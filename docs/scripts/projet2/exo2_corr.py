def ajouter_lettre(T, lettre):
    taille = len(T)
    nouveau_tableau = [0] * (taille+1)
    
    for i in range(taille): nouveau_tableau[i] = T[i]
    nouveau_tableau[len(T)] = lettre
    
    return nouveau_tableau

def ajouter_expression(tableau, expression):
    for lettre in expression :
        tableau = ajouter_lettre(tableau, lettre)
    return tableau

T1 = ['X', 'F', '+']
expression = 'ABC'
T2 = ajouter_expression(T1, expression)
print(T2)