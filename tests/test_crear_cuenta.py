import unittest
from sqlalchemy.orm import sessionmaker
from BatallaNaval.src.Jugador import Jugador
from BatallaNaval.base_datos.db import engine
from BatallaNaval.base_datos.modelo import Usuario, Puntuacion  # Importa Puntuacion

Session = sessionmaker(bind=engine)

class TestCrearCuenta(unittest.TestCase):

    def setUp(self):
        self.session = Session()
        # Borra las puntuaciones de usuarios con nombre que empiece con "usuario"
        usuarios = self.session.query(Usuario).filter(Usuario.nombre.like("usuario%")).all()
        for u in usuarios:
            self.session.query(Puntuacion).filter(Puntuacion.usuario_id == u.id).delete()
        # Borra esos usuarios
        self.session.query(Usuario).filter(Usuario.nombre.like("usuario%")).delete()
        self.session.commit()

    def tearDown(self):
        self.session.close()

    def test_creacion_exitosa(self):
        jugador = Jugador()
        resultado = jugador.crear_cuenta("usuario1", "contraseña123")
        self.assertEqual(resultado, "Cuenta creada exitosamente")

    def test_usuario_diferente(self):
        jugador = Jugador()
        resultado = jugador.crear_cuenta("usuario2", "claveSegura456")
        self.assertEqual(resultado, "Cuenta creada exitosamente")

    def test_contraseña_larga(self):
        jugador = Jugador()
        resultado = jugador.crear_cuenta("usuario3", "contraseñaMuyLarga123456")
        self.assertEqual(resultado, "Cuenta creada exitosamente")

    def test_usuario_corto(self):
        jugador = Jugador()
        resultado = jugador.crear_cuenta("u" + str(id(self)), "clave123")
        self.assertEqual(resultado, "Cuenta creada exitosamente")

    def test_contraseña_corta(self):
        jugador = Jugador()
        resultado = jugador.crear_cuenta("usuario4", "c")
        self.assertEqual(resultado, "Cuenta creada exitosamente")

    def test_credenciales_largas(self):
        jugador = Jugador()
        usuario_largo = "usuario" * 5 + str(id(self))  # para no repetir
        contraseña_larga = "clave" * 5
        resultado = jugador.crear_cuenta(usuario_largo, contraseña_larga)
        self.assertEqual(resultado, "Cuenta creada exitosamente")

    def test_ambos_vacios(self):
        jugador = Jugador()
        resultado = jugador.crear_cuenta("", "")
        self.assertEqual(resultado, "Las credenciales no pueden estar vacías")

    def test_usuario_vacio(self):
        jugador = Jugador()
        resultado = jugador.crear_cuenta("", "contraseña123")
        self.assertEqual(resultado, "El usuario no puede estar vacío")

    def test_contraseña_vacia(self):
        jugador = Jugador()
        resultado = jugador.crear_cuenta("usuario5", "")
        self.assertEqual(resultado, "La contraseña no puede estar vacía")

if __name__ == '__main__':
    unittest.main()
