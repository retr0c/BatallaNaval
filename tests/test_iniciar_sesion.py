import unittest
from src.Jugador import iniciar_sesion

class TestIniciarSesion(unittest.TestCase):

    #N
    def test_sesion_exitosa(self):
        resultado = iniciar_sesion("usuario1", "contraseña123")
        self.assertEqual(resultado, "Sesión iniciada")

    def test_usuario_incorrecto(self):
        resultado = iniciar_sesion("usuario_invalido", "contraseña123")
        self.assertEqual(resultado, "Usuario no encontrado")

    def test_contraseña_incorrecta(self):
        resultado = iniciar_sesion("usuario1", "contraseña_erronea")
        self.assertEqual(resultado, "Contraseña incorrecta")

    #E
    def test_usuario_vacio(self):
        resultado = iniciar_sesion("", "contraseña123")
        self.assertEqual(resultado, "Usuario no puede estar vacío")

    def test_contraseña_vacia(self):
        resultado = iniciar_sesion("usuario1", "")
        self.assertEqual(resultado, "Contraseña no puede estar vacía")

    def test_credenciales_vacias(self):
        resultado = iniciar_sesion("", "")
        self.assertEqual(resultado, "Credenciales incompletas")

    #E
    def test_usuario_nulo(self):
        with self.assertRaises(TypeError):
            iniciar_sesion(None, "contraseña123")

    def test_contraseña_nula(self):
        with self.assertRaises(TypeError):
            iniciar_sesion("usuario1", None)

    def test_ambos_nulos(self):
        with self.assertRaises(TypeError):
            iniciar_sesion(None, None)

if __name__ == '__main__':
    unittest.main()
