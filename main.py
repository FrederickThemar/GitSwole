import kivy

from kivy.app import App
from kivy.uix.label import Label
# from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.pagelayout import PageLayout
from kivy.uix.relativelayout import RelativeLayout
# from kivy.graphics import *

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



# class Punishments(RelativeLayout):
#     def __init__(self, **kwargs):
#         super(Punishments, self).__init__(**kwargs)
#     with self.canvas:
#         Color(1., 0, 0)
#         Rectangle(pos=(10,10), size=(500,500))

class FlipPages(PageLayout):
    def __init__(self, **kwargs):
        super(FlipPages, self).__init__(**kwargs)
        page1 = UserInput()
        page2 = Label(text='ayy lmao')

        self.add_widget(page1)
        self.add_widget(page2)

class MyApp(App):

    def build(self):
        return FlipPages()
    
if __name__ == '__main__':
    MyApp().run()