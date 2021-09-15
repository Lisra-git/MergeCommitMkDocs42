genre, age = "femme", 21

inscription_non_autorisée = False
if genre == "homme":
    if age > 18:
        inscription_payante = True
    else:
        inscription_non_autorisée = True
else:
    if age > 18:            
        inscription_payante = False
    else:
        inscription_non_autorisée = True

print(f"Interdit : {inscription_non_autorisée}")
if not inscription_non_autorisée:
    print(f"Payant : {inscription_payante}")