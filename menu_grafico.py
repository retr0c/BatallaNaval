from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager

from BatallaNaval.src.views.menu_kivy_controller import (
    MenuInicio, CrearCuenta, IniciarSesion, MenuPrincipal
)

# Cargamos todas las pantallas
Builder.load_file("BatallaNaval/src/views/screens.kv")

class BatallaNavalApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MenuInicio(name="menu_inicio"))
        sm.add_widget(CrearCuenta(name="crear_cuenta"))
        sm.add_widget(IniciarSesion(name="iniciar_sesion"))
        sm.add_widget(MenuPrincipal(name="menu_principal"))
        return sm

if __name__ == "__main__":
    BatallaNavalApp().run()
