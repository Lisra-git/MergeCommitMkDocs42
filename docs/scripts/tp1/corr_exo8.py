import turtle

longueur = 100
nombre_côté = 10
angle = 360 / nombre_côté
nombre_max_traits = 30

fred = turtle.Turtle()
fred.penup() # utile pour le site web.
fred.goto(350,200) # utile pour le site web.
fred.pendown() # utile pour le site web.

n = 0
while n < nombre_max_traits:
    if longueur >= 0:
        fred.fd(longueur)
        fred.right(angle)
        # modifier le décrément et observer le résultat
        print(longueur)
        longueur = longueur - 5
    n = n + 1

fred.mainloop()
