def trouver_pair(tableau):
    for entier in tableau:
        if entier % 2 == 0:
            return True
        else:
            return False

trouvé = trouver_pair([4, 10, 20])
print(trouvé)   