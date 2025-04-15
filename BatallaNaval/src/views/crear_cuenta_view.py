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

        self.add_widget(layout)

    def crear_cuenta(self, instance):
        usuario = self.usuario_input.text
        contraseña = self.contraseña_input.text
        
        # Lógica para crear cuenta
        if usuario and contraseña:
            # Aquí puedes conectar con tu lógica de creación de cuenta
            jugador = Jugador()  # Asumiendo que tienes una clase Jugador
            resultado = jugador.crear_cuenta(usuario, contraseña)  # Cambiar a tu lógica real
            
            if resultado == "Cuenta creada con éxito":
                self.mostrar_popup("✅ Éxito", "Cuenta creada correctamente")
                self.manager.current = "iniciar_sesion"  # Cambiar a la pantalla de inicio de sesión
            else:
                self.mostrar_popup("❌ Error", resultado)
        else:
            self.mostrar_popup("❌ Error", "Por favor, complete todos los campos.")

    def mostrar_popup(self, titulo, mensaje):
        popup = Popup(title=titulo,
                      content=Label(text=mensaje),
                      size_hint=(None, None), size=(300, 200))
        popup.open()
