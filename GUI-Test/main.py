# use kivy to build the gui
from kivy.app import App
# from kivy.uix.boxlayout import BoxLayout
from more_itertools import sample
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, WipeTransition



# Caricare file stile con nomi diversi da quello de lpile pytohn
kv = Builder.load_file("style.kv")

class MyPopup(Popup):
    send_form = ObjectProperty(None)

    def dismiss_popup(self):
        self.dismiss()


class MainWindow(Screen):
    sub = ObjectProperty(None)
    
    def pop_form(self):
        custom_popup = MyPopup(title='Confirm submission', size_hint=(0.5, 0.25), size = (400, 800), send_form=self.send_form)
        custom_popup.open()

    def send_form(self):
        form = open("/home/ale/Scrivania/form.txt", "w+")
        form.write("Nome: " + self.input_name.text + "\n" + 
                   "Cognome: " + self.input_surname.text + "\n" + 
                   "Città: " + self.input_city.text + "\n" +  
                   "Data: " + self.input_day.text + "/"+ self.input_month+ "/"+ self.input_year + "\n" +
                   "Job: " + self.input_job.text + "\n" )

        sm.switch_to(screens[1], direction='left')



class SecondWindow(Screen):
    def go_back(self):
                sm.switch_to(screens[0], direction='right')
    pass

class WindowManager(ScreenManager):
    pass


sm = WindowManager()
screens = [MainWindow(name='main'), SecondWindow(name='second')]
for screen in screens:
    sm.add_widget(screen)
sm.current = 'main'




class MainApp(App):
    def build(self):
        return sm

sample_app = MainApp()
sample_app.run()



