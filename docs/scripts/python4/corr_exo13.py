import turtle

fred = turtle.Turtle()

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

triangle(fred, 60, 0, 0)
fred.mainloop()