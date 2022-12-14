from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.utils import platform
from kivy.properties import BooleanProperty
from kivy.core.audio import SoundLoader
from plyer import gps



class põhiekraan(BoxLayout):
    tekst=StringProperty('sisesta kordinaadid formaadis: *****, *****')
    sisestus=''
    tekstenable=BooleanProperty(True)

    def on_toggle(self, widget):
        if widget.state == 'normal':
            self.textenable=True
        else:
            try:
                self.sisestus=self.ids.myinput.text.split(', ')
                self.sisestus=[float(x) for x in self.sisestus]
                self.tekstenable=False
                self.alusta()
            except:
                self.sisestus=''
                self.tekstenable=True
                self.tekst='Vales formaadis, sisesta kordinaadid formaadis: *****, *****'
                widget.state='normal'

    def alusta(self):
        if platform == 'android':
            gps.configure(on_location=self.võrdle)
            gps.start()
        else:
            self.tekst='sellel masinal pole gps moodulit'
    
    
    def võrdle(self, **kwargs):
        self.tekst=str(kwargs['lat'])+str(kwargs['lon'])
        if self.sisestus[0]-0.001<=kwargs['lat'] and kwargs['lat']<=self.sisestus[0]+0.001 and self.sisestus[1]-0.001<=kwargs['lon'] and kwargs['lon']<=self.sisestus[1]-0.001:
            gps.stop()
            sound=SoundLoader.load('alarm.mp3')
            sound.play()
            





class gpsApp(App):
    def on_start(self):
        if platform == 'android':
            from android.permissions import Permission, request_permissions
            request_permissions([Permission.ACCESS_COARSE_LOCATION, Permission.ACCESS_FINE_LOCATION, Permission.INTERNET, Permission.VIBRATE])
        else:
            pass



         
    def build(self):
        return põhiekraan()
    
    


if __name__ == '__main__':
    gpsApp().run()