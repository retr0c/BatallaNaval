import unittest
from BatallaNaval.src.Jugador import Jugador
from sqlalchemy.orm import sessionmaker
from BatallaNaval.base_datos.db import engine
from BatallaNaval.base_datos.modelo import Usuario  # Importa el modelo Usuario

Session = sessionmaker(bind=engine)

class TestIniciarSesion(unittest.TestCase):

    def setUp(self):
        # Crear sesión para manipulación directa en el test
        self.session = Session()
        
        # Limpiar la tabla usuarios que tengan nombre 'usuario%'
        self.session.query(Usuario).filter(Usuario.nombre.like("usuario%")).delete()
        self.session.commit()

        # Crear instancia de Jugador pasando la sesión para que use la misma DB
        self.jugador = Jugador(session=self.session)

        # Crear cuenta para probar inicio de sesión
        self.jugador.crear_cuenta("usuario1", "contraseña123")

    def tearDown(self):
        self.session.close()

    def test_sesion_exitosa(self):
        resultado = self.jugador.iniciar_sesion("usuario1", "contraseña123")
        self.assertEqual(resultado, "Sesión iniciada")

    def test_usuario_incorrecto(self):
        resultado = self.jugador.iniciar_sesion("usuario_invalido", "contraseña123")
        self.assertEqual(resultado, "Usuario no encontrado")

    def test_contraseña_incorrecta(self):
        resultado = self.jugador.iniciar_sesion("usuario1", "contraseña_erronea")
        self.assertEqual(resultado, "Contraseña incorrecta")

    def test_credenciales_vacias(self):
        resultado = self.jugador.iniciar_sesion("", "")
        self.assertEqual(resultado, "Credenciales incompletas")

    def test_usuario_vacio(self):
        resultado = self.jugador.iniciar_sesion("", "contraseña123")
        self.assertEqual(resultado, "Usuario no puede estar vacío")

    def test_contraseña_vacia(self):
        resultado = self.jugador.iniciar_sesion("usuario1", "")
        self.assertEqual(resultado, "Contraseña no puede estar vacía")

    def test_usuario_nulo(self):
        with self.assertRaises(TypeError):
            self.jugador.iniciar_sesion(None, "contraseña123")

    def test_contraseña_nula(self):
        with self.assertRaises(TypeError):
            self.jugador.iniciar_sesion("usuario1", None)

    def test_ambos_nulos(self):
        with self.assertRaises(TypeError):
            self.jugador.iniciar_sesion(None, None)


if __name__ == '__main__':
    unittest.main()
