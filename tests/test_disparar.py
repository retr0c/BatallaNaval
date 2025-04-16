import unittest
from BatallaNaval.src.Juego import Juego

class TestDisparar(unittest.TestCase):

    def setUp(self):
        self.juego = Juego()

    # Normales
    def test_disparo_acierto(self):
        campo = [[0, 1], [0, 0]]
        resultado = self.juego.disparar(campo, 0, 1)
        self.assertEqual(resultado, "¡Impacto!")

    def test_disparo_agua(self):
        campo = [[0, 1], [0, 0]]
        resultado = self.juego.disparar(campo, 1, 0)
        self.assertEqual(resultado, "Agua")

    def test_disparo_repetido(self):
        campo = [[0, 1], [0, 0]]
        self.juego.disparar(campo, 0, 1)
        resultado = self.juego.disparar(campo, 0, 1)
        self.assertEqual(resultado, "Ya disparaste aquí")

    # Extremas
    def test_disparo_en_borde(self):
        campo = [[1, 0], [0, 0]]
        resultado = self.juego.disparar(campo, 0, 0)
        self.assertEqual(resultado, "¡Impacto!")

    def test_disparo_ultimo_casillero(self):
        campo = [[0, 0], [0, 1]]
        resultado = self.juego.disparar(campo, 1, 1)
        self.assertEqual(resultado, "¡Impacto!")

    def test_disparo_fuera_de_rango(self):
        campo = [[0, 1], [0, 0]]
        with self.assertRaises(IndexError):
            self.juego.disparar(campo, 2, 2)

    # Error
    def test_disparo_fila_negativa(self):
        campo = [[0, 1], [0, 0]]
        with self.assertRaises(IndexError):
            self.juego.disparar(campo, -1, 1)

    def test_disparo_columna_negativa(self):
        campo = [[0, 1], [0, 0]]
        with self.assertRaises(IndexError):
            self.juego.disparar(campo, 1, -1)

    def test_disparo_en_campo_vacio(self):
        campo = []
        with self.assertRaises(IndexError):
            self.juego.disparar(campo, 0, 0)

if __name__ == '__main__':
    unittest.main()
