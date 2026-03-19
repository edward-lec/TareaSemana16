import tkinter as tk
from tkinter import ttk, messagebox

# Clase de la interfaz gráfica (Capa UI)
class AppTkinter:
    def __init__(self, servicio):
        """
        Constructor de la interfaz gráfica.

        Parámetro:
        servicio -> objeto de la capa de servicios (inyección de dependencias)

        Aquí SOLO se maneja la interfaz, no la lógica del sistema.
        """
        # Guardamos el servicio para usarlo en los métodos
        self.servicio = servicio

        # ===== VENTANA PRINCIPAL =====
        self.root = tk.Tk()
        self.root.title("Sistema de Registro de Visitantes")
        self.root.geometry("650x400")

        # ===== FORMULARIO DE ENTRADA =====

        # Etiqueta y campo para la cédula
        tk.Label(self.root, text="Cédula").grid(row=0, column=0, padx=5, pady=5)
        self.entry_cedula = tk.Entry(self.root)
        self.entry_cedula.grid(row=0, column=1)

        # Etiqueta y campo para el nombre
        tk.Label(self.root, text="Nombre").grid(row=1, column=0, padx=5, pady=5)
        self.entry_nombre = tk.Entry(self.root)
        self.entry_nombre.grid(row=1, column=1)

        # Etiqueta y campo para el motivo
        tk.Label(self.root, text="Motivo").grid(row=2, column=0, padx=5, pady=5)
        self.entry_motivo = tk.Entry(self.root)
        self.entry_motivo.grid(row=2, column=1)

        # ===== PANEL DE BOTONES =====

        # Botón para registrar un visitante (Create)
        tk.Button(self.root, text="Registrar", command=self.registrar)\
            .grid(row=3, column=0, pady=10)

        # Botón para eliminar un visitante (Delete)
        tk.Button(self.root, text="Eliminar", command=self.eliminar)\
            .grid(row=3, column=1)

        # Botón para limpiar los campos del formulario
        tk.Button(self.root, text="Limpiar", command=self.limpiar_campos)\
            .grid(row=3, column=2)

        # Botón para actualizar un visitante (Update)
        tk.Button(self.root, text="Actualizar", command=self.actualizar)\
            .grid(row=3, column=3)

        # ===== TABLA DE VISUALIZACIÓN (Treeview) =====

        # Creamos la tabla con tres columnas
        self.tabla = ttk.Treeview(
            self.root,
            columns=("Cedula", "Nombre", "Motivo"),
            show="headings"  # Oculta la columna vacía inicial
        )

        # Definimos los encabezados de la tabla
        self.tabla.heading("Cedula", text="Cédula")
        self.tabla.heading("Nombre", text="Nombre")
        self.tabla.heading("Motivo", text="Motivo")

        # Ubicamos la tabla en la ventana
        self.tabla.grid(row=4, column=0, columnspan=4, padx=10, pady=10)

        # Evento: cuando el usuario selecciona una fila de la tabla
        self.tabla.bind("<<TreeviewSelect>>", self.seleccionar_registro)

    def run(self):
        """
        Método que inicia la ejecución de la aplicación.
        Se llama desde main.py (buena práctica de arquitectura).
        """
        self.root.mainloop()

    def registrar(self):
        """
        Método para registrar un nuevo visitante (Create).
        Obtiene los datos del formulario y usa el servicio.
        """

        # Obtener datos del formulario
        cedula = self.entry_cedula.get()
        nombre = self.entry_nombre.get()
        motivo = self.entry_motivo.get()

        # Validar que no existan campos vacíos
        if not cedula or not nombre or not motivo:
            messagebox.showwarning("Error", "Todos los campos son obligatorios")
            return

        # Llamar al servicio para registrar
        if self.servicio.registrar_visitante(cedula, nombre, motivo):
            messagebox.showinfo("Éxito", "Visitante registrado")

            # Actualizar tabla y limpiar formulario
            self.actualizar_tabla()
            self.limpiar_campos()
        else:
            messagebox.showerror("Error", "La cédula ya existe")

    def eliminar(self):
        """
        Método para eliminar un visitante seleccionado (Delete).
        """

        # Obtener selección de la tabla
        seleccion = self.tabla.selection()

        # Validar que haya selección
        if not seleccion:
            messagebox.showwarning("Error", "Seleccione un registro")
            return

        # Obtener datos de la fila seleccionada
        item = seleccion[0]
        valores = self.tabla.item(item, "values")
        cedula = valores[0]

        # Llamar al servicio para eliminar
        if self.servicio.eliminar_visitante(cedula):
            messagebox.showinfo("Éxito", "Registro eliminado")
            self.actualizar_tabla()

    def seleccionar_registro(self, event):
        """
        Carga los datos de la fila seleccionada en el formulario.
        Permite editar (Update).
        """

        seleccion = self.tabla.selection()

        if seleccion:
            item = seleccion[0]
            valores = self.tabla.item(item, "values")

            # Limpiar antes de cargar nuevos datos
            self.limpiar_campos()

            # Insertar datos en los campos
            self.entry_cedula.insert(0, valores[0])
            self.entry_nombre.insert(0, valores[1])
            self.entry_motivo.insert(0, valores[2])

    def actualizar(self):
        """
        Método para actualizar un visitante (Update).
        Modifica los datos del objeto existente.
        """

        cedula = self.entry_cedula.get()
        nombre = self.entry_nombre.get()
        motivo = self.entry_motivo.get()

        # Validar campos vacíos
        if not cedula or not nombre or not motivo:
            messagebox.showwarning("Error", "Todos los campos son obligatorios")
            return

        actualizado = False

        # Buscar el visitante y actualizar sus datos
        for v in self.servicio.obtener_visitantes():
            if v.get_cedula() == cedula:
                v.set_nombre(nombre)
                v.set_motivo(motivo)
                actualizado = True
                break

        # Mensajes de resultado
        if actualizado:
            messagebox.showinfo("Éxito", "Registro actualizado")
            self.actualizar_tabla()
            self.limpiar_campos()
        else:
            messagebox.showerror("Error", "No se encontró el registro")

    def limpiar_campos(self):
        """
        Limpia todos los campos del formulario.
        """

        self.entry_cedula.delete(0, tk.END)
        self.entry_nombre.delete(0, tk.END)
        self.entry_motivo.delete(0, tk.END)

    def actualizar_tabla(self):
        """
        Refresca la tabla con los datos actuales del servicio (Read).
        """

        # Eliminar filas actuales
        for fila in self.tabla.get_children():
            self.tabla.delete(fila)

        # Insertar datos actualizados
        for v in self.servicio.obtener_visitantes():
            self.tabla.insert(
                "", "end",
                values=(v.get_cedula(), v.get_nombre(), v.get_motivo())
            )