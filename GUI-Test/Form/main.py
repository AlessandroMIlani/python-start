from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, WipeTransition

# Gestione Popup
class MyPopup(Popup):
    send_form = ObjectProperty(None)

    def dismiss_popup(self):
        self.dismiss()

# Gestione Schermata Principale
class MainWindow(Screen):
    sub = ObjectProperty(None)
    
    def pop_form(self):
        custom_popup = MyPopup(title='Confirm submission', size_hint=(0.5, 0.25), size = (400, 800), send_form=self.send_form)
        custom_popup.open()

    def send_form(self):
        licenses = ""
        form = open("/home/ale/Scrivania/form.txt", "w+")
        form.write("Nome: "    + self.input_name.text + "\n" + 
                   "Cognome: " + self.input_surname.text + "\n" + 
                   "Città: "   + self.input_city.text + "\n" +  
                   "Data: "    + self.input_day.text + "-" + self.input_month.text + "-" + self.input_year.text + "\n" +
                   "Job: "     + self.input_job.text + "\n" )
        if self.license_a.active:
            licenses += "License A "
        if self.license_b.active:
            licenses += "License B "
        if self.license_c.active:
            licenses += "License C "
        form.write("Licenses: " + licenses + "\n")
        sm.switch_to(screens[1], direction='left')


# Gestione Schermata Secondaria
class SecondWindow(Screen):
    def go_back(self):
                sm.switch_to(screens[0], direction='right')
    pass

# Windows Manager per gestire le diverse schermate
class WindowManager(ScreenManager):
    pass

# Creazione App
class MainApp(App):
    def build(self):
        return sm


# Caricare file stile con nomi diversi da quello de lpile pytohn
kv = Builder.load_file("style.kv")

sm = WindowManager()
sample_app = MainApp()
screens = [MainWindow(name='main'), SecondWindow(name='second')]

for screen in screens:
    sm.add_widget(screen)
sm.current = 'main'


sample_app.run()



