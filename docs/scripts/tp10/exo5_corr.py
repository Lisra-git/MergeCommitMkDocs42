import turtle

def spiraler(T):
    for longueur in T:
        turtle.forward(longueur)
        turtle.right(90)
    return None

T = [i*5 for i in range(40)]
spiraler(T)