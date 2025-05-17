from BatallaNaval.base_datos.db import guardar_puntuacion, obtener_puntuaciones

class Puntuacion:
    """Clase que administra la lista de puntuaciones del juego."""

    def __init__(self):
        """Inicializa la clase Puntuacion sin puntuaciones predefinidas."""
        self.puntuaciones = []

    def agregar_puntuacion(self, usuario_id, puntaje):
        """
        Agrega una nueva puntuación a la base de datos y a la lista local.

        Parámetros:
        - usuario_id (int): ID del usuario.
        - puntaje (int): Puntuación obtenida.

        Levanta:
        - ValueError: Si la puntuación no es un número entero.
        """
        if not isinstance(puntaje, int):
            raise ValueError("La puntuación debe ser un número entero.")
        self.puntuaciones.append((usuario_id, puntaje))
        guardar_puntuacion(usuario_id, puntaje)

    def visualizar_puntuaciones(self, desde_bd=False):
        """
        Devuelve la lista de puntuaciones.

        Parámetros:
        - desde_bd (bool): Si es True, obtiene las puntuaciones desde la base de datos.

        Retorna:
        - list: Lista de puntuaciones.
        """
        if desde_bd:
            return obtener_puntuaciones()
        return self.puntuaciones
