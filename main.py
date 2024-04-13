import kivy

from kivy.app import App
from kivy.uix.label import Label
# from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.pagelayout import PageLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.graphics import *
from kivy.graphics.transformation import Matrix


class UserInput(BoxLayout):
    def __init__(self, **kwargs):
        super(UserInput, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.text = Label(text='How many steps did you take today?')
        self.add_widget(self.text)
        self.stepCountInput = TextInput(multiline=False, size_hint=(1,.25))
        self.add_widget(self.stepCountInput)
        # self.text.bind()
        self.stepCountInput.bind(on_text_validate=self.checkStepCount)

    def checkStepCount(self, instance):
        # print(text)
        if int(instance.text) < 2000:
            self.text.text = "Uh oh! That was a poor decision..."
        else:
            self.text.text = "Gooooood~~"

class Punishments(RelativeLayout):
    def __init__(self, **kwargs):
        super(Punishments, self).__init__(**kwargs)
        # self.pos = (-1,-1)
        # self.size = (1000,1000)
        with self.canvas:
            Color(1., 0, 0)
            Rectangle(pos=(10,10), size=(50,50))

class FlipPages(PageLayout):
    def __init__(self, **kwargs):
        super(FlipPages, self).__init__(**kwargs)
        page1 = Punishments()
        page2 = UserInput()

        self.add_widget(page1)
        self.add_widget(page2)

class MyApp(App):

    def build(self):
        return FlipPages()
    
if __name__ == '__main__':
    MyApp().run()