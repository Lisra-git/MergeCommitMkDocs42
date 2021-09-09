poids_colis = 4

if poids_colis > 6.2:
    prix_au_kg = 2.2
elif poids_colis <= 1:
    prix_au_kg = 0.55
else:
    prix_au_kg = 1.4

prix = prix_au_kg * poids_colis
print(prix)