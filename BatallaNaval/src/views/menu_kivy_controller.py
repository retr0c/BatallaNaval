# BatallaNaval/src/views/menu_kivy_controller.py

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, FadeTransition
from kivy.lang import Builder
import os

KV_PATH = os.path.join(os.path.dirname(__file__), "screens.kv")

class GestorPantallas(ScreenManager):
    pass

class BatallaNavalApp(App):
    def build(self):
        Builder.load_file(KV_PATH)
        sm = GestorPantallas(transition=FadeTransition())
        return sm

def iniciar_aplicacion():
    BatallaNavalApp().run()
