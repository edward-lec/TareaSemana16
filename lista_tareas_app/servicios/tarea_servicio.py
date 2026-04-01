from modelos.tarea import Tarea

# Clase que maneja la lógica del sistema
class TareaServicio:
    def __init__(self):
        self._tareas = []
        self._contador_id = 1

    def agregar_tarea(self, descripcion):
        """
        Crea y agrega una nueva tarea
        """
        tarea = Tarea(self._contador_id, descripcion)
        self._tareas.append(tarea)
        self._contador_id += 1
        return tarea

    def obtener_tareas(self):
        """
        Retorna todas las tareas
        """
        return self._tareas

    def completar_tarea(self, id):
        """
        Marca una tarea como completada
        """
        for tarea in self._tareas:
            if tarea.get_id() == id:
                tarea.marcar_completada()
                return True
        return False

    def eliminar_tarea(self, id):
        """
        Elimina una tarea por su ID
        """
        for tarea in self._tareas:
            if tarea.get_id() == id:
                self._tareas.remove(tarea)
                return True
        return False