class Puntuacion:
    """Clase que administra la lista de puntuaciones del juego."""

    def __init__(self):
        """
        Inicializa la clase Puntuacion con una lista vacía.
        """
        self.puntuaciones = []

    def agregar_puntuacion(self, puntaje):
        """
        Agrega una nueva puntuación a la lista.

        Args:
            puntaje (int): Puntuación a agregar.

        Raises:
            ValueError: Si el puntaje no es un número entero.
        """
        if not isinstance(puntaje, int):
            raise ValueError("La puntuación debe ser un número entero.")
        self.puntuaciones.append(puntaje)

    def visualizar_puntuaciones(self):
        """
        Devuelve la lista de puntuaciones actuales.

        Returns:
            list: Lista de puntuaciones.

        Raises:
            TypeError: Si las puntuaciones no están en una lista.
            ValueError: Si algún elemento no es un número entero.
        """
        if not isinstance(self.puntuaciones, list):
            raise TypeError("Las puntuaciones deben estar en una lista.")

        for puntuacion in self.puntuaciones:
            if not isinstance(puntuacion, int):
                raise ValueError("Todas las puntuaciones deben ser números enteros.")

        return self.puntuaciones
