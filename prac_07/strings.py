from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty


class strings(App):

    status_text = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.strings = ["Dog", "Cat", "Horse"]

    def build(self):
        self.title = "strings"
        self.root = Builder.load_file('strings.kv')
        return self.root

    def strings_text(self):
        for string in self.strings:
            self.status_text = string


strings().run()