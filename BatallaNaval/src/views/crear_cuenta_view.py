# src/views/crear_cuenta_view.py
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from src.Jugador import Jugador

class CrearCuentaScreen(Screen):
    username_input = ObjectProperty(None)
    password_input = ObjectProperty(None)
    confirm_password_input = ObjectProperty(None)
    status_label = ObjectProperty(None)
    
    def crear_cuenta(self):
        username = self.username_input.text
        password = self.password_input.text
        confirm_password = self.confirm_password_input.text
        
        if password != confirm_password:
            self.status_label.text = "Las contraseñas no coinciden"
            return
        
        # Lógica para crear cuenta
        jugador = Jugador()
        resultado = jugador.crear_cuenta(username, password)
        
        if resultado:
            self.status_label.text = "Cuenta creada correctamente"
            self.manager.current = 'iniciar_sesion'
        else:
            self.status_label.text = "Error al crear la cuenta"
    
    def volver_menu(self):
        self.manager.current = 'menu_principal'