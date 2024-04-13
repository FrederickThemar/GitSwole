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
from kivy.core.window import Window


class UserInput(BoxLayout):
    def __init__(self, **kwargs):
        super(UserInput, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.text = Label(text='How many steps did you take today?')
        self.add_widget(self.text)
        self.stepCountInput = TextInput(multiline=False, size_hint=(1,.25))
        self.add_widget(self.stepCountInput)
        self.text.bind()
        self.stepCountInput.bind(on_text_validate=self.checkStepCount)
        self.missed = 0

    def checkStepCount(self, instance):
        hotdog = ['hi', 'lo', 'deez', 'nuts']
        if int(instance.text) < 2000:
            # Use a lambda function inside the formatted string to output each item in the list hotdog along with its index followed by a new line
            self.missed += 1
            self.text.text = f"Uh oh! That was a poor decision. You have missed {self.missed} goals. \nNow you must choose...\n" + ''.join(map(lambda x: f'Message {x[0] + 1}: {x[1]}\n', enumerate(hotdog))) + "\nChoose a message to send, you naughty little slacker."
        else:
            self.text.text = "Gooooood~~"

class Punishments(RelativeLayout):
    def __init__(self, **kwargs):
        super(Punishments, self).__init__(**kwargs)
        # self.pos = (-1,-1)
        # self.size = (1000,1000)
        center_x = 0.5 * int(Window.size[0])
        with self.canvas:
            # print(Window.size[0])
            Color(1., 0, 0)
            # Rectangle(pos=(center_x+(75/1.5),15), size=(50,750))
            Rectangle(pos=(center_x+(75/1.5),15), size=(50,150)) # Cover the circle
            for i in range(UserInput.missed):
                y = 15 + 150 + (i*60) # Calculate y value of rectangle
                Rectangle(pos=(center_x+(75/1.5),y), size=(50,60))
            Ellipse(3, pos=(center_x,10), size=(150,150))
        # self.lv1 = Label(text="Lv1", pos=(100, 500))
        # self.add_widget(self.lv1)

class FlipPages(PageLayout):
    def __init__(self, **kwargs):
        super(FlipPages, self).__init__(**kwargs)
        page1 = UserInput()
        page2 = Punishments()

        self.add_widget(page1)
        self.add_widget(page2)

class MyApp(App):

    def build(self):
        return FlipPages()
    
if __name__ == '__main__':
    MyApp().run()