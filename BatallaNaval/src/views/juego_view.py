from kivy.uix.screenmanager import Screen
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from BatallaNaval.src.Juego import Juego
from BatallaNaval.src.Jugador import Jugador

class JuegoScreen(Screen):
    """
    Pantalla del juego principal de Batalla Naval.
    Permite configurar el campo, disparar, mostrar el campo y puntuar.
    """
    def __init__(self, **kwargs):
        super(JuegoScreen, self).__init__(**kwargs)
        self.juego = None
        self.campo = None
        self.score = 0
        self.jugador = None

    def iniciar_juego(self):
        """
        Inicializa el campo de batalla con los parámetros dados por el usuario.
        """
        try:
            ancho = int(self.ids.ancho_input.text)
            alto = int(self.ids.alto_input.text)
            naves = int(self.ids.naves_input.text)
        except ValueError:
            self.mostrar_popup("Error", "Debe ingresar números válidos.")
            return

        self.juego = Juego()
        self.campo = self.juego.iniciar_campo_juego(ancho, alto, naves)
        self.score = 0
        self.jugador = self.manager.get_screen("iniciar_sesion").jugador
        self.mostrar_popup("Juego Iniciado", "Campo de batalla generado. ¡Comienza el juego!")
        self.mostrar_campo()

    def disparar(self):
        """
        Realiza un disparo en la posición indicada por el usuario y actualiza el campo.
        """
        try:
            fila = int(self.ids.fila_input.text) - 1
            columna = int(self.ids.columna_input.text) - 1
        except ValueError:
            self.mostrar_popup("Error", "Ingrese números válidos para fila y columna.")
            return

        if not self.campo:
            self.mostrar_popup("Error", "No se ha iniciado el juego.")
            return

        try:
            resultado = self.juego.disparar(self.campo, fila, columna)
        except IndexError:
            self.mostrar_popup("Error", "Coordenadas fuera de rango.")
            return

        if resultado == "¡Impacto!":
            self.score += 10
        elif resultado == "Agua":
            self.score -= 2

        self.mostrar_popup("Resultado", f"{resultado}\nPuntuación: {self.score}")
        self.mostrar_campo()
        self.verificar_fin_juego()

    def mostrar_campo(self):
        """
        Muestra el campo de batalla en el label correspondiente.
        """
        campo_str = ""
        for row in self.campo:
            line = ""
            for celda in row:
                if celda == "X":
                    line += " X "
                else:
                    line += " ~ "
            campo_str += line + "\n"

        self.ids.campo_label.markup = False
        self.ids.campo_label.text = campo_str

    def verificar_fin_juego(self):
        """
        Verifica si todas las naves han sido hundidas y finaliza el juego si es así.
        """
        for row in self.campo:
            if 1 in row:
                return  # Aún quedan naves

        self.mostrar_popup("Fin del Juego", f"¡Has hundido todas las naves!\nPuntuación final: {self.score}")
        self.manager.current = "menu_principal"

    def salir_juego(self):
        """
        Regresa al menú principal.
        """
        self.manager.current = "menu_principal"

    def mostrar_popup(self, titulo, mensaje):
        """
        Muestra un popup con un mensaje.
        """
        popup = Popup(title=titulo, content=Label(text=mensaje),
                      size_hint=(None, None), size=(300, 200))
        popup.open()
