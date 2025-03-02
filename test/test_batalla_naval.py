import unittest
from src.batalla_naval import (
    iniciar_campo_juego,
    disparar,
    iniciar_sesion,
    crear_cuenta,
    cambiar_contraseña,
    visualizar_puntuaciones
)

class TestBatallaNaval(unittest.TestCase):

    def test_iniciar_campo_juego(self):
        self.assertIsNotNone(iniciar_campo_juego(10, 10))

    def test_disparar(self):
        self.assertIsNone(disparar(5, 5))

    def test_iniciar_sesion(self):
        self.assertIsNone(iniciar_sesion("usuario", "contraseña"))

    def test_crear_cuenta(self):
        self.assertIsNone(crear_cuenta("nuevo_usuario", "nueva_contraseña"))

    def test_cambiar_contraseña(self):
        self.assertIsNone(cambiar_contraseña("usuario", "nueva_contraseña"))

    def test_visualizar_puntuaciones(self):
        self.assertIsNone(visualizar_puntuaciones())

if __name__ == "__main__":
    unittest.main()
