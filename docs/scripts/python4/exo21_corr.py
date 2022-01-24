import turtle

def dessiner_polygone(tortue, n_côté, L):
    angle = 360 // n_côté
    for _ in range(n_côté):
        # attention ! On parle de la tortue en général, pas seulement de fred.
        tortue.fd(L)
        tortue.right(angle)
    return None

fred = turtle.Turtle()
dessiner_polygone(fred, 6, 40)
dessiner_polygone(fred, 10, 40)
dessiner_polygone(fred, 12, 40)
fred.mainloop()