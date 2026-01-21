"""
Punto de entrada del programa.
Demuestra el uso de constructores y destructores mediante la gestión de un recurso de log.
"""

from servicios.gestor_recursos import GestorRecursos

def main():
    print("=== Iniciando programa ===")
    
    # Crear gestor de recursos → se llama al constructor de RecursoLog
    gestor = GestorRecursos("mi_sesion.log")
    
    # Ejecutar algunas tareas
    gestor.ejecutar_tarea("Procesar datos del usuario")
    gestor.ejecutar_tarea("Enviar notificación por correo")
    
    print("\n[MAIN] Finalizando programa...\n")
    
    # El destructor de RecursoLog se llamará automáticamente
    # cuando el objeto 'gestor' salga de alcance (al final de main)
    # o cuando el intérprete termine.

if __name__ == "__main__":
    main()