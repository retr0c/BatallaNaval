class Puntuacion:
    def __init__(self):
        self.puntuaciones = []

    def agregar_puntuacion(self, puntaje):
        if not isinstance(puntaje, int):
            raise ValueError("La puntuación debe ser un número entero.")
        self.puntuaciones.append(puntaje)

    def visualizar_puntuaciones(self):
        if not isinstance(self.puntuaciones, list):
            raise TypeError("Las puntuaciones deben estar en una lista.")

        for puntuacion in self.puntuaciones:
            if not isinstance(puntuacion, int):
                raise ValueError("Todas las puntuaciones deben ser números enteros.")

        return self.puntuaciones