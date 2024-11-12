import tkinter as tk
from tkinter import font

# Función para abrir un submenú en una nueva ventana con botones específicos
def abrir_submenu(titulo, opciones):
    submenu = tk.Toplevel(root)
    submenu.title(titulo)
    submenu.geometry("400x300")
    submenu.configure(bg="#2c3e50")  # Fondo de submenú en gris oscuro
    
    # Crear un frame para contener los botones del submenú
    submenu_frame = tk.Frame(submenu, bg="#2c3e50")
    submenu_frame.pack(fill="both", expand=True, padx=10, pady=10)

    # Crear un botón por cada opción del submenú con estilo plano
    for opcion in opciones:
        boton = tk.Button(submenu_frame, text=opcion, command=lambda o=opcion: ejecutar_accion(o),
                          bg="#3498db", fg="white", font=("Helvetica", 12, "bold"), bd=0, padx=10, pady=5)
        boton.pack(side="top", expand=True, fill="x", padx=5, pady=5)

# Función para ejecutar el código correspondiente al botón seleccionado
def ejecutar_accion(opcion):
    print(f"Ejecutando {opcion}...")
    # Aquí colocarías el código correspondiente para cada opción
    # Por ejemplo, si la opción es "Hilos-Hilos":
    if opcion == "Hilos-Hilos":
        print("Ejecutando Hilos-Hilos...")
        # Código de "Hilos-Hilos"
    
    elif opcion == "Hilos con argumentos":
        print("Ejecutando Hilos con argumentos...")
        # Código de "Hilos con argumentos"
    
    elif opcion == "Hilos con función tarea":
        print("Ejecutando Hilos con función tarea...")
        # Código de "Hilos con función tarea"
    
    elif opcion == "Hilos sincronizados":
        print("Ejecutando Hilos sincronizados...")
        # Código de "Hilos sincronizados"
    
    elif opcion == "Mario Bros Ruleta":
        print("Ejecutando Mario Bros Ruleta...")
        # Código de "Mario Bros Ruleta"
    
    elif opcion == "Mensajes Cliente/Servidor":
        print("Ejecutando Mensajes Cliente/Servidor...")
        # Código de "Mensajes Cliente/Servidor"
    
    elif opcion == "TCP Cliente/Servidor":
        print("Ejecutando TCP Cliente/Servidor...")
        # Código de "TCP Cliente/Servidor"
    
    elif opcion == "UDP Cliente/Servidor":
        print("Ejecutando UDP Cliente/Servidor...")
        # Código de "UDP Cliente/Servidor"
    
    elif opcion == "Comunicación directa":
        print("Ejecutando Comunicación directa...")
        # Código de "Comunicación directa"
    
    elif opcion == "Comunicación indirecta":
        print("Ejecutando Comunicación indirecta...")
        # Código de "Comunicación indirecta"
    
    elif opcion == "Autenticación Águila":
        print("Ejecutando Autenticación Águila...")
        # Código de "Autenticación Águila"
    
    elif opcion == "Condición de carrera":
        print("Ejecutando Condición de carrera...")
        # Código de "Condición de carrera"
    
    elif opcion == "Sincronización de semáforos":
        print("Ejecutando Sincronización de semáforos...")
        # Código de "Sincronización de semáforos"
    
    elif opcion == "Semáforos Cliente/Servidor":
        print("Ejecutando Semáforos Cliente/Servidor...")
        # Código de "Semáforos Cliente/Servidor"
    
    elif opcion == "Barbero dormilón":
        print("Ejecutando Barbero dormilón...")
        # Código de "Barbero dormilón"
    
    elif opcion == "SALA DE CHAT (local o con IP)":
        print("Ejecutando SALA DE CHAT...")
        # Código de "SALA DE CHAT"
    
    elif opcion == "Futuro Promesa":
        print("Ejecutando Futuro Promesa...")
        # Código de "Futuro Promesa"
    
    elif opcion == "Productor-Consumidor":
        print("Ejecutando Productor-Consumidor...")
        # Código de "Productor-Consumidor"
    
    elif opcion == "Actores":
        print("Ejecutando Actores...")
        # Código de "Actores"
    
    elif opcion == "Reactor y Proactor":
        print("Ejecutando Reactor y Proactor...")
        # Código de "Reactor y Proactor"

# Función para cerrar la aplicación
def salir():
    root.quit()

# Función para mostrar ayuda
def mostrar_ayuda():
    abrir_submenu("Ayuda", ["Nombres de Integrantes:\n- Fabricio Meneses Avila\n- Jorge Ruiz Diaz\n- Josefa Francisco Hernandez\n- Diego Daniel Magdaleno Medina\n- GaboGabriel"])

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

# Crear la barra de menú superior
menu_bar = tk.Frame(root, bg="#2c3e50")  # Fondo de la barra en gris oscuro
menu_bar.pack(side="top", fill="x")
# Configurar el fondo de la ventana
#background_image = tk.PhotoImage(file="imagenes/BG.png")
#background_label = tk.Label(root, image=background_image)
#background_label.place(relwidth=1, relheight=1)
# Fuente personalizada para los botones de menú
menu_font = font.Font(family="Helvetica", size=12, weight="bold")

# Crear botones de menú principal que abren submenús con estilo moderno
boton_estilo = {"bg": "#3498db", "fg": "white", "font": menu_font, "bd": 0, "padx": 10, "pady": 5}

tk.Button(menu_bar, text="Hilos", command=lambda: abrir_submenu("Hilos", hilos_opciones), **boton_estilo).pack(side="left", expand=True, fill="both")
tk.Button(menu_bar, text="Sockets", command=lambda: abrir_submenu("Sockets", sockets_opciones), **boton_estilo).pack(side="left", expand=True, fill="both")
tk.Button(menu_bar, text="Semáforos", command=lambda: abrir_submenu("Semáforos", semaforos_opciones), **boton_estilo).pack(side="left", expand=True, fill="both")
tk.Button(menu_bar, text="Patrones", command=lambda: abrir_submenu("Patrones", patrones_opciones), **boton_estilo).pack(side="left", expand=True, fill="both")
tk.Button(menu_bar, text="Ayuda", command=mostrar_ayuda, **boton_estilo).pack(side="left", expand=True, fill="both")
tk.Button(menu_bar, text="Salir", command=salir, **boton_estilo).pack(side="left", expand=True, fill="both")

# Ejecutar la aplicación
root.mainloop()