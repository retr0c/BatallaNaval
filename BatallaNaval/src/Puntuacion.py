from BatallaNaval.base_datos.db import guardar_puntuacion

class Puntuacion:
    """Clase que administra la lista de puntuaciones del juego."""

    def __init__(self):
        """Inicializa la clase Puntuacion sin puntuaciones predefinidas."""
        self.puntuaciones = []

    def agregar_puntuacion(self, usuario_id, puntaje):
        """Agrega una nueva puntuación a la base de datos."""
        if not isinstance(puntaje, int):
            raise ValueError("La puntuación debe ser un número entero.")
        
        # Guarda la puntuación en la base de datos
        guardar_puntuacion(usuario_id, puntaje)
        self.puntuaciones.append(puntaje)  

    def visualizar_puntuaciones(self):
        """Devuelve la lista de puntuaciones actuales."""
        return self.puntuaciones  