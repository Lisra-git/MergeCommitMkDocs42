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

def générer_nouveau_tableau(tableau):
    nouveau_tableau = []
    for lettre in tableau:
        if lettre == 'X':
            nouveau_tableau = ajouter_expression(nouveau_tableau, 'F+[[X]-X]-F[-FX]+X')
        elif lettre == 'F':
            nouveau_tableau = ajouter_expression(nouveau_tableau, 'FF')
        else :
            nouveau_tableau = ajouter_expression(nouveau_tableau, lettre)
    return nouveau_tableau


def générer_plante(tableau, finesse):
    for étape in range(finesse):
        tableau = générer_nouveau_tableau(tableau)
    return tableau

tableau = générer_plante(['X'], 2)
print(tableau)