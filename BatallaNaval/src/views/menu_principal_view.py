from kivy.uix.screenmanager import Screen
from kivy.uix.popup import Popup
from kivy.uix.label import Label

class MenuPrincipalScreen(Screen):
    """
    Pantalla del menú principal del juego.
    Permite iniciar partida, cambiar contraseña o cerrar sesión.
    """

    def iniciar_juego(self):
        """
        Navega a la pantalla del juego.
        """
        self.manager.current = "juego"

    def cambiar_contraseña(self):
        """
        Cambia la contraseña del jugador actual.
        """
        nueva_contraseña = self.ids.new_password_input.text if "new_password_input" in self.ids else ""
        if nueva_contraseña:
            jugador = self.manager.get_screen("iniciar_sesion").jugador
            resultado = jugador.cambiar_contraseña(nueva_contraseña)
            self.mostrar_popup("Cambio Contraseña", resultado)
        else:
            self.mostrar_popup("Error", "Ingresa una nueva contraseña.")

    def cerrar_sesion(self):
        """
        Cierra la sesión actual y regresa al inicio.
        """
        jugador = self.manager.get_screen("iniciar_sesion").jugador
        jugador.cerrar_sesion()
        self.manager.current = "iniciar_sesion"

    def mostrar_popup(self, titulo, mensaje):
        """
        Muestra un popup informativo o de error.
        """
        popup = Popup(title=titulo,
                      content=Label(text=mensaje),
                      size_hint=(None, None), size=(300, 200))
        popup.open()
