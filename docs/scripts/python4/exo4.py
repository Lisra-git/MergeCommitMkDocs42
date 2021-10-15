import random
import turtle

x = random.randint(0, 700)

def placer_aléatoirement():
    pass

def choisir_couleur():
    n = random.randint(0,3)
    pass

def créer_tache():
    taille = random.randint(1, 50)
    x, y = placer_aléatoirement()
    couleur = choisir_couleur()
    if couleur is not None:
        turtle.hideturtle()
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.dot(taille, couleur)
    return None

