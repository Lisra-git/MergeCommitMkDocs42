import turtle

def dessiner_polygone(tortue, n_côté, L):
    n_côté = 10
    angle = 360 // n_côté
    for _ in range(n_côté):
        fred.fd(50)
        fred.right(angle)
    return None

fred = turtle.Turtle()
dessiner_polygone(fred, 6, 40)

fred.mainloop()