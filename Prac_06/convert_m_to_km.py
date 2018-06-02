from kivy.app import App
from kivy.lang import Builder


class ConvertMilesToKilometersApp(App):
    def build(self):
        """ build the Kivy app from the kv file """
        self.title = "Convert Miles To Kilometers"
        self.root = Builder.load_file('convert_m_to_km.kv')
        return self.root


ConvertMilesToKilometersApp().run()
