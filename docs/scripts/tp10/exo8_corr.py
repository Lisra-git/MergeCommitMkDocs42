def concaténer(T1, T2):
    taille1 = len(T1)
    taille2 = len(T2)
    
    nouveau_tableau = [0] * (taille1 + taille2)
    
    for i in range(taille1):
        nouveau_tableau[i] = T1[i]
    for i in range(taille2):
        # On ne veut pas réécrire sur les indices 0, 1 ,2...
        nouveau_tableau[i + taille1] = T2[i]
        
    return nouveau_tableau

tableau1 = [3, 4, 5]
tableau2 = [6, 7]
tableau_complet = concaténer(tableau1, tableau2)
print(tableau_complet)