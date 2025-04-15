from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class MenuPrincipalScreen(Screen):
    def __init__(self, **kwargs):
        super(MenuPrincipalScreen, self).__init__(**kwargs)
        
        layout = BoxLayout(orientation='vertical', padding=50, spacing=20)
        
        # Título
        title = Label(text="🎮 Menú Principal", font_size=32, size_hint_y=None, height=60)
        layout.add_widget(title)

        # Botón para iniciar el juego
        btn_jugar = Button(text="Jugar")
        btn_jugar.bind(on_press=self.iniciar_juego)
        layout.add_widget(btn_jugar)

        # Botón para cerrar sesión
        btn_cerrar_sesion = Button(text="Cerrar Sesión")
        btn_cerrar_sesion.bind(on_press=self.cerrar_sesion)
        layout.add_widget(btn_cerrar_sesion)

        self.add_widget(layout)

    def iniciar_juego(self, instance):
        # Lógica para iniciar el juego
        print("Iniciando el juego...")
        self.manager.current = "juego"  # Cambiar a la pantalla de juego

    def cerrar_sesion(self, instance):
        # Lógica para cerrar sesión
        print("Cerrando sesión...")
        self.manager.current = "iniciar_sesion"  # Cambiar a la pantalla de inicio de sesión
