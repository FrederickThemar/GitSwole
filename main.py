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
from kivy.clock import Clock


class UserInput(BoxLayout):
    missed = 0
    def __init__(self, **kwargs):
        super(UserInput, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.text = Label(text='How many steps did you take today?')
        self.add_widget(self.text)
        self.stepCountInput = TextInput(multiline=False, size_hint=(1,.25))
        self.add_widget(self.stepCountInput)
        self.text.bind()
        self.stepCountInput.bind(on_text_validate=self.checkStepCount)

    def checkStepCount(self, instance):
        hotdog = ['hi', 'lo', 'deez', 'nuts']
        if int(instance.text) < 2000:
            # Use a lambda function inside the formatted string to output each item in the list hotdog along with its index followed by a new line
            UserInput.missed += 1
            self.text.text = f"Uh oh! That was a poor decision. You have missed {self.missed} goals. \nNow you must choose...\n" + ''.join(map(lambda x: f'Message {x[0] + 1}: {x[1]}\n', enumerate(hotdog))) + "\nChoose a message to send, you naughty little slacker."
        else:
            self.text.text = "Gooooood~~"

class Punishments(RelativeLayout):
    center_x = 0.5 * int(Window.size[0])
    def __init__(self, **kwargs):
        super(Punishments, self).__init__(**kwargs)
        # self.pos = (-1,-1)
        # self.size = (1000,1000)
        with self.canvas:
            # print(Window.size[0])
            Color(1., 0, 0)
            Ellipse(3, pos=(self.center_x,10), size=(150,150))
            # Rectangle(pos=(center_x+(75/1.5),15), size=(50,750))
            Rectangle(pos=(self.center_x+(75/1.5),15), size=(50,150)) # Cover the circle
            for i in range(UserInput.missed):
                y = 15 + 150 + (i*120) # Calculate y value of rectangle
                Rectangle(pos=(self.center_x+(75/1.5),y), size=(50,120))
            Color(0.75, 0, 0)
            for i in range(5 - UserInput.missed):
                y = 15 + 150 + (UserInput.missed*120) + (i*120) # Calculate y value of rectangle
                Rectangle(pos=(self.center_x+(75/1.5),y), size=(50,120))
        # self.lv1 = Label(text="Lv1", pos=(100, 500))
        # self.add_widget(self.lv1)

    def redraw(self, dt):
        self.canvas.clear()
        with self.canvas:
            # print(Window.size[0])
            Color(1., 0, 0)
            Ellipse(3, pos=(self.center_x,10), size=(150,150))
            # print(UserInput.missed)
            # Rectangle(pos=(center_x+(75/1.5),15), size=(50,750))
            Rectangle(pos=(self.center_x+(75/1.5),15), size=(50,150)) # Cover the circle
            for i in range(UserInput.missed):
                y = 15 + 150 + (i*120) # Calculate y value of rectangle
                Rectangle(pos=(self.center_x+(75/1.5),y), size=(50,120))
            Color(0.75, 0, 0)
            for i in range(5 - UserInput.missed):
                y = 15 + 150 + (UserInput.missed*120) + (i*120) # Calculate y value of rectangle
                Rectangle(pos=(self.center_x+(75/1.5),y), size=(50,120))

    def startClock(self):
        Clock.schedule_interval(self.redraw, 0.5)

class FlipPages(PageLayout):
    def __init__(self, **kwargs):
        super(FlipPages, self).__init__(**kwargs)
        page1 = UserInput()
        page2 = Punishments()

        page2.startClock()

        self.add_widget(page1)
        self.add_widget(page2)

class MyApp(App):

    def build(self):
        return FlipPages()
    
if __name__ == '__main__':
    MyApp().run()