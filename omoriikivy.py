from kivy.app import App
from kivy.app import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.uix.button import Button

class Inicio(Screen):
    pass

class pantalla1(Screen):
    pass

class pantalla2(Screen):
    i = 0
    limite = False

    def clicks(self):
        self.i += 1
        print(self.i)
        if self.i == 5:
            print("llegaste a 5 clicks")
            limite = True
            self.manager.current = "password"
            self.manager.transition.direction = "right"

class password(Screen):
    pass

class correcto(Screen):
    pass


class Fade(Screen):
    opacidad = 1
    def fade(self):

        for i in range(0,1):
            self.opacidad -= 0.1
            print("opacidad =", self.opacidad)

 

class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("omoriclase.kv")

class omoriiapp(App):
    Window.size = (600, 400)

    def build(self):
        return kv
    
    def iniciar(self):
        print("bienvenido")






if __name__ == "__main__":
    omoriiapp().run()