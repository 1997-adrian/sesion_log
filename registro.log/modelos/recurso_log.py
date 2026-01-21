"""
Módulo que define la clase RecursoLog.
Representa un recurso que escribe en un archivo de log.
Utiliza __init__ para abrir el archivo y __del__ para cerrarlo.
"""

class RecursoLog:
    """
    Clase que representa un recurso de escritura en un archivo de log.
    """

    def __init__(self, nombre_archivo="registro.log"):
        """
        Constructor: inicializa el recurso abriendo un archivo de log.
        - nombre_archivo: nombre del archivo donde se escribirán los logs.
        """
        self.nombre_archivo = nombre_archivo
        try:
            self.archivo = open(self.nombre_archivo, "a", encoding="utf-8")
            self.archivo.write("=== Inicio de sesión ===\n")
            print(f"[INFO] Archivo de log '{nombre_archivo}' abierto.")
        except IOError as e:
            print(f"[ERROR] No se pudo abrir el archivo: {e}")
            self.archivo = None

    def registrar(self, mensaje):
        """
        Registra un mensaje en el archivo de log.
        """
        if self.archivo and not self.archivo.closed:
            self.archivo.write(f"{mensaje}\n")
            print(f"[LOG] Registrado: {mensaje}")

    def __del__(self):
        """
        Destructor: intenta cerrar el archivo si aún está abierto.
        Se ejecuta cuando el objeto es destruido (por ejemplo, al final del programa o con 'del').
        Nota: En Python, el destructor no garantiza ejecución inmediata debido al garbage collector.
        """
        if hasattr(self, 'archivo') and self.archivo and not self.archivo.closed:
            self.archivo.write("=== Fin de sesión ===\n")
            self.archivo.close()
            print(f"[INFO] Archivo de log '{self.nombre_archivo}' cerrado correctamente.")
