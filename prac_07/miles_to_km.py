from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class miles_to_km(App):
    def build(self):
        Window.size = (600, 200)
        self.root = Builder.load_file('miles_to_km.kv')
        return self.root

    def convert_miles_to_km(self):
        value = self.get_validated_miles()
        result = value * 1.60934
        self.root.ids.output_label.text = str(result)

    def increment(self, change):
        value = self.get_validated_miles() + change
        self.root.ids.input_miles.text = str(value)
        self.convert_miles_to_km()

    def get_validated_miles(self):
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0


miles_to_km().run()
