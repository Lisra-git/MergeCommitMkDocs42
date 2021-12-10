import turtle

def ajouter_lettre(tableau, lettre):
    taille = len(tableau)

    nouveau_tableau = [0] * (taille + 1)
    for i in range(taille):
        nouveau_tableau[i] = tableau[i]

    nouveau_tableau[taille] = lettre
    return nouveau_tableau

def ajouter_expression(tableau, expression):
    for lettre in expression :
        tableau = ajouter_lettre(tableau, lettre)
    return tableau

def générer_nouveau_tableau(tableau):
    nouveau_tableau = []
    for lettre in tableau:
        if lettre == 'X':
            nouveau_tableau = ajouter_expression(nouveau_tableau, 'F+[[X]-X]-F[-FX]+X')
        elif lettre == 'F':
            nouveau_tableau = ajouter_expression(nouveau_tableau, 'FF')
        else :
            nouveau_tableau = ajouter_expression(nouveau_tableau, lettre)
    return nouveau_tableau

def générer_plante(tableau, n_finesse):
    for degré_finesse in range(n_finesse):
        tableau = générer_nouveau_tableau(tableau)
    return tableau

tableau = générer_plante(['X'], 6)
print(tableau)


longueur = 3

turtle.tracer(0)
turtle.ht()
pile_actions = []
turtle.pu()
turtle.screensize(1000,2000)
turtle.setpos(-300,-300)
turtle.seth(45)
turtle.pd()

k=0
for action in tableau:
    if(action == '-'): turtle.left(25)
    elif(action == '+'): turtle.right(25)
    elif(action == 'F') : turtle.forward(longueur)
    elif(action == '[') : pile_actions.append([turtle.pos(), turtle.heading()])
    elif(action == ']') :
        ancienne_position, ancien_angle = pile_actions.pop(-1)
        turtle.penup()
        turtle.seth(ancien_angle)
        turtle.setpos(ancienne_position)
        turtle.pendown()
    
turtle.update()
turtle.exitonclick()
