def valider_email(email):
    # on suppose que le caractère @ est absent.
    trouvé = False
    for lettre in email:
        if lettre == "@":
            trouvé = True
    return trouvé


