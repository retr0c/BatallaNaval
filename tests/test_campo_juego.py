import unittest
from BatallaNaval.src.Juego import Juego

class TestIniciarCampoJuego(unittest.TestCase):

    def setUp(self):
        self.juego = Juego()

    # Casos normales
    def test_campo_10x10(self):
        campo = self.juego.iniciar_campo_juego(10, 10)
        self.assertEqual(len(campo), 10)
        self.assertEqual(len(campo[0]), 10)

    def test_campo_rectangular(self):
        campo = self.juego.iniciar_campo_juego(10, 5)
        self.assertEqual(len(campo), 5)
        self.assertEqual(len(campo[0]), 10)

    def test_naves_en_posiciones_validas(self):
        campo = self.juego.iniciar_campo_juego(10, 10)
        for fila in campo:
            for celda in fila:
                self.assertIn(celda, [0, 1])

    # Casos extremos
    def test_campo_1x1(self):
        campo = self.juego.iniciar_campo_juego(1, 1)
        self.assertEqual(len(campo), 1)
        self.assertEqual(len(campo[0]), 1)

    def test_campo_100x100(self):
        campo = self.juego.iniciar_campo_juego(100, 100)
        self.assertEqual(len(campo), 100)
        self.assertEqual(len(campo[0]), 100)

    def test_campo_sin_naves(self):
        campo = self.juego.iniciar_campo_juego(10, 10, 0)
        for fila in campo:
            for celda in fila:
                self.assertEqual(celda, 0)

    # Casos de error
    def test_dimensiones_negativas(self):
        with self.assertRaises(ValueError):
            self.juego.iniciar_campo_juego(-5, 5)

    def test_dimensiones_no_enteras(self):
        with self.assertRaises(TypeError):
            self.juego.iniciar_campo_juego("10", 10)

    def test_sin_parametros(self):
        with self.assertRaises(TypeError):
            self.juego.iniciar_campo_juego()

if __name__ == '__main__':
    unittest.main()
