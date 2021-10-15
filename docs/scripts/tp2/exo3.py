import turtle

x_fred = -200
y_fred = 40

fred = turtle.Turtle()
fred.pu()
fred.goto(x_fred, y_fred)
fred.pd()
couleur = 1

for i in range(11):
    if i % 2 == 0: taille = 40
    else: taille = 20
    fred.dot(taille, (couleur, 0, 0))
    fred.pu()
    fred.fd(40)
    fred.pd()

fred.speed(10)
turtle.exitonclick()
