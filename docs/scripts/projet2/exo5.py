import turtle 


def dessiner_plante(tableau, longueur):

    position_en_mémoire = []
    direction_en_mémoire = []

    pass


# turtle.tracer(0) # tracé instantané
turtle.ht()
turtle.pu()
turtle.screensize(1000,2000)
turtle.setpos(-300,-300) # place la tortue
turtle.seth(45) # définit la direction de la tortue
turtle.pd()

dessiner_plante(['X'], 10)

turtle.update()
turtle.exitonclick()
