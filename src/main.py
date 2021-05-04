from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
from kivy.config import Config

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
                    print(color_string)
                except Exception:
                    color_string = color
            print(color_string)
            kivy = []
            for c in color_string.split(","):
                print(c)
                kivy.append(round((int(c) / 255), 2))
            print(kivy)
            if len(kivy) == 3:
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
    ColorApp().run()