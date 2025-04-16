import unittest
from BatallaNaval.src.Jugador import Jugador

class TestCambiarContraseña(unittest.TestCase):

    def setUp(self):
        self.jugador = Jugador("usuario1", "contraseña123")

    # Casos normales
    def test_cambiar_contraseña_exitosa(self):
        resultado = self.jugador.cambiar_contraseña("nuevaContraseña456")
        self.assertEqual(resultado, "Contraseña cambiada exitosamente")

    def test_cambiar_contraseña_a_misma_contraseña(self):
        resultado = self.jugador.cambiar_contraseña("contraseña123")
        self.assertEqual(resultado, "La nueva contraseña no puede ser igual a la actual")

    def test_cambiar_contraseña_con_formato_valido(self):
        resultado = self.jugador.cambiar_contraseña("Valida123$")
        self.assertEqual(resultado, "Contraseña cambiada exitosamente")

    # Casos extremos
    def test_cambiar_contraseña_minima_longitud(self):
        resultado = self.jugador.cambiar_contraseña("abc12")
        self.assertEqual(resultado, "Contraseña demasiado corta")

    def test_cambiar_contraseña_maxima_longitud(self):
        contraseña_larga = "a" * 101
        resultado = self.jugador.cambiar_contraseña(contraseña_larga)
        self.assertEqual(resultado, "Contraseña demasiado larga")

    def test_cambiar_contraseña_con_caracteres_especiales(self):
        resultado = self.jugador.cambiar_contraseña("Contraseña@#456")
        self.assertEqual(resultado, "Contraseña cambiada exitosamente")

    # Casos de error
    def test_cambiar_contraseña_vacia(self):
        resultado = self.jugador.cambiar_contraseña("")
        self.assertEqual(resultado, "La contraseña no puede estar vacía")

    def test_cambiar_contraseña_nula(self):
        with self.assertRaises(TypeError):
            self.jugador.cambiar_contraseña(None)

    def test_cambiar_contraseña_tipo_incorrecto(self):
        with self.assertRaises(TypeError):
            self.jugador.cambiar_contraseña(123456)

if __name__ == "__main__":
    unittest.main()
