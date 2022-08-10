#use kivy to build the gui
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from more_itertools import sample
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup


class MyPopup(Popup):
    send_form = ObjectProperty(None)

    def dismiss_popup(self):
        self.dismiss()


class MainWindow(BoxLayout):
    sub = ObjectProperty(None)
    
    def pop_form(self):
        custom_popup = MyPopup(title='Confirm submission', size_hint=(0.5, 0.25), size = (400, 800), send_form=self.send_form)
        custom_popup.open()

    def send_form(self):
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
