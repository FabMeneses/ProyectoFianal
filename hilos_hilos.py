import threading
import tkinter as tk

# Función que se ejecutará en el hilo
def Primer_Hilo():
    label.config(text="Mi Primer Programa con Hilos en Python")

if __name__ == '__main__':
    # Crear la ventana principal de tkinter
    root = tk.Tk()
    root.title("Programa con Hilos")
    
    # Crear y empaquetar una etiqueta en la ventana
    label = tk.Label(root, text="")
    label.pack(pady=20)
    
    # Crear y empezar el hilo
    thread = threading.Thread(target=Primer_Hilo)
    thread.start()
    
    # Iniciar el bucle principal de tkinter
    root.mainloop()
