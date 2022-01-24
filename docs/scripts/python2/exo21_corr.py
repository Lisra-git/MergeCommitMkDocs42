import random
de1 = random.randint(1,6)
de2 = random.randint(1,6)
print(f"La valeur du dé 1 est {de1} et celle du dé 2 est {de2}.")
# Programme à commencer ici #
somme = de1 + de2
if somme >= 10:
    print('Taxe spéciale !', 36)
elif 4 <= somme < 10:
    print('Taxe régulière', somme * 2)
else :
    print('Pas de taxe', 0)