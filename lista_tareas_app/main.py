import tkinter as tk
from servicios.tarea_servicio import TareaServicio
from ui.app_tkinter import AppTkinter

# Punto de entrada del programa
if __name__ == "__main__":
    root = tk.Tk()

    # Se crea el servicio (lógica)
    servicio = TareaServicio()

    # Se inicia la interfaz
    app = AppTkinter(root, servicio)

    # Bucle principal
    root.mainloop()