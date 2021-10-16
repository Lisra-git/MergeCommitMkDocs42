import turtle
from math import sqrt

fred = turtle.Turtle()

def calculer_hauteur(côté):
    pass

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
    pass

nucléaire(fred, 60)
fred.mainloop()