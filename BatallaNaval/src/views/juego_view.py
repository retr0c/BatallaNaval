from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class JuegoScreen(Screen):
    def __init__(self, **kwargs):
        super(JuegoScreen, self).__init__(**kwargs)
        
        layout = BoxLayout(orientation='vertical', padding=50, spacing=20)
        
        # Título de la pantalla
        title = Label(text="⚔️ Juego en Progreso", font_size=32, size_hint_y=None, height=60)
        layout.add_widget(title)

        # Botón para salir del juego
        btn_salir = Button(text="Salir del Juego")
        btn_salir.bind(on_press=self.salir_juego)
        layout.add_widget(btn_salir)

        self.add_widget(layout)

    def salir_juego(self, instance):
        # Lógica para salir del juego
        print("Saliendo del juego...")
        self.manager.current = "menu_principal"  # Cambiar a la pantalla de menú principal
