import turtle
from math import sqrt

fred = turtle.Turtle()

def calculer_hauteur(côté):
    return sqrt(3) / 2 * côté

def triangle(tortue, côté, x, y):
    tortue.penup()
    tortue.goto(x, y)
    tortue.pendown()
    tortue.fillcolor('green')
    tortue.begin_fill()
    for _ in range(3):
        tortue.fd(côté)
        tortue.lt(120)
    tortue.end_fill()
    return None

def nucléaire(tortue, côté):
    hauteur = calculer_hauteur(côté)
    triangle(tortue, côté, 0, 0)
    triangle(tortue, côté, -côté, 0)
    triangle(tortue, côté, -côté / 2, -hauteur)
    return None

nucléaire(fred, 60)
fred.mainloop()