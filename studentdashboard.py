from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window

Window.size = (350, 600)

KV = '''
<DrawerClickableItem@MDNavigationDrawerItem>
    focus_color: "#e7e4c0"
    text_color: "#4a4939"
    icon_color: "#4a4939"
    ripple_color: "#c5bdd2"
    selected_color: "#0c6c4d"


<DrawerLabelItem@MDNavigationDrawerItem>
    text_color: "#4a4939"
    icon_color: "#4a4939"
    focus_behavior: False
    selected_color: "#4a4939"
    _no_ripple_effect: True


MDScreen:

    MDNavigationLayout:

        MDScreenManager:

            MDScreen:

                MDTopAppBar:
                    title: "Student Dashboard"
                    elevation: 4
                    pos_hint: {"top": 1}
                    md_bg_color: "#e7e4c0"
                    specific_text_color: "#4a4939"
                    left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]

        MDNavigationDrawer:
            id: nav_drawer
            radius: (0, 16, 16, 0)

            MDNavigationDrawerMenu:

                MDNavigationDrawerHeader:
                    title: "Student Dashboard"
                    title_color: "#4a4939"

                DrawerClickableItem:
                    icon: "account"
                    text_right_color: "#4a4939"
                    text: "Profile"

                DrawerClickableItem:
                    icon: "information"
                    text: "Class Details"

                DrawerClickableItem:
                    icon: "pen"
                    text: "Registration Details" 

                DrawerClickableItem:
                    icon: "map"
                    text: "Location" 

                DrawerClickableItem:
                    icon: "bell"
                    text: "Notifications"

                DrawerClickableItem:
                    icon: "message"
                    text: "Chat"             

                DrawerClickableItem:
                    icon: "lightbulb-on"
                    text: "Class Suggestion"         

                MDNavigationDrawerDivider:

                DrawerLabelItem:
                    icon: "cog"
                    text: "Settings"

                DrawerLabelItem:
                    icon: "logout"
                    text: "Logout"    
'''


class MainApp(MDApp):
    def build(self):
        self.title = 'Class Check-in'
        self.theme_cls.theme_style = "Dark"
        return Builder.load_string(KV)


MainApp().run()