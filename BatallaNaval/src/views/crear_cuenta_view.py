from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from BatallaNaval.src.Jugador import Jugador

class CrearCuentaScreen(Screen):
    def __init__(self, **kwargs):
        super(CrearCuentaScreen, self).__init__(**kwargs)
        
        layout = BoxLayout(orientation='vertical', padding=50, spacing=20)
        
        # Título
        title = Label(text="📝 Crear Cuenta", font_size=32, size_hint_y=None, height=60)
        layout.add_widget(title)

        # Campos de texto
        self.usuario_input = TextInput(hint_text="Nuevo Usuario", multiline=False)
        self.contraseña_input = TextInput(hint_text="Contraseña", password=True, multiline=False)
        
        layout.add_widget(self.usuario_input)
        layout.add_widget(self.contraseña_input)

        # Botón para crear cuenta
        btn_crear = Button(text="Crear Cuenta")
        btn_crear.bind(on_press=self.crear_cuenta)
        layout.add_widget(btn_crear)

        # Botón para volver a iniciar sesión (ahora con una función dedicada)
        btn_volver = Button(text="Volver a Iniciar Sesión")
        btn_volver.bind(on_press=self.volver_a_iniciar_sesion)
        layout.add_widget(btn_volver)

        self.add_widget(layout)

    def crear_cuenta(self, instance):
        usuario = self.usuario_input.text
        contraseña = self.contraseña_input.text
        
        # Lógica para crear cuenta
        if usuario and contraseña:
            # Utilizamos la instancia de Jugador que ya tengamos en la pantalla de iniciar sesión
            # Esto asume que la pantalla de iniciar sesión tiene un atributo 'jugador'
            jugador = self.manager.get_screen("iniciar_sesion").jugador  
            resultado = jugador.crear_cuenta(usuario, contraseña)
            if resultado == "Cuenta creada exitosamente":
                self.mostrar_popup("✅ Éxito", "Cuenta creada correctamente")
                self.manager.current = "iniciar_sesion"  # Cambiar a la pantalla de inicio de sesión
            else:
                self.mostrar_popup("❌ Error", resultado)
        else:
            self.mostrar_popup("❌ Error", "Por favor, complete todos los campos.")

    def volver_a_iniciar_sesion(self, instance):
        self.manager.current = "iniciar_sesion"

    def mostrar_popup(self, titulo, mensaje):
        popup = Popup(title=titulo,
                      content=Label(text=mensaje),
                      size_hint=(None, None), size=(300, 200))
        popup.open()
