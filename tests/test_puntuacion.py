import unittest
from BatallaNaval.src.Puntuacion import Puntuacion

class TestVisualizarPuntuaciones(unittest.TestCase):

    # Normales
    def test_agregar_puntuacion_correcta(self):
        puntuacion = Puntuacion()
        puntuacion.agregar_puntuacion(1, 250)  # Usuario id 1
        self.assertEqual(puntuacion.puntuaciones, [(1, 250)])

    def test_agregar_puntuacion_invalida(self):
        puntuacion = Puntuacion()
        with self.assertRaises(ValueError):
            puntuacion.agregar_puntuacion(1, "cien")  # Puntaje inválido

    def test_visualizar_con_puntuaciones(self):
        puntuacion = Puntuacion()
        puntuacion.puntuaciones = [(1, 100), (2, 200), (3, 300)]
        resultado = puntuacion.visualizar_puntuaciones()
        self.assertEqual(resultado, [(1, 100), (2, 200), (3, 300)])

    def test_visualizar_una_sola_puntuacion(self):
        puntuacion = Puntuacion()
        puntuacion.puntuaciones = [(1, 150)]
        resultado = puntuacion.visualizar_puntuaciones()
        self.assertEqual(resultado, [(1, 150)])

    def test_visualizar_sin_puntuaciones(self):
        puntuacion = Puntuacion()
        puntuacion.puntuaciones = []
        resultado = puntuacion.visualizar_puntuaciones()
        self.assertEqual(resultado, [])

    # Extremas
    def test_visualizar_puntuaciones_maximas(self):
        puntuacion = Puntuacion()
        puntuacion.puntuaciones = [(i, 99999) for i in range(1000)]
        resultado = puntuacion.visualizar_puntuaciones()
        self.assertEqual(len(resultado), 1000)
        self.assertEqual(resultado[0][1], 99999)

    def test_visualizar_puntuaciones_minimas(self):
        puntuacion = Puntuacion()
        puntuacion.puntuaciones = [(i, 0) for i in range(1000)]
        resultado = puntuacion.visualizar_puntuaciones()
        self.assertEqual(len(resultado), 1000)
        self.assertEqual(resultado[0][1], 0)

    def test_visualizar_puntuaciones_muy_variadas(self):
        puntuacion = Puntuacion()
        puntuacion.puntuaciones = [(1, 1), (2, 100), (3, 10000), (4, 500), (5, 50)]
        resultado = puntuacion.visualizar_puntuaciones()
        self.assertEqual(resultado, [(1, 1), (2, 100), (3, 10000), (4, 500), (5, 50)])

    # Error
    def test_visualizar_puntuaciones_nulas(self):
        puntuacion = Puntuacion()
        puntuacion.puntuaciones = None
        with self.assertRaises(TypeError):
            puntuacion.visualizar_puntuaciones()

    def test_visualizar_puntuaciones_formato_incorrecto(self):
        puntuacion = Puntuacion()
        puntuacion.puntuaciones = "no es una lista"
        with self.assertRaises(TypeError):
            puntuacion.visualizar_puntuaciones()

    def test_visualizar_puntuaciones_con_elementos_invalidos(self):
        puntuacion = Puntuacion()
        puntuacion.puntuaciones = [(1, 100), (2, "puntaje"), (3, 300)]
        with self.assertRaises(ValueError):
            puntuacion.visualizar_puntuaciones()

if __name__ == '__main__':
    unittest.main()
