from kivy.app import App
from kivy.app import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.properties import NumericProperty
from kivy.uix.video import Video
from kivy.uix.videoplayer import VideoPlayer

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
    
    intentos = NumericProperty(1)
    
    def check(self, label_password, input_password):
        
        self.password = input_password.text
        label_password.text = "ingresa el código"

        if self.password == "143":
            self.intentos = 3
            input_password.text = " "
            print("contraseña correcta")
            self.manager.current = "correcto"
        else:
            print(f'error, intento {self.intentos}/3')
            self.intentos += 1
            if self.intentos > 3:
                self.manager.current = 'error'



    


class correcto(Screen):
    pass

class error(Screen):
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