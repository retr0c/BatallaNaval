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

        Levanta:
        - TypeError: Si la lista de puntuaciones no es una lista.
        - ValueError: Si algún elemento no es una tupla (usuario_id, puntaje) con puntaje int.
        """
        if desde_bd:
            return obtener_puntuaciones()

        # Validar que self.puntuaciones sea lista
        if not isinstance(self.puntuaciones, list):
            raise TypeError("Las puntuaciones deben ser una lista.")

        # Validar cada elemento
        for elem in self.puntuaciones:
            if not (isinstance(elem, tuple) and len(elem) == 2):
                raise ValueError("Cada puntuación debe ser una tupla (usuario_id, puntaje).")
            usuario_id, puntaje = elem
            if not isinstance(puntaje, int):
                raise ValueError("El puntaje debe ser un número entero.")
            # opcional: podrías validar usuario_id aquí si quieres

        return self.puntuaciones