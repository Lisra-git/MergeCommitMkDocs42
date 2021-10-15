import turtle

fred = turtle.Turtle()
fred.pu()
fred.goto(-200, 40)
fred.pd()
couleur = 1

x_fred = -200
y_fred = 40

for j in range(3):
    for i in range(11):
        if i % 2 == 0: taille = 40
        else: taille = 20
        fred.dot(taille, (couleur, 0, 0))
        fred.pu()
        fred.fd(40)
        fred.pd()
    y_fred = y_fred + 40
    fred.pu()
    fred.goto(-200, y_fred)
    fred.pd()


turtle.exitonclick()
