import tkinter as tk
from tkinter import ttk, messagebox

# Clase de la interfaz gráfica
class AppTkinter:
    def __init__(self, root, servicio):
        self.root = root
        self.servicio = servicio

        self.root.title("Lista de Tareas")

        # ===== CAMPO DE TEXTO =====
        self.entry = tk.Entry(root, width=40)
        self.entry.pack(pady=10)

        # Evento de teclado (ENTER)
        self.entry.bind("<Return>", self.agregar_tarea_evento)

        # ===== BOTONES =====
        frame_botones = tk.Frame(root)
        frame_botones.pack()

        tk.Button(frame_botones, text="Añadir Tarea", command=self.agregar_tarea)\
            .grid(row=0, column=0, padx=5)

        tk.Button(frame_botones, text="Marcar Completada", command=self.marcar_completada)\
            .grid(row=0, column=1, padx=5)

        tk.Button(frame_botones, text="Eliminar", command=self.eliminar_tarea)\
            .grid(row=0, column=2, padx=5)

        # ===== TABLA (TREEVIEW) =====
        self.tree = ttk.Treeview(root, columns=("ID", "Descripción", "Estado"), show="headings")

        self.tree.heading("ID", text="ID")
        self.tree.heading("Descripción", text="Descripción")
        self.tree.heading("Estado", text="Estado")

        self.tree.pack(pady=10)

        # ===== CONFIGURACIÓN DE COLORES =====
        # Se configuran UNA SOLA VEZ los estilos para las tareas
        # Rojo → tareas pendientes
        # Verde → tareas completadas
        self.tree.tag_configure("pendiente", foreground="red")
        self.tree.tag_configure("completado", foreground="green")

        # Evento de ratón (doble clic)
        self.tree.bind("<Double-1>", self.marcar_completada_evento)

    # ===== FUNCIONES =====

    def agregar_tarea(self):
        """
        Agrega una nueva tarea desde el campo de texto
        """
        descripcion = self.entry.get()

        if descripcion:
            self.servicio.agregar_tarea(descripcion)
            self.entry.delete(0, tk.END)
            self.actualizar_lista()
        else:
            messagebox.showwarning("Error", "Ingrese una tarea")

    def agregar_tarea_evento(self, event):
        """Evento al presionar ENTER"""
        self.agregar_tarea()

    def marcar_completada(self):
        """
        Marca la tarea seleccionada como completada
        """
        seleccion = self.tree.selection()

        if not seleccion:
            messagebox.showwarning("Error", "Seleccione una tarea")
            return

        item = self.tree.item(seleccion)
        id = item["values"][0]

        self.servicio.completar_tarea(id)
        self.actualizar_lista()

    def marcar_completada_evento(self, event):
        """Evento doble clic"""
        self.marcar_completada()

    def eliminar_tarea(self):
        """
        Elimina la tarea seleccionada
        """
        seleccion = self.tree.selection()

        if not seleccion:
            messagebox.showwarning("Error", "Seleccione una tarea")
            return

        item = self.tree.item(seleccion)
        id = item["values"][0]

        self.servicio.eliminar_tarea(id)
        self.actualizar_lista()

    def actualizar_lista(self):
        """
        Actualiza la tabla con las tareas actuales
        """
        # ===== LIMPIAR TABLA =====
        for item in self.tree.get_children():
            self.tree.delete(item)

        # ===== INSERTAR TAREAS =====
        for tarea in self.servicio.obtener_tareas():

            # Determinar texto del estado
            estado = "✔ Hecho" if tarea.get_completada() else "Pendiente"

            # Determinar color mediante tags
            # Verde si está completada, rojo si está pendiente
            if tarea.get_completada():
                tag = "completado"
            else:
                tag = "pendiente"

            # Insertar en la tabla con el color correspondiente
            self.tree.insert(
                "", "end",
                values=(tarea.get_id(), tarea.get_descripcion(), estado),
                tags=(tag,)  # Aquí se aplica el color
            )