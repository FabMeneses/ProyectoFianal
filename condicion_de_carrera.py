import tkinter as tk
from tkinter import messagebox
import threading

class CuentaBancaria:
    def __init__(self, saldo_inicial):
        self.saldo = saldo_inicial
        self.bloqueo = threading.Lock()
    
    def depositar(self, monto):
        with self.bloqueo:
            saldo_actual = self.saldo
            saldo_actual += monto
            self.saldo = saldo_actual

def ejecutar():
    # Crear la ventana principal
    root = tk.Tk()
    root.title("Condición de Carrera - Cuenta Bancaria")
    root.geometry("400x350")
    root.resizable(False, False)

    # Crear una instancia de CuentaBancaria
    cuenta = CuentaBancaria(1000)

    # Variables de texto
    texto_saldo = tk.StringVar(value=f"Saldo actual: ${cuenta.saldo}")

    # Función para manejar depósitos
    def hacer_deposito(cuenta, monto, texto_saldo, callback):
        cuenta.depositar(monto)
        texto_saldo.set(f"Saldo actual: ${cuenta.saldo}")
        callback()

    def iniciar_depositos():
        try:
            monto1 = int(entrada_monto1.get())
            monto2 = int(entrada_monto2.get())
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingresa montos válidos.")
            return

        contador = [0]  # Usamos una lista para que sea mutable en los hilos

        def hilo_terminado():
            contador[0] += 1
            if contador[0] == 2:  # Ambos hilos han terminado
                messagebox.showinfo("Finalizado", f"Depósitos completados. Saldo final: ${cuenta.saldo}")

        # Iniciar los hilos sin bloquear la interfaz
        threading.Thread(target=hacer_deposito, args=(cuenta, monto1, texto_saldo, hilo_terminado)).start()
        threading.Thread(target=hacer_deposito, args=(cuenta, monto2, texto_saldo, hilo_terminado)).start()

    # Etiquetas y entradas
    tk.Label(root, text="Condición de Carrera", font=("Helvetica", 16, "bold")).pack(pady=10)
    tk.Label(root, text="La cuenta tiene un saldo inicial de $1000.", font=("Helvetica", 12), fg="black").pack(pady=5)
    tk.Label(root, textvariable=texto_saldo, font=("Helvetica", 14), fg="blue").pack(pady=5)

    tk.Label(root, text="Monto del primer depósito:", font=("Helvetica", 12)).pack(pady=5)
    entrada_monto1 = tk.Entry(root, font=("Helvetica", 12))
    entrada_monto1.pack(pady=5)

    tk.Label(root, text="Monto del segundo depósito:", font=("Helvetica", 12)).pack(pady=5)
    entrada_monto2 = tk.Entry(root, font=("Helvetica", 12))
    entrada_monto2.pack(pady=5)

    # Botón para iniciar los depósitos
    tk.Button(root, text="Hacer Depósitos", font=("Helvetica", 12, "bold"), bg="#3498db", fg="white",
              command=iniciar_depositos).pack(pady=15)

    # Iniciar el loop de la ventana
    root.mainloop()
