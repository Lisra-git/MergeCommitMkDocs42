import tkinter as tk

largeur, hauteur = 390, 390

fenetre = tk.Tk()
fenetre.title('Une fenêtre !')

lab = tk.Label(fenetre, text='')
lab.grid(row = 0, column = 0, padx=3, pady=3, columnspan = 2)

btn1 = tk.Button(fenetre, text= 'Quit', command = fenetre.quit)
btn1.grid(row = 2, column = 1, padx=3, pady=3, sticky = tk.E + tk.W)

btn2 = tk.Button(fenetre, text= 'Play again')#, command = clear)
btn2.grid(row = 2, column = 0, padx=3, pady=3, sticky = tk.E + tk.W)

canvas = tk.Canvas(fenetre, width= largeur, height = hauteur, background = 'black')
canvas.grid(row = 1, column = 0, padx=3, pady=3, columnspan = 2)

def tracer_croix(x_clic : int, y_clic : int) -> None:
    canvas.create_line(x_clic, y_clic, x_clic + 130, y_clic + 130, width=5, fill='blue')
    canvas.create_line(x_clic, y_clic + 130, x_clic + 130, y_clic, width=5, fill='blue')

def tracer_cercle(x_clic : int, y_clic : int) -> None:
    canvas.create_oval(x_clic, y_clic, x_clic + 130, y_clic + 130, width=5, outline='white')

tracer_croix(0, 0)
tracer_cercle(0, 0)

fenetre.mainloop()