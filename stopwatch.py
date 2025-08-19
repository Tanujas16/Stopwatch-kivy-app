from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock

class MyApp(App):
    def build(self):
        self.min = 0
        self.sec = 0
        self.ms = 0
        self.go = False

        self.box = BoxLayout(orientation='vertical')

        self.time = Label(text='00:00:00', font_size=40)
        self.box.add_widget(self.time)

        self.btn1 = Button(text='Start')
        self.btn1.bind(on_press=self.start)
        self.box.add_widget(self.btn1)

        self.btn2 = Button(text='Pause')
        self.btn2.bind(on_press=self.pause)
        self.box.add_widget(self.btn2)

        self.btn3 = Button(text='Reset')
        self.btn3.bind(on_press=self.reset)
        self.box.add_widget(self.btn3)

        return self.box

    def run_time(self, dt):
        if self.go:
            self.ms += 1
            if self.ms == 100:
                self.ms = 0
                self.sec += 1
            if self.sec == 60:
                self.sec = 0
                self.min += 1
            self.time.text = f'{self.min:02}:{self.sec:02}:{self.ms:02}'

    def start(self, instance):
        if not self.go:
            self.go = True
            Clock.schedule_interval(self.run_time, 0.01)

    def pause(self, instance):
        self.go = False
        Clock.unschedule(self.run_time)

    def reset(self, instance):
        self.go = False
        Clock.unschedule(self.run_time)
        self.min = 0
        self.sec = 0
        self.ms = 0
        self.time.text = '00:00:00'

MyApp().run()

