phrase = 'In the castle of '
mot = ''
# aucune raison d'utiliser range : 
for lettre in 'Argh':
    mot = mot + lettre * 5

phrase = phrase + mot
print(phrase)

