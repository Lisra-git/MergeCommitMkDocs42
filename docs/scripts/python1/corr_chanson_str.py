sujet1 = "She's " # On peut mettre un guillemet ' dans des ""
sujet2 = "I'm "
nom = " Cool \n"
titre = "Daddy"
phrase1 = "crazy like a fool \n"  # \n force un retour à la ligne
phrase2 = "What about it "
phrase3 = phrase2 + titre + nom # "What about it" + "Daddy" + "Cool"

refrain = sujet1 + phrase1 + phrase3 + sujet2 + phrase1 + phrase3
# on prend le refrain d'avant, on saute une ligne et répète 4 fois "Daddy, Daddy Cool"
# on répète deux fois le même bloc "She's crazy...." et "Daddy, Daddy Cool"
chanson = (refrain + "\n" + (titre + ", " + titre + nom) * 4 + "\n") * 2
print(chanson)