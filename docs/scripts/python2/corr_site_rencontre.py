genre, age = "femme", 21

inscription_non_autorisée = False
if age > 18 and genre == "homme":
    inscription_payante = True
elif age > 18 and genre == "femme":
    inscription_payante = False
else:
    inscription_non_autorisée = True

print(f"Interdit : {inscription_non_autorisée}")
if not inscription_non_autorisée:
    print(f"Payant : {inscription_payante}")