from kivy.uix.screenmanager import Screen
from BatallaNaval.src.Jugador import Jugador
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.app import App

class IniciarSesionScreen(Screen):
    def iniciar_sesion(self):
        usuario = self.ids.usuario_input.text
        contraseña = self.ids.contraseña_input.text
        jugador = Jugador()
        resultado = jugador.iniciar_sesion(usuario, contraseña)

        if resultado == "Sesión iniciada":
            # Guardamos el jugador en la App para accederlo desde otras pantallas
            App.get_running_app().jugador = jugador

            self.mostrar_popup("✅ Éxito", "Sesión iniciada correctamente")
            self.manager.current = "menu_principal"
        else:
            self.mostrar_popup("❌ Error", resultado)

    def mostrar_popup(self, titulo, mensaje):
        popup = Popup(title=titulo,
                      content=Label(text=mensaje),
                      size_hint=(None, None), size=(300, 200))
        popup.open()
