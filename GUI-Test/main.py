#use kivy to build the gui
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from more_itertools import sample

class MainWindow(BoxLayout):
    pass


class MainApp(App):
    def build(self):
        return MainWindow()

sample_app = MainApp()
sample_app.run()