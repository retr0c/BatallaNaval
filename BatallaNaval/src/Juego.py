import random

class Juego:
    """Clase que maneja la lógica del juego Batalla Naval."""

    def iniciar_campo_juego(self, ancho, alto, naves=None):
        """
        Inicializa el campo de juego con naves colocadas aleatoriamente.
        
        :param ancho: Ancho del campo de juego.
        :param alto: Alto del campo de juego.
        :param naves: Número de naves a colocar (opcional).
        :return: Campo de juego como una matriz 2D.
        """
        if not isinstance(ancho, int) or not isinstance(alto, int):
            raise TypeError("Las dimensiones deben ser enteros")
        if ancho <= 0 or alto <= 0:
            raise ValueError("Las dimensiones deben ser mayores a 0")

        campo = [[0 for _ in range(ancho)] for _ in range(alto)]

        if naves is None:
            naves = (ancho * alto) // 10

        posiciones_disponibles = [(i, j) for i in range(alto) for j in range(ancho)]
        random.shuffle(posiciones_disponibles)

        for _ in range(min(naves, len(posiciones_disponibles))):
            x, y = posiciones_disponibles.pop()
            campo[x][y] = 1

        return campo

    def disparar(self, campo, fila, columna):
        """
        Realiza un disparo en el campo de juego.

        :param campo: Matriz del campo de juego.
        :param fila: Fila a disparar.
        :param columna: Columna a disparar.
        :return: Resultado del disparo como cadena.
        """
        if not (0 <= fila < len(campo) and 0 <= columna < len(campo[0])):
            raise IndexError("Coordenadas fuera de rango")

        if campo[fila][columna] == "X":
            return "Ya disparaste aquí"

        if campo[fila][columna] == 1:
            campo[fila][columna] = "X"
            return "¡Impacto!"
        else:
            campo[fila][columna] = "X"
            return "Agua"