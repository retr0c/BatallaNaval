import unittest
from BatallaNaval.src.Jugador import Jugador

class TestCrearCuenta(unittest.TestCase):

    # N - Casos normales
    def test_creacion_exitosa(self):
        jugador = Jugador()
        resultado = jugador.crear_cuenta("usuario1", "contraseña123")
        self.assertEqual(resultado, "Cuenta creada exitosamente")

    def test_usuario_diferente(self):
        jugador = Jugador()
        resultado = jugador.crear_cuenta("otroUsuario", "claveSegura456")
        self.assertEqual(resultado, "Cuenta creada exitosamente")

    def test_contraseña_larga(self):
        jugador = Jugador()
        resultado = jugador.crear_cuenta("usuario2", "contraseñaMuyLarga123456")
        self.assertEqual(resultado, "Cuenta creada exitosamente")

    # E - Casos extremos
    def test_usuario_corto(self):
        jugador = Jugador()
        resultado = jugador.crear_cuenta("u", "clave123")
        self.assertEqual(resultado, "Cuenta creada exitosamente")

    def test_contraseña_corta(self):
        jugador = Jugador()
        resultado = jugador.crear_cuenta("usuario3", "c")
        self.assertEqual(resultado, "Cuenta creada exitosamente")

    def test_credenciales_largas(self):
        jugador = Jugador()
        usuario_largo = "usuario" * 50
        contraseña_larga = "clave" * 50
        resultado = jugador.crear_cuenta(usuario_largo, contraseña_larga)
        self.assertEqual(resultado, "Cuenta creada exitosamente")

    # E - Casos de error
    def test_usuario_vacio(self):
        jugador = Jugador()
        resultado = jugador.crear_cuenta("", "contraseña123")
        self.assertEqual(resultado, "El usuario no puede estar vacío")

    def test_contraseña_vacia(self):
        jugador = Jugador()
        resultado = jugador.crear_cuenta("usuario4", "")
        self.assertEqual(resultado, "La contraseña no puede estar vacía")

    def test_ambos_vacios(self):
        jugador = Jugador()
        resultado = jugador.crear_cuenta("", "")
        self.assertEqual(resultado, "Las credenciales no pueden estar vacías")

if __name__ == '__main__':
    unittest.main()
