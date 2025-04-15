from kivy.uix.screenmanager import Screen
from kivy.uix.popup import Popup
from kivy.uix.label import Label

class MenuPrincipalScreen(Screen):
    def iniciar_juego(self):
        self.manager.current = "juego"

    def cambiar_contraseña(self):
        # Suponemos que tienes un TextInput con id 'new_password_input' en la vista
        nueva_contraseña = self.ids.new_password_input.text if "new_password_input" in self.ids else ""
        if nueva_contraseña:
            jugador = self.manager.get_screen("iniciar_sesion").jugador
            resultado = jugador.cambiar_contraseña(nueva_contraseña)
            self.mostrar_popup("Cambio Contraseña", resultado)
        else:
            self.mostrar_popup("Error", "Ingresa una nueva contraseña.")

    def cerrar_sesion(self):
        jugador = self.manager.get_screen("iniciar_sesion").jugador
        jugador.cerrar_sesion()
        self.manager.current = "iniciar_sesion"

    def mostrar_popup(self, titulo, mensaje):
        popup = Popup(title=titulo, content=Label(text=mensaje),
                      size_hint=(None, None), size=(300, 200))
        popup.open()
