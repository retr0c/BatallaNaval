from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from BatallaNaval.src.Jugador import Jugador

Builder.load_file("BatallaNaval/src/views/screens.kv")

# Pantallas básicas
class MenuInicio(Screen):
    pass

class CrearCuenta(Screen):
    def crear_cuenta(self):
        usuario = self.ids.usuario_input.text
        contraseña = self.ids.contraseña_input.text
        jugador = App.get_running_app().jugador
        resultado = jugador.crear_cuenta(usuario, contraseña)
        self.ids.resultado.text = resultado

class IniciarSesion(Screen):
    def iniciar_sesion(self):
        usuario = self.ids.usuario_login.text
        contraseña = self.ids.contraseña_login.text
        jugador = App.get_running_app().jugador
        resultado = jugador.iniciar_sesion(usuario, contraseña)
        self.ids.resultado_login.text = resultado
        if resultado == "Sesión iniciada":
            self.manager.current = "menu_principal"

class MenuPrincipal(Screen):
    def cerrar_sesion(self):
        jugador = App.get_running_app().jugador
        jugador.cerrar_sesion()
        self.manager.current = "menu_inicio"

# Controlador de pantallas
class GestorPantallas(ScreenManager):
    pass

# Aplicación principal
class BatallaNavalApp(App):
    def build(self):
        self.jugador = Jugador()
        sm = GestorPantallas()
        sm.add_widget(MenuInicio(name="menu_inicio"))
        sm.add_widget(CrearCuenta(name="crear_cuenta"))
        sm.add_widget(IniciarSesion(name="iniciar_sesion"))
        sm.add_widget(MenuPrincipal(name="menu_principal"))
        return sm

if __name__ == "__main__":
    BatallaNavalApp().run()
