from kivy.app import App
from kivy.lang import Builder

M_TO_KM = 1.60934


class ConvertMilesToKilometersApp(App):

    def build(self):
        """ build the Kivy app from the kv file """
        self.title = "Convert Miles To Kilometers"
        self.root = Builder.load_file('convert_m_to_km.kv')
        return self.root

    def handle_convert(self):
        value = self.get_input_miles()
        converted_result = value * M_TO_KM
        print(converted_result)
        self.root.ids.answer_label.text = str(converted_result)

    def handle_increment(self, increment):
        value = self.get_input_miles() + increment
        self.root.ids.input_miles.text = str(value)
        pass

    def get_input_miles(self):
        value = float(self.root.ids.input_miles.text)
        return value


ConvertMilesToKilometersApp().run()
