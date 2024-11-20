import tkinter as tk
import threading
import time
import random

# Creamos un semáforo con un valor máximo de 2 (la impresora puede atender dos procesos a la vez)
semaforo_impresora = threading.Semaphore(2)

# Función para simular el envío del documento desde cada equipo
def enviar_documento(equipo_id, consola, queue):
    paginas = random.randint(1, 10)  # Número aleatorio de páginas (1 a 10)
    queue.put(f"Equipo {equipo_id} tiene un documento de {paginas} páginas.\n")
    
    with semaforo_impresora:
        queue.put(f"Equipo {equipo_id} está enviando el documento a la impresora.\n")
        time.sleep(paginas)  # Simula tiempo de impresión
        queue.put(f"Equipo {equipo_id} ha terminado de imprimir.\n")

# Función principal para manejar la simulación
def iniciar_simulacion(consola, root):
    equipos = 6
    queue = []

    # Limpiar la consola antes de iniciar
    consola.delete(1.0, tk.END)

    def procesar_queue():
        while queue:
            mensaje = queue.pop(0)
            consola.insert(tk.END, mensaje)
            consola.see(tk.END)
        root.after(100, procesar_queue)

    def iniciar_hilos():
        threads = []
        for equipo_id in range(1, equipos + 1):
            t = threading.Thread(target=enviar_documento, args=(equipo_id, consola, queue))
            threads.append(t)
            t.start()

        for t in threads:
            t.join()

    # Inicia los hilos en un subproceso para no bloquear la GUI
    threading.Thread(target=iniciar_hilos, daemon=True).start()
    procesar_queue()

# Interfaz gráfica
def ejecutar():
    root = tk.Tk()
    root.title("Sincronización con Semáforos")
    root.geometry("600x400")

    # Título
    tk.Label(root, text="Sincronización de Impresoras", font=("Helvetica", 16, "bold")).pack(pady=10)

    # Consola para mostrar la salida
    consola = tk.Text(root, wrap="word", font=("Courier", 12), height=15, width=70)
    consola.pack(pady=10)

    # Botón para iniciar la simulación
    tk.Button(
        root, text="Iniciar Simulación", font=("Helvetica", 12, "bold"),
        bg="#3498db", fg="white", command=lambda: iniciar_simulacion(consola, root)
    ).pack(pady=10)

    root.mainloop()
