mystere = [111, 107, 44, 32, 98, 105, 101, 110, 32, 106, 111, 117, 233]
mot_secret = ""

for nombre in mystere:
    lettre = chr(nombre)
    mot_secret = mot_secret + lettre

print(mot_secret)