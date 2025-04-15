from kivy.uix.screenmanager import Screen
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from BatallaNaval.src.Jugador import Jugador

class IniciarSesionScreen(Screen):
    # Para facilitar la comunicación, guardaremos el jugador en la pantalla de inicio de sesión
    def __init__(self, **kwargs):
        super(IniciarSesionScreen, self).__init__(**kwargs)
        self.jugador = Jugador()  # Instancia global del jugador

    def iniciar_sesion(self, usuario, contraseña):
        print(f"Intentando iniciar sesión:\nUsuario: {usuario}\nContraseña: {contraseña}")
        resultado = self.jugador.iniciar_sesion(usuario, contraseña)
        if resultado == "Sesión iniciada":
            self.manager.current = "menu_principal"
        else:
            self.mostrar_popup("Error", resultado)

    def mostrar_popup(self, titulo, mensaje):
        popup = Popup(title=titulo,
                      content=Label(text=mensaje),
                      size_hint=(None, None), size=(300, 200))
        popup.open()
