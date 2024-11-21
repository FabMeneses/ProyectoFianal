import concurrent.futures
import time
import tkinter as tk
from tkinter import ttk

# Función que simula una operación costosa
def tarea_pesada():
    time.sleep(3)  # Simula un trabajo pesado de 3 segundos
    return "¡Tarea completada!"

# Función para manejar la operación en segundo plano
def ejecutar_tarea():
    progreso.set("Procesando...")
    boton_ejecutar.config(state=tk.DISABLED)

    # Usar ThreadPoolExecutor para manejar la concurrencia
    with concurrent.futures.ThreadPoolExecutor() as ejecutor:
        futuro = ejecutor.submit(tarea_pesada)
        root.after(100, verificar_resultado, futuro)

# Función para verificar el resultado de la tarea
def verificar_resultado(futuro):
    if futuro.done():
        resultado = futuro.result()
        progreso.set(resultado)
        boton_ejecutar.config(state=tk.NORMAL)
    else:
        root.after(100, verificar_resultado, futuro)

# Configuración de la ventana principal
root = tk.Tk()
root.title("Concurrencia con Tkinter")
root.geometry("400x200")
root.config(bg="#002B7F")  # Azul profundo del equipo

# Variables y elementos de la interfaz
progreso = tk.StringVar(value="Presiona el botón para comenzar")

# Etiqueta para mostrar el estado
etiqueta = ttk.Label(
    root,
    textvariable=progreso,
    background="#002B7F",  # Azul profundo
    foreground="#FFD700",  # Amarillo dorado
    font=("Helvetica", 14, "bold")
)
etiqueta.pack(pady=30)

# Estilo para el botón
style = ttk.Style()
style.configure(
    "TButton",
    font=("Helvetica", 12, "bold"),
    foreground="#002B7F",  # Azul profundo
    background="#FFD700",  # Amarillo
    padding=10
)
style.map(
    "TButton",
    background=[("active", "#002B7F")],
    foreground=[("active", "#FFD700")]
)

# Botón para ejecutar la tarea
boton_ejecutar = ttk.Button(root, text="Ejecutar tarea", style="TButton", command=ejecutar_tarea)
boton_ejecutar.pack(pady=20)

# Pie de página decorativo
pie_de_pagina = tk.Label(
    root,
    text="¡Arriba los Tigres!",
    bg="#FFD700",  # Amarillo
    fg="#002B7F",  # Azul profundo
    font=("Helvetica", 10, "bold")
)
pie_de_pagina.pack(side="bottom", fill="x")

# Iniciar el bucle principal
root.mainloop()
