import turtle
import random

x_fred = -200
y_fred = 40

fred = turtle.Turtle()
fred.pu()
fred.goto(x_fred, y_fred)
fred.pd()
couleur = 1

for j in range(3):
    for i in range(11):
        if (i+j) % 2 == 0: taille = 40
        else: taille = 20
        fred.dot(taille, (random.random(), random.random(), random.random()))
        fred.pu()
        fred.fd(40)
        fred.pd()
    y_fred = y_fred - 40
    fred.pu()
    fred.goto(-200, y_fred)
    fred.pd()

turtle.exitonclick()


accumulateur = 0
for nombre in []