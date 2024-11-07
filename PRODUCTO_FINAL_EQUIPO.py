import tkinter as tk
from tkinter import Menu

def on_button_click():
    print("Botón presionado")

root = tk.Tk()
root.title("Ventana con Barra de Menú")

# Configurar el fondo de la ventana
background_image = tk.PhotoImage(file="imagenes/BG.png")
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

menu_bar = tk.Frame(root, bg="lightgrey")
menu_bar.pack(side="top", fill="x")

# Lista de nombres para los botones
button_names = ["Hilos", "Sockets", "Semaforos", "Patrones", "Ayuda", "Salir"]

for name in button_names:
    button = tk.Button(menu_bar, text=name, command=on_button_click)
    button.pack(side="left", expand=True, fill="both")

# Configurar el tamaño de la ventana
root.geometry("600x500")

root.mainloop()