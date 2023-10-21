from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
Window.size = (450, 500)

LoginPage = """
MDFloatLayout:
    MDLabel:
        text: "Login"
        pos_hint: {"center_y": .85}
        font_style: "H4"
        halign: "center"
        theme_text_color: "Custom"
        text_color: 0, 0, 0, 1
    MDTextField:
        id: email
        hint_text: "Enter Your Email"
        pos_hint: {"center_x": .5, "center_y": .6}
        current_hint_text_color: 0, 0, 0, 1
        size_hint_x: .8
    MDTextField:
        id: password
        hint_text: "Password"
        pos_hint: {"center_x": .5, "center_y": .5}
        current_hint_text_color: 0, 0, 0, 1
        size_hint_x: .8
        password: True 
    MDRaisedButton:
        text: "Log in"
        pos_hint: {"center_x": .5, "center_y": .25}
        size_hint_x: .5
        on_release: app.verify(email.text, password.text)
        theme_text_color: "Custom"
        text_color: 0, 0, 0, 1 
    MDRaisedButton:
        text: "Don't have an account? Sign Up"
        pos_hint: {"center_x": .5, "center_y": .1}
        size_hint_x: .6
        on_release: app.go_to_signup() 
        theme_text_color: "Custom"
        text_color: 0, 0, 0, 1    
"""

class Tutorial(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Red"
        login_page = Builder.load_string(LoginPage)
        return login_page
    
    def verify(self, email, password):
        if email == "" and password == "":
            print("Successful Login")

if __name__ == "__main__":
    Tutorial().run()