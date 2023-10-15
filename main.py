from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window

Window.size = (350, 600)

class MainApp(MDApp):
    def build(self):
        self.title='Class Check-in'
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "DeepPurple"


MainApp().run()
