import random

class Juego():
    def iniciar_campo_juego(self, ancho, alto, naves=None):
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



