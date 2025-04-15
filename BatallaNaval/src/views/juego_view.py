from kivy.uix.screenmanager import Screen
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from BatallaNaval.src.Juego import Juego
from BatallaNaval.src.Jugador import Jugador

class JuegoScreen(Screen):
    def __init__(self, **kwargs):
        super(JuegoScreen, self).__init__(**kwargs)
        self.juego = None
        self.campo = None
        self.score = 0
        self.jugador = None

    def iniciar_juego(self):
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

        # Verificar si quedan naves (celdas con 1)
        game_over = True
        for row in self.campo:
            if 1 in row:
                game_over = False
                break
        if game_over:
            self.mostrar_popup("Fin del Juego", f"¡Has hundido todas las naves!\nPuntuación final: {self.score}")
            self.manager.current = "menu_principal"

    def mostrar_campo(self):
        campo_str = ""
        for row in self.campo:
            line = ""
            for celda in row:
                if celda == "X":
                    line += " X "
                elif celda == 1:
                    line += " ~ "
                else:
                    line += " ~ "
            campo_str += line + "\n"
        
        self.ids.campo_label.markup = False
        self.ids.campo_label.text = campo_str
        
    def salir_juego(self):
        self.manager.current = "menu_principal"

    def mostrar_popup(self, titulo, mensaje):
        popup = Popup(title=titulo, content=Label(text=mensaje),
                      size_hint=(None, None), size=(300, 200))
        popup.open()
