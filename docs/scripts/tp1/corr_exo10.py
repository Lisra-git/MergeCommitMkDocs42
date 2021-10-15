import turtle

longueur = 100
nombre_côté = 10
angle = 360 / nombre_côté
nombre_max_traits = 30
largeur = 8
couleur_rouge = 1

fred = turtle.Turtle()
fred.penup() # utile pour le site web.
fred.goto(350,200) # utile pour le site web.
fred.pendown() # utile pour le site web.
fred.width(largeur)
fred.color(couleur_rouge, 0, 0)

n = 0
while n < nombre_max_traits:
    if longueur >= 0:
        fred.fd(longueur)
        fred.right(angle)
        # modifier le décrément et observer le résultat
        print(longueur)
        longueur = longueur - 5
    if n % 5 == 0: 
        largeur = largeur * 0.75
        fred.width(largeur)
    n = n + 1
    couleur_rouge = couleur_rouge * 0.95
    fred.color(couleur_rouge, 0, 0)

fred.mainloop()
