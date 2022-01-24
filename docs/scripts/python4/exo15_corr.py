def trouver_pair(tableau):
    for entier in tableau:
        if entier % 2 == 0:
            return True
    return False
