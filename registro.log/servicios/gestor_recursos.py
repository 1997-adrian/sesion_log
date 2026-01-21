"""
Módulo que contiene la lógica de gestión de recursos.
Usa la clase RecursoLog del modelo para realizar operaciones controladas.
"""

from modelos.recurso_log import RecursoLog

class GestorRecursos:
    """
    Clase que gestiona el uso de recursos como archivos de log.
    Separa la lógica de negocio de la representación del recurso.
    """

    def __init__(self, nombre_archivo="registro.log"):
        """
        Inicializa el gestor creando un recurso de log.
        """
        self.recurso = RecursoLog(nombre_archivo)

    def ejecutar_tarea(self, descripcion):
        """
        Simula una tarea del sistema y registra su inicio y fin.
        """
        self.recurso.registrar(f"Iniciando tarea: {descripcion}")
        # Aquí iría la lógica real de la tarea
        self.recurso.registrar(f"Tarea completada: {descripcion}")

    def liberar_recurso(self):
        """
        Opcional: permite cerrar explícitamente el recurso antes de que el objeto sea destruido.
        Esto es una buena práctica para evitar depender solo del destructor.
        """
        del self.recurso
