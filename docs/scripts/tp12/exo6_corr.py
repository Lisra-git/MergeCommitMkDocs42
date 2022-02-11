import tkinter as tk

TOUR = 1
COTE_CARRE = 130

def tracer_croix(x_clic : int, y_clic : int) -> None:
    canvas.create_line(x_clic, y_clic, x_clic + COTE_CARRE, y_clic + COTE_CARRE, width = 5, fill = 'blue')
    canvas.create_line(x_clic, y_clic + COTE_CARRE, x_clic + COTE_CARRE, y_clic, width = 5, fill = 'blue')

def tracer_cercle(x_clic : int, y_clic : int) -> None:
    canvas.create_oval(x_clic, y_clic, x_clic + COTE_CARRE, y_clic + COTE_CARRE, width = 5, outline = 'red')

def tracer_damier():
    for i in [0, COTE_CARRE, 2*COTE_CARRE]:
        for j in [0, COTE_CARRE, 2*COTE_CARRE]:
            canvas.create_rectangle(i, j, i + COTE_CARRE, j + COTE_CARRE, width = 2, fill = 'white')

def calculer_coordonnees(x, y):
    return (x // COTE_CARRE) * COTE_CARRE, (y // COTE_CARRE) * COTE_CARRE

def jouer(event):
    global TOUR
    x, y = calculer_coordonnees(event.x, event.y)
    if TOUR % 2:
        tracer_croix(x, y)
        TOUR += 1
    else : 
        tracer_cercle(x, y)
        TOUR += 1


largeur, hauteur = 3 * COTE_CARRE, 3 * COTE_CARRE

fenetre = tk.Tk()
fenetre.title('Morpion !')

lab = tk.Label(fenetre, text = '')
lab.grid(row = 0, column = 0, padx = 3, pady = 3, columnspan = 2)

btn1 = tk.Button(fenetre, text= 'Quit', command = fenetre.quit)
btn1.grid(row = 2, column = 1, padx = 3, pady = 3, sticky = tk.E + tk.W)

btn2 = tk.Button(fenetre, text= 'Play again')#, command = clear)
btn2.grid(row = 2, column = 0, padx = 3, pady = 3, sticky = tk.E + tk.W)

canvas = tk.Canvas(fenetre, width= largeur, height = hauteur, background = 'black')
canvas.grid(row = 1, column = 0, padx = 3, pady = 3, columnspan = 2)
tracer_damier()


canvas.bind('<Button-1>', jouer)

fenetre.mainloop()