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


        # EVENTOS DE TECLADO (.bind)


        # Completar tarea con tecla "C"
        self.root.bind("c", self.marcar_completada_evento)

        # Eliminar tarea con tecla "Delete"
        self.root.bind("<Delete>", self.eliminar_tarea_evento)

        # También con "D" (opcional permitido)
        self.root.bind("d", self.eliminar_tarea_evento)

        # Cerrar aplicación con tecla "Escape"
        self.root.bind("<Escape>", self.cerrar_app)

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

        # ===== COLORES =====
        self.tree.tag_configure("pendiente", foreground="red")
        self.tree.tag_configure("completado", foreground="green")

        # Evento de ratón (doble clic)
        self.tree.bind("<Double-1>", self.marcar_completada_evento)

    # ===== FUNCIONES =====

    def agregar_tarea(self):
        descripcion = self.entry.get()

        if descripcion:
            self.servicio.agregar_tarea(descripcion)
            self.entry.delete(0, tk.END)
            self.actualizar_lista()
        else:
            messagebox.showwarning("Error", "Ingrese una tarea")

    def agregar_tarea_evento(self, event):
        self.agregar_tarea()

    def marcar_completada(self):
        seleccion = self.tree.selection()

        if not seleccion:
            messagebox.showwarning("Error", "Seleccione una tarea")
            return

        item = self.tree.item(seleccion)
        id = item["values"][0]

        self.servicio.completar_tarea(id)
        self.actualizar_lista()

    def marcar_completada_evento(self, event):
        self.marcar_completada()

    def eliminar_tarea(self):
        seleccion = self.tree.selection()

        if not seleccion:
            messagebox.showwarning("Error", "Seleccione una tarea")
            return

        item = self.tree.item(seleccion)
        id = item["values"][0]

        self.servicio.eliminar_tarea(id)
        self.actualizar_lista()

    # ===== EVENTOS =====

    def eliminar_tarea_evento(self, event):
        self.eliminar_tarea()

    def cerrar_app(self, event):
        self.root.quit()

    def actualizar_lista(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        for tarea in self.servicio.obtener_tareas():

            estado = "✔ Hecho" if tarea.get_completada() else "Pendiente"

            if tarea.get_completada():
                tag = "completado"
            else:
                tag = "pendiente"

            self.tree.insert(
                "", "end",
                values=(tarea.get_id(), tarea.get_descripcion(), estado),
                tags=(tag,)
            )