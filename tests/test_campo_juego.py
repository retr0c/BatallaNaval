import unittest
from src.batalla_naval import iniciar_campo_juego

class TestIniciarCampoJuego(unittest.TestCase):

    # Pruebas normales
    def test_campo_10x10(self):
        campo = iniciar_campo_juego(10, 10)
        self.assertEqual(len(campo), 10)
        self.assertEqual(len(campo[0]), 10)

    def test_campo_5x5(self):
        campo = iniciar_campo_juego(5, 5)
        self.assertEqual(len(campo), 5)
        self.assertEqual(len(campo[0]), 5)

    def test_naves_en_posiciones_validas(self):
        campo = iniciar_campo_juego(10, 10)
        for fila in campo:
            for celda in fila:
                self.assertIn(celda, [0, 1])  # 0 = vacío, 1 = nave

    # Pruebas extremas
    def test_campo_1x1(self):
        campo = iniciar_campo_juego(1, 1)
        self.assertEqual(len(campo), 1)
        self.assertEqual(len(campo[0]), 1)

    def test_campo_100x100(self):
        campo = iniciar_campo_juego(100, 100)
        self.assertEqual(len(campo), 100)
        self.assertEqual(len(campo[0]), 100)

    def test_campo_sin_naves(self):
        campo = iniciar_campo_juego(10, 10, 0)  # Suponiendo que el tercer parámetro es cantidad de naves
        self.assertTrue(all(celda == 0 for fila in campo for celda in fila))

    # Pruebas de error
    def test_dimensiones_negativas(self):
        with self.assertRaises(ValueError):
            iniciar_campo_juego(-5, 5)

    def test_dimensiones_no_enteras(self):
        with self.assertRaises(TypeError):
            iniciar_campo_juego("10", 10)

    def test_sin_parametros(self):
        with self.assertRaises(TypeError):
            iniciar_campo_juego()

if __name__ == "__main__":
    unittest.main()
