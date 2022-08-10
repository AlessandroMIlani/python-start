#use kivy to build the gui
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from more_itertools import sample
from kivy.properties import ObjectProperty


class MainWindow(BoxLayout):
    sub = ObjectProperty(None)
    


    def send_form(self):
        self.sub.text = "Sended!"
        form = open("/home/ale/Scrivania/form.txt", "w+")
        form.write("Nome: " + self.input_name.text + "\n" + 
                   "Cognome: " + self.input_surname.text + "\n" + 
                   "Città: " + self.input_city.text + "\n" +  
                   "Data: " + self.input_age.text + "\n")


class MainApp(App):
    def build(self):
        return MainWindow()

sample_app = MainApp()
sample_app.run()
