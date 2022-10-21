import csv

def import_CSV(fichier: str, separateur = ";" ):
    flux = open(fichier, 'r')  # ouverture de fichier en lecture
    table_CSV = csv.DictReader(flux, delimiter = separateur) # utilise la librairie csv
    tableau = [] # création d'une liste vide
    for ligne in table_CSV:  # parcourt de la chose renvoyée par DictReader
        tableau.append(dict(ligne)) # ajout de la ligne formattée dans tableau
    flux.close()
    return tableau

def export_CSV(données : list, fichier : str):
    header = données[0].keys()
    # DictWriter va être un "dictionnaire" que l'on va écrire
    # header = en-têtes du fichier CSV (nom de colonnes)
    fichier_CSV = csv.DictWriter(open(fichier, 'w'), fieldnames = header)
    # écrit dans le fichier texte les en-têtes
    fichier_CSV.writeheader()
    # écriture des données ligne par ligne
    for ligne in données:
        fichier_CSV.writerow(ligne)
    return None

for ligne in import_CSV('exemple.csv'):
    print(ligne)