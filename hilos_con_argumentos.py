
import tkinter as tk

def ejecutar():
    root = tk.Tk()
    root.title("Hilos con argumentos")
    root.geometry("400x300")
    root.configure(bg="#2c3e50")
    
    label = tk.Label(root, text="Ejecutando Hilos con argumentos...", bg="#2c3e50", fg="white", font=("Helvetica", 12, "bold"))
    label.pack(expand=True)
    
    root.mainloop()