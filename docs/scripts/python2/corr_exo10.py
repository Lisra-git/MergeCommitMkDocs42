poids_colis = 4
prix_au_kg = 1.4

if poids_colis > 6.2:
    print("Trop lourd")
else:
    if poids_colis <= 1:
        print("Trop léger")
    else:
        prix = prix_au_kg * poids_colis
        print(prix)