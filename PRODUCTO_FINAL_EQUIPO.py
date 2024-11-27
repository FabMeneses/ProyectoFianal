import tkinter as tk
from tkinter import font
import subprocess
import os
import hilos_hilos
import hilos_con_argumentos
import hilos_con_funcion_tarea
import hilos_sincronizados
import mario_bros_ruleta
import mensajes_cliente_servidor
import tcp_cliente_servidor
import udp_cliente_servidor
import comunicacion_directa
import comunicacion_indirecta
import autenticacion_aguila
import condicion_de_carrera
import sincronizacion_de_semaforos
import semaforos_cliente_servidor
import barbero_dormilon
import sala_de_chat
import futuro_promesa
import productor_consumidor
import actores
import reactor_y_proactor

from tkinter import font, Toplevel
from PIL import Image, ImageTk #pip install PyMuPDF pillow
import fitz  # PyMuPDF

# Ruta específica del archivo PDF
PDF_PATH = r"Documentacion\pdfproyectofinal.pdf"  # Cambia esta ruta a la ubicación de tu PDF

# Función para mostrar documentación en un visor PDF
def mostrar_documentacion():
    ventana_pdf = Toplevel(root)
    ventana_pdf.title("Documentación")
    ventana_pdf.geometry("650x600")

    # Crear marco para Canvas y scrollbars
    frame = tk.Frame(ventana_pdf)
    frame.pack(fill="both", expand=True)

    canvas = tk.Canvas(frame, bg="white")
    scroll_y = tk.Scrollbar(frame, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=scroll_y.set)

    scroll_y.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)

    # Marco interior para colocar imágenes
    inner_frame = tk.Frame(canvas, bg="white")
    canvas.create_window((0, 0), window=inner_frame, anchor="nw")

    def load_pdf():
        # Cargar el documento PDF
        try:
            doc = fitz.open(PDF_PATH)
            images = []

            for page_number in range(len(doc)):
                page = doc.load_page(page_number)
                pix = page.get_pixmap()
                image = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
                photo = ImageTk.PhotoImage(image)
                images.append(photo)

                # Crear un label por página y agregarlo al marco interior
                label = tk.Label(inner_frame, image=photo, bg="white")
                label.image = photo  # Prevenir que Python borre la referencia
                label.pack()

            # Ajustar el scrollregion al contenido
            inner_frame.update_idletasks()
            canvas.configure(scrollregion=canvas.bbox("all"))

        except Exception as e:
            tk.Label(inner_frame, text=f"Error al cargar el PDF:\n{e}", fg="red", bg="white").pack()

    # Cargar el PDF directamente al abrir la ventana
    load_pdf()

# Función para ejecutar el script hilos_hilos.py
def ejecutar_hilos_hilos():
    subprocess.run(["python", "hilos_hilos.py"])

# Diccionario para mapear opciones a funciones
opciones_funciones = {
    "Hilos-Hilos": lambda: ejecutar_hilos_hilos(),
    "Hilos con argumentos": lambda: hilos_con_argumentos.ejecutar() if hasattr(hilos_con_argumentos, 'ejecutar') else print("Función no encontrada"),
    "Hilos con función tarea": lambda: hilos_con_funcion_tarea.ejecutar() if hasattr(hilos_con_funcion_tarea, 'ejecutar') else print("Función no encontrada"),
    "Hilos sincronizados": lambda: hilos_sincronizados.ejecutar() if hasattr(hilos_sincronizados, 'ejecutar') else print("Función no encontrada"),
    "Mario Bros Ruleta": lambda: mario_bros_ruleta.ejecutar() if hasattr(mario_bros_ruleta, 'ejecutar') else print("Función no encontrada"),
    "Mensajes Cliente/Servidor": lambda: mensajes_cliente_servidor.ejecutar() if hasattr(mensajes_cliente_servidor, 'ejecutar') else print("Función no encontrada"),
    "TCP Cliente/Servidor": lambda: tcp_cliente_servidor.ejecutar() if hasattr(tcp_cliente_servidor, 'ejecutar') else print("Función no encontrada"),
    "UDP Cliente/Servidor": lambda: udp_cliente_servidor.ejecutar() if hasattr(udp_cliente_servidor, 'ejecutar') else print("Función no encontrada"),
    "Comunicación directa": lambda: comunicacion_directa.ejecutar() if hasattr(comunicacion_directa, 'ejecutar') else print("Función no encontrada"),
    "Comunicación indirecta": lambda: comunicacion_indirecta.ejecutar() if hasattr(comunicacion_indirecta, 'ejecutar') else print("Función no encontrada"),
    "Autenticación Águila": lambda: autenticacion_aguila.ejecutar() if hasattr(autenticacion_aguila, 'ejecutar') else print("Función no encontrada"),
    "Condición de carrera": lambda: condicion_de_carrera.ejecutar() if hasattr(condicion_de_carrera, 'ejecutar') else print("Función no encontrada"),
    "Sincronización de semáforos": lambda: sincronizacion_de_semaforos.ejecutar() if hasattr(sincronizacion_de_semaforos, 'ejecutar') else print("Función no encontrada"),
    "Semáforos Cliente/Servidor": lambda: semaforos_cliente_servidor.interfaz_semaforos() if hasattr(semaforos_cliente_servidor, 'interfaz_semaforos') else print("Función no encontrada"),
    "Barbero dormilón": lambda: barbero_dormilon.ejecutar() if hasattr(barbero_dormilon, 'ejecutar') else print("Función no encontrada"),
    "SALA DE CHAT (local o con IP)": lambda: sala_de_chat.ejecutar() if hasattr(sala_de_chat, 'ejecutar') else print("Función no encontrada"),
    "Futuro Promesa": lambda: futuro_promesa.ejecutar() if hasattr(futuro_promesa, 'ejecutar') else print("Función no encontrada"),
    "Productor-Consumidor": lambda: productor_consumidor.main() if hasattr(productor_consumidor, 'main') else print("Función no encontrada"),
    "Actores": lambda: actores.ejecutar() if hasattr(actores, 'ejecutar') else print("Función no encontrada"),
    "Reactor y Proactor": lambda: reactor_y_proactor.ejecutar() if hasattr(reactor_y_proactor, 'ejecutar') else print("Función no encontrada")
}

# Función para mostrar el contenido del submenú en la misma ventana
def mostrar_submenu(titulo, opciones):
    # Limpiar el contenido actual de la ventana principal
    for widget in root.winfo_children():
        if widget != menu_bar:
            widget.destroy()

    # Crear un frame para contener los botones del submenú
    submenu_frame = tk.Frame(root, bg="#2c3e50")
    submenu_frame.pack(fill="both", expand=True, padx=10, pady=10)

    # Crear un botón por cada opción del submenú con estilo plano
    for opcion in opciones:
        boton = tk.Button(submenu_frame, text=opcion, command=lambda o=opcion: ejecutar_accion(o),
                          bg="#3498db", fg="white", font=("Helvetica", 12, "bold"), bd=0, padx=10, pady=5)
        boton.pack(side="top", padx=5, pady=5)

# Función para ejecutar el código correspondiente al botón seleccionado
def ejecutar_accion(opcion):
    if opcion in opciones_funciones:
        opciones_funciones[opcion]()

# Función para cerrar la aplicación
def salir():
    root.quit()

# Función para mostrar ayuda en la misma ventana
def mostrar_ayuda():
    mostrar_submenu("Ayuda", ["Nombres de Integrantes:\n- Fabricio Meneses Avila\n- Jorge Ruiz Diaz\n- Josefa Francisco Hernandez\n- Diego Daniel Magdaleno Medina\n- Angel Gabriel Castillo Sanchez"])

# Opciones para cada submenú
hilos_opciones = ["Hilos-Hilos", "Hilos con argumentos", "Hilos con función tarea", "Hilos sincronizados", "Mario Bros Ruleta"]
sockets_opciones = ["Mensajes Cliente/Servidor", "TCP Cliente/Servidor", "UDP Cliente/Servidor", "Comunicación directa", "Comunicación indirecta", "Autenticación Águila"]
semaforos_opciones = ["Condición de carrera", "Sincronización de semáforos", "Semáforos Cliente/Servidor", "Barbero dormilón", "SALA DE CHAT (local o con IP)"]
patrones_opciones = ["Futuro Promesa", "Productor-Consumidor", "Actores", "Reactor y Proactor"]

# Crear la ventana principal
root = tk.Tk()
root.title("Programación Concurrente UPP SFTW_07_03")

root.geometry("800x600")
root.configure(bg="#34495e")  # Fondo en gris oscuro
root.state('zoomed')  # Maximizar la ventana

# Configurar el fondo de la 
background_image = tk.PhotoImage(file="Imagenes/BG.png")
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

# Crear la barra de menú superior
menu_bar = tk.Frame(root, bg="#2c3e50")  # Fondo de la barra en gris oscuro
menu_bar.pack(side="top", fill="x")

# Fuente personalizada para los botones de menú
menu_font = font.Font(family="Helvetica", size=12, weight="bold")

# Crear botones de menú principal que muestran submenús en la misma ventana con estilo moderno
boton_estilo = {"bg": "#3498db", "fg": "white", "font": menu_font, "bd": 0, "padx": 10, "pady": 5}

tk.Button(menu_bar, text="Hilos", command=lambda: mostrar_submenu("Hilos", hilos_opciones), **boton_estilo).pack(side="left", expand=True, fill="both")
tk.Button(menu_bar, text="Sockets", command=lambda: mostrar_submenu("Sockets", sockets_opciones), **boton_estilo).pack(side="left", expand=True, fill="both")
tk.Button(menu_bar, text="Semáforos", command=lambda: mostrar_submenu("Semáforos", semaforos_opciones), **boton_estilo).pack(side="left", expand=True, fill="both")
tk.Button(menu_bar, text="Patrones", command=lambda: mostrar_submenu("Patrones", patrones_opciones), **boton_estilo).pack(side="left", expand=True, fill="both")
tk.Button(menu_bar, text="Documentación", command=mostrar_documentacion, **boton_estilo).pack(side="left", expand=True, fill="both")
tk.Button(menu_bar, text="Ayuda", command=mostrar_ayuda, **boton_estilo).pack(side="left", expand=True, fill="both")
tk.Button(menu_bar, text="Salir", command=salir, **boton_estilo).pack(side="left", expand=True, fill="both")

# Ejecutar la aplicación
root.mainloop()
