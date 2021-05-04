from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
from kivy.config import Config
import os, sys
from kivy.resources import resource_add_path, resource_find

class MainScreen(BoxLayout):
    text_input = ObjectProperty()
    kivy_color = StringProperty()
    display_color = ObjectProperty()

    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.kivy_color = "Enter RGB color"
        self.display_color.background_color = [0.1, 0.5, 0.6]

    def get_kivy_color(self):
        color = self.text_input.text
        color_string = ""
        try:
            if len(color) > 1:
                try:
                    color_string = color[color.find("(")+1:color.find(")")]
                except Exception:
                    color_string = color
            kivy = []
            color_list = color_string.split(",")
            for c in color_list[:3]:
                kivy.append(round((int(c) / 255), 2))

            if len(color_list) > 3:
                kivy.append(color_list[-1])
            else:
                kivy.append(1)

            self.kivy_color = ", ".join(str(x) for x in kivy)
            self.display_color.background_color = kivy
        
        except ValueError:
            self.kivy_color = "Invalid RGB entry"

class ColorApp(App):
    Config.set("graphics", "width", "250")
    Config.set("graphics", "height", "250")

    def build(self):
        return MainScreen()


if __name__ == "__main__":
    if hasattr(sys, '_MEIPASS'):
        resource_add_path(os.path.join(sys._MEIPASS))
    ColorApp().run()