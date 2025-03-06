import random

class Ecosistema:
    def __init__(self, tamano, num_depredadores, num_presas, num_plantas):
        self.tamano = tamano
        self.matriz = self.crear_matriz(tamano, tamano)
        self.poblar(num_depredadores, Depredador)
        self.poblar(num_presas, Presa)
        self.poblar(num_plantas, Planta)

    def crear_matriz(self, filas, cols):
        if filas == 0:
            return []
        else:
            return [self.crear_fila(cols)] + self.crear_matriz(filas - 1, cols)

    def crear_fila(self, cols):
        if cols == 0:
            return []
        else:
            return [None] + self.crear_fila(cols - 1)

    def poblar(self, cantidad, tipo_entidad):
        if cantidad == 0:
            return
        x, y = random.randint(0, self.tamano - 1), random.randint(0, self.tamano - 1)
        if self.matriz[x][y] is None:
            self.matriz[x][y] = tipo_entidad()
            cantidad -= 1
        self.poblar(cantidad, tipo_entidad)

    def simular(self, ciclos, ciclo_actual=1):
        if ciclos == 0 or not self.hay_organismos_rec(0, 0):
            print("\nSimulación terminada")
            return
        print("\nCiclo", ciclo_actual)
        self.mostrar_rec(0)
        self.actualizar(0, 0)
        if ciclo_actual % 3 == 0:
            self.regenerar_planta()
        self.simular(ciclos - 1, ciclo_actual + 1)

    def hay_organismos_rec(self, x, y):
        if x == self.tamano:
            return False
        if y == self.tamano:
            return self.hay_organismos_rec(x + 1, 0)
        if self.matriz[x][y] is not None:
            return True
        return self.hay_organismos_rec(x, y + 1)

    def actualizar(self, x, y):
        if x == self.tamano:
            return
        if y == self.tamano:
            self.actualizar(x + 1, 0)
            return
        entidad = self.matriz[x][y]
        if entidad is not None:
            entidad.actuar(x, y, self)
        self.actualizar(x, y + 1)

    def mover(self, x, y, nuevo_x, nuevo_y):
        if 0 <= nuevo_x < self.tamano and 0 <= nuevo_y < self.tamano and self.matriz[nuevo_x][nuevo_y] is None:
            print(type(self.matriz[x][y]).__name__, "se movió de (", x, ",", y, ") a (", nuevo_x, ",", nuevo_y, ")")
            self.matriz[nuevo_x][nuevo_y] = self.matriz[x][y]
            self.matriz[x][y] = None

    def mostrar_rec(self, fila):
        if fila == self.tamano:
            return
        self.mostrar_fila(fila, 0)
        print("")
        self.mostrar_rec(fila + 1)

    def mostrar_fila(self, fila, col):
        if col == self.tamano:
            return
        simbolo = '.'
        celda = self.matriz[fila][col]
        if celda is not None:
            if isinstance(celda, Depredador):
                simbolo = 'D'
            elif isinstance(celda, Presa):
                simbolo = 'P'
            elif isinstance(celda, Planta):
                simbolo = '*'
        print(simbolo, end=" ")
        self.mostrar_fila(fila, col + 1)

    def regenerar_planta(self):
        x = random.randint(0, self.tamano - 1)
        y = random.randint(0, self.tamano - 1)
        if self.matriz[x][y] is None:
            print("Una planta se ha regenerado en (", x, ",", y, ")")
            self.matriz[x][y] = Planta()
        else:
            self.regenerar_planta()

class Depredador:
    def __init__(self):
        self.energia = 5

    def actuar(self, x, y, ecosistema):
        self.energia -= 1
        if self.energia <= 0:
            print("El Depredador en (", x, ",", y, ") murió de hambre")
            ecosistema.matriz[x][y] = None
            return
        pos = self.buscar_presa_visible(x, y, ecosistema, 1)
        if pos is not None:
            nuevo_x, nuevo_y = pos
            print("El Depredador en (", x, ",", y, ") se comió a la Presa en (", nuevo_x, ",", nuevo_y, ")")
            ecosistema.matriz[nuevo_x][nuevo_y] = self
            ecosistema.matriz[x][y] = None
            self.energia = 5
        else:
            self.mover_aleatorio(x, y, ecosistema)
        if self.energia >= 7:
            self.reproducir(x, y, ecosistema, [(0, 1), (1, 0), (0, -1), (-1, 0)], 0)
            self.energia = 5

    def buscar_presa_visible(self, x, y, ecosistema, d):
        if d >= ecosistema.tamano:
            return None
        if y - d >= 0 and isinstance(ecosistema.matriz[x][y - d], Presa):
            return (x, y - d)
        if y + d < ecosistema.tamano and isinstance(ecosistema.matriz[x][y + d], Presa):
            return (x, y + d)
        if x - d >= 0 and isinstance(ecosistema.matriz[x - d][y], Presa):
            return (x - d, y)
        if x + d < ecosistema.tamano and isinstance(ecosistema.matriz[x + d][y], Presa):
            return (x + d, y)
        return self.buscar_presa_visible(x, y, ecosistema, d + 1)

    def mover_aleatorio(self, x, y, ecosistema):
        movimientos = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        random.shuffle(movimientos)
        self.intentar_mover(x, y, ecosistema, movimientos, 0)

    def intentar_mover(self, x, y, ecosistema, movimientos, i):
        if i == len(movimientos):
            return
        dx, dy = movimientos[i]
        nuevo_x, nuevo_y = x + dx, y + dy
        if 0 <= nuevo_x < ecosistema.tamano and 0 <= nuevo_y < ecosistema.tamano and ecosistema.matriz[nuevo_x][nuevo_y] is None:
            ecosistema.mover(x, y, nuevo_x, nuevo_y)
            return
        self.intentar_mover(x, y, ecosistema, movimientos, i + 1)

    def reproducir(self, x, y, ecosistema, movimientos, i):
        if i == len(movimientos):
            return
        dx, dy = movimientos[i]
        nuevo_x, nuevo_y = x + dx, y + dy
        if 0 <= nuevo_x < ecosistema.tamano and 0 <= nuevo_y < ecosistema.tamano and ecosistema.matriz[nuevo_x][nuevo_y] is None:
            print("El Depredador en (", x, ",", y, ") se reproduce en (", nuevo_x, ",", nuevo_y, ")")
            ecosistema.matriz[nuevo_x][nuevo_y] = Depredador()
            return
        self.reproducir(x, y, ecosistema, movimientos, i + 1)

class Presa:
    def __init__(self):
        self.contador_reproduccion = 0

    def actuar(self, x, y, ecosistema):
        movimientos = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        random.shuffle(movimientos)
        self.intentar_mover(x, y, ecosistema, movimientos, 0)
        self.contador_reproduccion += 1
        if self.contador_reproduccion >= 3:
            self.reproducir(x, y, ecosistema, [(0, 1), (1, 0), (0, -1), (-1, 0)], 0)
            self.contador_reproduccion = 0

    def intentar_mover(self, x, y, ecosistema, movimientos, i):
        if i == len(movimientos):
            return
        dx, dy = movimientos[i]
        nuevo_x, nuevo_y = x + dx, y + dy
        if 0 <= nuevo_x < ecosistema.tamano and 0 <= nuevo_y < ecosistema.tamano and ecosistema.matriz[nuevo_x][nuevo_y] is None:
            ecosistema.mover(x, y, nuevo_x, nuevo_y)
            return
        self.intentar_mover(x, y, ecosistema, movimientos, i + 1)

    def reproducir(self, x, y, ecosistema, movimientos, i):
        if i == len(movimientos):
            return
        dx, dy = movimientos[i]
        nuevo_x, nuevo_y = x + dx, y + dy
        if 0 <= nuevo_x < ecosistema.tamano and 0 <= nuevo_y < ecosistema.tamano and ecosistema.matriz[nuevo_x][nuevo_y] is None:
            print("La Presa en (", x, ",", y, ") se reproduce en (", nuevo_x, ",", nuevo_y, ")")
            ecosistema.matriz[nuevo_x][nuevo_y] = Presa()
            return
        self.reproducir(x, y, ecosistema, movimientos, i + 1)

class Planta:
    def actuar(self, x, y, ecosistema):
        return

if __name__ == "__main__":
    ecosistema = Ecosistema(tamano=5, num_depredadores=2, num_presas=4, num_plantas=6)
    ecosistema.simular(10)
