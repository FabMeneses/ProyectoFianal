import socket
import threading
import time
import random
from tkinter import Tk, Label, Listbox, Scrollbar, VERTICAL, END
from threading import Semaphore

# Configuración de los nodos
HOST = '127.0.0.1'
PUERTO_ACTOR1 = 5001
PUERTO_ACTOR2 = 5002

# Límite de mensajes
MAX_MENSAJES = 100
contador_mensajes = 0  # Contador global protegido por semáforos
contador_semaforo = Semaphore(1)  # Protege el contador global

# Semáforos para actores
semaforo_actor1 = Semaphore(1)
semaforo_actor2 = Semaphore(1)

# Configuración de la interfaz gráfica
root = Tk()
root.title("Mensajes entre Actores - Formato Terminal")
root.geometry("800x600")
root.config(bg="#002B5C")  # Fondo azul oscuro

# Etiqueta de título
Label(root, text="Log de Mensajes", font=("Arial", 16, "bold"), bg="#FEC524", fg="black").pack(pady=10)

# Listbox para mostrar el log de mensajes
listbox_log = Listbox(root, width=100, height=30, bg="#FFFFFF", fg="#002B5C", font=("Courier", 10))
listbox_log.pack(padx=10, pady=10)

# Scrollbar para el log
scroll_log = Scrollbar(root, orient=VERTICAL, command=listbox_log.yview)
scroll_log.pack(side="right", fill="y")
listbox_log.config(yscrollcommand=scroll_log.set)


# Función para registrar mensajes en la interfaz
def log_mensaje(mensaje):
    listbox_log.insert(END, mensaje)
    listbox_log.yview(END)  # Auto-scroll hacia abajo


# Función para escuchar mensajes
def escuchar_actor(puerto, nombre_actor, semaforo):
    global contador_mensajes
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket_servidor:
        socket_servidor.bind((HOST, puerto))
        socket_servidor.listen()
        log_mensaje(f"{nombre_actor} escuchando en el puerto {puerto}")
        
        while True:
            conn, addr = socket_servidor.accept()
            with conn:
                datos = conn.recv(1024).decode('utf-8')
                if datos:
                    with contador_semaforo:
                        contador_mensajes += 1
                        log_mensaje(f"{nombre_actor} recibió: {datos}")
                        log_mensaje(f"{nombre_actor} está ahora en estado: Ocupado")
                        if contador_mensajes >= MAX_MENSAJES:
                            return  # Termina si se alcanza el límite
                    time.sleep(1)  # Simulación de procesamiento


# Función para enviar mensajes
def enviar_actor(puerto_destino, nombre_actor):
    global contador_mensajes
    while True:
        with contador_semaforo:
            if contador_mensajes >= MAX_MENSAJES:
                return  # Salir si se alcanzó el límite
        
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket_cliente:
            try:
                socket_cliente.connect((HOST, puerto_destino))
                mensaje = f"Hola desde {nombre_actor}"
                socket_cliente.sendall(mensaje.encode('utf-8'))
                log_mensaje(f"{nombre_actor} envió: {mensaje}")
                time.sleep(random.uniform(0.5, 1.5))  # Simulación de periodicidad
            except ConnectionRefusedError:
                log_mensaje(f"{nombre_actor} no pudo conectar al puerto {puerto_destino}")
                time.sleep(1)


# Hilos para los actores
actor1_escuchar = threading.Thread(target=escuchar_actor, args=(PUERTO_ACTOR1, "Actor1", semaforo_actor1))
actor2_escuchar = threading.Thread(target=escuchar_actor, args=(PUERTO_ACTOR2, "Actor2", semaforo_actor2))
actor1_enviar = threading.Thread(target=enviar_actor, args=(PUERTO_ACTOR2, "Actor1"))
actor2_enviar = threading.Thread(target=enviar_actor, args=(PUERTO_ACTOR1, "Actor2"))

# Iniciar los hilos
actor1_escuchar.start()
actor2_escuchar.start()
actor1_enviar.start()
actor2_enviar.start()

# Inicia el bucle principal de Tkinter
root.mainloop()

# Espera a que los hilos terminen
actor1_escuchar.join()
actor2_escuchar.join()
actor1_enviar.join()
actor2_enviar.join()

print("Programa terminado después de 100 mensajes.")

