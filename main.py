from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import BooleanProperty, StringProperty

from plyer import gps
 

class põhiline(BoxLayout):
    textenable=BooleanProperty(True)
    tekst=''
    def toggled(self, widget):
        if widget.state == 'normal':
            self.textenable=True
        else:
            self.tekst=self.ids.myinput.text.split(', ')
            self.tekst=[float(x) for x in self.tekst]
            self.textenable=False
            print(self.tekst)
            self.alusta
    def alusta(self):
        gps.configure(on_location=self.võrdlus)
        gps.start()

    def võrdlus(self, **kwargs):
        if (self.tekst[0]-0.0001<=kwargs['lat']<=self.tekst[0]+0.0001) and (self.tekst[1]-0.0001<=kwargs['lon']<=self.tekst[1]-0.0001):
            #siia pane alarm
            pass
        else:
            pass

    

        


         
    
class gpsApp(App):
    pass


gpsApp().run()