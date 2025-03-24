import unittest
from BatallaNaval.src.Puntuacion import Puntuacion



class TestVisualizarPuntuaciones(unittest.TestCase):

    def test_agregar_puntuacion_correcta(self):
        puntuacion = Puntuacion()
        puntuacion.agregar_puntuacion(250)
        self.assertEqual(puntuacion.puntuaciones, [250])
        
    def test_agregar_puntuacion_invalida(self):
        puntuacion = Puntuacion()
        with self.assertRaises(ValueError):
            puntuacion.agregar_puntuacion("cien")
    

    
    # Pruebas normales (N)
    def test_visualizar_con_puntuaciones(self):
        puntuacion = Puntuacion()
        puntuacion.puntuaciones = [100, 200, 300]
        resultado = puntuacion.visualizar_puntuaciones()
        self.assertEqual(resultado, [100, 200, 300])

    def test_visualizar_una_sola_puntuacion(self):
        puntuacion = Puntuacion()
        puntuacion.puntuaciones = [150]
        resultado = puntuacion.visualizar_puntuaciones()
        self.assertEqual(resultado, [150])

    def test_visualizar_sin_puntuaciones(self):
        puntuacion = Puntuacion()
        puntuacion.puntuaciones = []
        resultado = puntuacion.visualizar_puntuaciones()
        self.assertEqual(resultado, [])

    # Pruebas extremas (E)
    def test_visualizar_puntuaciones_maximas(self):
        puntuacion = Puntuacion()
        puntuacion.puntuaciones = [99999] * 1000
        resultado = puntuacion.visualizar_puntuaciones()
        self.assertEqual(len(resultado), 1000)
        self.assertEqual(resultado[0], 99999)

    def test_visualizar_puntuaciones_minimas(self):
        puntuacion = Puntuacion()
        puntuacion.puntuaciones = [0] * 1000
        resultado = puntuacion.visualizar_puntuaciones()
        self.assertEqual(len(resultado), 1000)
        self.assertEqual(resultado[0], 0)

    def test_visualizar_puntuaciones_muy_variadas(self):
        puntuacion = Puntuacion()
        puntuacion.puntuaciones = [1, 100, 10000, 500, 50]
        resultado = puntuacion.visualizar_puntuaciones()
        self.assertEqual(resultado, [1, 100, 10000, 500, 50])

    # Pruebas de error (E)
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
        puntuacion.puntuaciones = [100, "puntaje", 300]
        with self.assertRaises(ValueError):
            puntuacion.visualizar_puntuaciones()

if __name__ == '__main__':
    unittest.main()
