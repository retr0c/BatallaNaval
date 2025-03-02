import unittest
from src.Juego import disparar

class TestDisparar(unittest.TestCase):

    # N
    def test_disparo_acierto(self):
        campo = [[0, 1], [0, 0]]
        resultado = disparar(campo, 0, 1)
        self.assertEqual(resultado, "¡Impacto!")

    def test_disparo_agua(self):
        campo = [[0, 1], [0, 0]]
        resultado = disparar(campo, 1, 0)
        self.assertEqual(resultado, "Agua")

    def test_disparo_repetido(self):
        campo = [[0, 1], [0, 0]]
        disparar(campo, 0, 1)
        resultado = disparar(campo, 0, 1)
        self.assertEqual(resultado, "Ya disparaste aquí")

    # E
    def test_disparo_en_borde(self):
        campo = [[1, 0], [0, 0]]
        resultado = disparar(campo, 0, 0)
        self.assertEqual(resultado, "¡Impacto!")

    def test_disparo_ultimo_casillero(self):
        campo = [[0, 0], [0, 1]]
        resultado = disparar(campo, 1, 1)
        self.assertEqual(resultado, "¡Impacto!")

    def test_disparo_fuera_de_rango(self):
        campo = [[0, 1], [0, 0]]
        with self.assertRaises(IndexError):
            disparar(campo, 2, 2)

    # E
    def test_disparo_fila_negativa(self):
        campo = [[0, 1], [0, 0]]
        with self.assertRaises(IndexError):
            disparar(campo, -1, 1)

    def test_disparo_columna_negativa(self):
        campo = [[0, 1], [0, 0]]
        with self.assertRaises(IndexError):
            disparar(campo, 1, -1)

    def test_disparo_en_campo_vacio(self):
        campo = []
        with self.assertRaises(IndexError):
            disparar(campo, 0, 0)

if __name__ == '__main__':
    unittest.main()
