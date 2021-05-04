from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty, ListProperty
from kivy.properties import StringProperty

# from kivy.config import Config
from kivy.core.window import Window

import os, sys
import re
from kivy.resources import resource_add_path, resource_find


class ColorButton(Button):
    def __init__(self, **kwargs):
        super(Button, self).__init__(**kwargs)
        self.background_color = [1, 0.2, 0.2, 0.2]

    def update_color(self, color):
        self.background_color = color


class MainScreen(BoxLayout):
    text_input = ObjectProperty()
    kivy_color = StringProperty()
    display = ObjectProperty(ColorButton())

    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.kivy_color = "Enter RGB color"

    def get_kivy_color(self):
        color = self.text_input.text
        color_string = ""
        try:
            color_string = re.findall("[0-9]+", color)
            kivy = []
            for c in color_string[:3]:
                num = int(c)
                if not 0 <= num < 255:
                    raise ValueError("Invalid number")
                val = round((num / 255), 2)
                kivy.append(val)

            if len(color_string) < 3:
                raise ValueError("Invalid number")
            elif len(color_string) > 3:
                last_digit = float(color_string[-1])
                if not 0 <= last_digit <= 1:
                    raise ValueError("Invalid number")
                elif last_digit == 0.0:
                    last_digit = 0
                elif last_digit == 1.0:
                    last_digit = 1
                kivy.append(last_digit)
            else:
                kivy.append(1)
            self.kivy_color = ", ".join(str(x) for x in kivy)
            self.display.background_color = kivy

        except ValueError:
            self.kivy_color = "Invalid RGB entry"


class ColorApp(App):
    # Config.set("graphics", "width", "100")
    # Config.set("graphics", "height", "100")

    def build(self):
        Window.size = (400, 300)
        return MainScreen()


if __name__ == "__main__":
    if hasattr(sys, "_MEIPASS"):
        resource_add_path(os.path.join(sys._MEIPASS))
    ColorApp().run()
