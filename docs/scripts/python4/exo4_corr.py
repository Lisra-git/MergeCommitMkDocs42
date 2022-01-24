import random
import turtle

def placer_aléatoirement():
    x = random.randint(0, 700)
    y = random.randint(0, 400)
    return x, y

def choisir_couleur():
    n = random.randint(0,3)
    if n == 0 : couleur = 'red'
    if n == 1 : couleur = 'green'
    if n == 2 : couleur = 'blue'
    if n == 3 : couleur = 'purple'
    return couleur

def créer_tache():
    taille = random.randint(1, 50)
    x, y = placer_aléatoirement()
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.dot(taille, choisir_couleur())
    return None

for _ in range(10):
    créer_tache()