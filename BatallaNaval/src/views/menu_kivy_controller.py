from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, FadeTransition
from kivy.lang import Builder
import os
from BatallaNaval.src.views.iniciar_sesion_view import IniciarSesionScreen
from BatallaNaval.src.views.crear_cuenta_view import CrearCuentaScreen
from BatallaNaval.src.views.menu_principal_view import MenuPrincipalScreen
from BatallaNaval.src.views.juego_view import JuegoScreen

# Ruta al archivo KV
KV_PATH = os.path.join(os.path.dirname(__file__), "screens.kv")

# Clase principal del ScreenManager
class GestorPantallas(ScreenManager):
    pass

# Clase de la aplicación
class BatallaNavalApp(App):
    def build(self):
        Builder.load_file(KV_PATH)
        sm = GestorPantallas(transition=FadeTransition())
        sm.add_widget(IniciarSesionScreen(name='iniciar_sesion'))
        sm.add_widget(CrearCuentaScreen(name='crear_cuenta'))
        sm.add_widget(MenuPrincipalScreen(name='menu_principal'))
        sm.add_widget(JuegoScreen(name='juego'))
        return sm

# Función para iniciar la aplicación
def iniciar_aplicacion():
    BatallaNavalApp().run()
