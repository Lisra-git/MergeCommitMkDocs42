import turtle

longueur = 30
nombre_côté = 13
angle = 360 / nombre_côté

fred = turtle.Turtle()
fred.penup() # utile pour le site web.
fred.goto(350,200) # utile pour le site web.
fred.pendown() # utile pour le site web.

n = 0
while n < 8:
    fred.fd(longueur)
    fred.right(45)
    n = n + 1

fred.mainloop()
