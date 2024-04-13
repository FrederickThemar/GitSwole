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
import smtplib
import pandas as pd
import random

def send_dumb_sms(msg):
    content=msg

    mail=smtplib.SMTP('smtp.gmail.com', 587)
    mail.ehlo()
    mail.starttls()
    sender='harryplotter631@gmail.com'
    recipient='4794097853@tmomail.net'
    mail.login('harryplotter631@gmail.com','feob oycr eavg aogp')
    mail.sendmail(sender, recipient, content)
    mail.close()


class UserInput(BoxLayout):
    missed = 0
    def __init__(self, **kwargs):
        super(UserInput, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.text = Label(text='How many steps did you take today?')
        self.add_widget(self.text)
        self.getInput = TextInput(multiline=False, size_hint=(1, .25))
        self.add_widget(self.getInput)
        self.text.bind()
        self.getInput.bind(on_text_validate=self.checkStepCount)
        # self.missed = 0
        self.messageList = []
        self.messageDict = {
            1: ["would you be interested in learing more about the church of scientology?\nhttps://www.scientology.org/",
                "Hey, you had some food in your teeth earlier, but i didn't tell you. Im sorry.", 
                "You're a hater. I'm just tryna act a little sussy sometimes.", 
                "I want to eat your bananas.", 
                "you're smell like doritos"],

            2: ["Mom is drinking again.", 
                "My toe itch", 
                "ooo wee mash my buttons!", 
                "I love you darling moist honey buscuit", 
                "Hey dad, i need some money to cover the vet bills for my partner's emotional support rabbit. \nIt should only be like 200 bucks."],

            3: ["I think you left your shirt at my house lat night...",
                "I think we should break up. You're kinda too much for me rn.",
                "I miss you daddy.",
                "I want taylor swift to be my mommy.",
                "Your face is stupid"],

            4: ["um, hi (uwu) *extends hand* I-I r-really like you-you're face! uwu *sniffles* ",
                "On the fields of mother's mercy, \nLiquifying the interior of my mind,\nMy body aches for you inside\nMy head like little chunks of lead.\n\nI hope you don't think differently of me now. Wanna grab dinner?",
                "we should get back together.",
                "your parents should have gotten a divorce.",
                "Hi baby girl hehe. Everything's okay, I promise. I forgive you. It's okay, don't worry about it. \nEverything's gonna be okay. I love you. I love you so much. \nI love you more than there are grains of sand, on every beach, of every planet, of every galaxy of the universe... "],

            5: ["blood blood blood blood blood blood blood blood blood blood blood blood blood blood blood blood",
                "I think you've put on some weight.",
                "I still love you.",
                "Wanna come overrr? xoxo i miss you",
                "I'm pregnant. It's yours."]
        }
        

    def checkStepCount(self, instance):
        try: 
            if int(instance.text) < 2000:
                UserInput.missed += 1
                # self.missed += 1
                if UserInput.missed > 5:
                    # self.missed = 5
                    UserInput.missed = 5
                self.messageList = self.messageDict[UserInput.missed]
                self.text.text = f"Uh oh! That was a poor decision. You have missed {UserInput.missed} goals. \nNow you must choose...\n\n" + ''.join(map(lambda x: f'{x[0] + 1}: \"{x[1]}\"\n\n', enumerate(self.messageList))) + "\nChoose a message to send, you naughty little slacker."
                self.getInput.text = ""  # Reset the input text box
                self.getInput.unbind(on_text_validate=self.checkStepCount)
                self.getInput.bind(on_text_validate=self.getMessageIndex)
                
            else:
                self.text.text = "Gooooood... You are doing great. Don't mess up now..."
                self.getInput.text = ""

        except ValueError: 
            self.text.text = "You gotta enter a number, you goofwad."
            self.getInput.text = ""

    def getMessageIndex(self, instance):
        try:
            message_index = int(instance.text)
            if 1 <= message_index <= len(self.messageList):
                self.selectedMessageIndex = message_index - 1  # Store the selected index (adjusting to 0-based)
                self.text.text = f"Sending \"{self.messageList[message_index-1]}\" to your ex!!!\nHow many steps did you take today?" 
                send_dumb_sms(self.messageList[message_index-1])
                self.getInput.text = ""
                self.getInput.unbind(on_text_validate=self.getMessageIndex)
                self.getInput.bind(on_text_validate=self.checkStepCount)


            else:
                self.text.text = "Invalid message index. Choose a valid index."
                self.getInput.text = ""
        except ValueError:
            self.text.text = "You gotta enter a number, you goofwad."
            self.getInput.text = ""

        # if int(instance.text) < 2000:
        #     # Use a lambda function inside the formatted string to output each item in the list hotdog along with its index followed by a new line
        #     UserInput.missed += 1
        #     self.messageList = self.messageDict(UserInput.missed)
        #     self.text.text = f"Uh oh! That was a poor decision. You have missed {self.missed} goals. \nNow you must choose...\n" + ''.join(map(lambda x: f'Message {x[0] + 1}: {x[1]}\n', enumerate(self.messageList))) + "\nChoose a message to send, you naughty little slacker."
        # else:
        #     self.text.text = "Gooooood~~"

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