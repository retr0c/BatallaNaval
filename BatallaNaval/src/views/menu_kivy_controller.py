from kivy.uix.screenmanager import Screen
from BatallaNaval.src.Jugador import Jugador

jugador = Jugador()

class MenuInicio(Screen):
    pass

class CrearCuenta(Screen):
    def crear_cuenta(self):
        usuario = self.ids.usuario_input.text
        contraseña = self.ids.contraseña_input.text
        resultado = jugador.crear_cuenta(usuario, contraseña)
        self.ids.resultado.text = resultado

class IniciarSesion(Screen):
    def iniciar_sesion(self):
        usuario = self.ids.usuario_login.text
        contraseña = self.ids.contraseña_login.text
        resultado = jugador.iniciar_sesion(usuario, contraseña)
        self.ids.resultado_login.text = resultado
        if resultado == "Sesión iniciada":
            self.manager.current = "menu_principal"

class MenuPrincipal(Screen):
    def cerrar_sesion(self):
        jugador.cerrar_sesion()
        self.manager.current = "menu_inicio"
