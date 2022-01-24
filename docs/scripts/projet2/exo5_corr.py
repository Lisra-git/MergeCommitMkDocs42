import turtle 


def dessiner_plante(tableau, longueur):

    position_en_mémoire = []
    direction_en_mémoire = []

    for lettre in tableau:
        if(lettre == '-'): turtle.left(25)
        elif(lettre == '+'): turtle.right(25)
        elif(lettre == 'F') : turtle.forward(longueur)
        elif(lettre == '[') : 
            position_en_mémoire.append(turtle.pos())
            direction_en_mémoire.append(turtle.heading())
        elif(lettre == ']') :
            ancienne_position = position_en_mémoire.pop(-1)
            ancienne_direction = direction_en_mémoire.pop(-1)
            turtle.penup()
            turtle.seth(ancienne_direction)
            turtle.setpos(ancienne_position)
            turtle.pendown()
    return None


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
