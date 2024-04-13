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
        self.getInput = TextInput(multiline=False, size_hint=(1, .25))
        self.add_widget(self.getInput)
        self.text.bind()
        self.getInput.bind(on_text_validate=self.checkStepCount)
        self.missed = 0
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
                "blood blood blood blood blood blood blood blood blood blood blood blood blood blood blood blood",
                "I want taylor swift to be my mommy.",
                "Your face is stupid"],

            4: ["um, hi (uwu) *extends hand* I-I r-really like you-you're face! uwu *sniffles* ",
                "On the fields of mother's mercy, \nLiquifying the interior of my mind,\nMy body aches for you inside\nMy head like little chunks of lead.\n\nI hope you don't think differently of me now. Wanna grab dinner?",
                "we should get back together.",
                "your parents should have gotten a divorce.",
                "Hi baby girl hehe. Everything's okay, I promise. I forgive you. It's okay, don't worry about it. \nEverything's gonna be okay. I love you. I love you so much. \nI love you more than there are grains of sand, on every beach, of every planet, of every galaxy of the universe. \nI-I need you in my life. I need you more than humans need water, and food to survive. \nYou mean more to me than - home depot means to Mr Ladrado. You mean more to me than just anything. \nYou mean more to me than gold and diamonds, mean to the greediest burglar. \nAnd you're just the most perfect, most beautiful girl in all of the world, and I love you so much. \nI hope you enjoy watching this, baby girl kiss, hehe. See you at school tomorrow baby girl. \nI love you raises eyebrows, hehe. I do, it's true. I love you more than anything else in the world hehehe. \nBye baby girl. Stay perfect. Just for me."],

            5: ["I miss you daddy.",
                "I think you've put on some weight...",
                "hey, i know its been a long time but i cant get you off my mind. i think of you with insatiable appetite. i have written you the following poem:\n\nIn the darkness of my soul, you lingered like a fart,\nA stench so foul, you left a permanent mark.\nYour love was like a poison, seeping through my veins,\nLeaving scars and memories, driving me insane.\n\nYou were a succubus, draining all my energy,\nLeaving me with nothing but despair and agony.\nYour kisses tasted like expired cheese,\nYour touch felt like a swarm of disease.\n\nYour lies were like cheap perfume, suffocating me,\nYour deceitful eyes, oh how they deceived me.\nBut I was blind, blinded by lust and desire,\nNow I see you for what you are, a burning dumpster fire.\n\nSo go ahead, with your wicked ways,\nBut know that I've escaped your toxic maze.\nI'll rise from the ashes, stronger than before,\nLeaving you behind, like a dirty old naughty girl/boy.\n\nI hope you still think of me fondly.",
                "Hey, do you have an extra pair of underwear I could borrow? Asking for a friend...",
                "I despise your life."]
        }
        

    def checkStepCount(self, instance):
        try: 
            if int(instance.text) < 2000:
                self.missed += 1
                self.messageList = self.messageDict[self.missed]
                self.text.text = f"Uh oh! That was a poor decision. You have missed {self.missed} goals. \nNow you must choose...\n\n" + ''.join(map(lambda x: f'{x[0] + 1}: \"{x[1]}\"\n\n', enumerate(self.messageList))) + "\nChoose a message to send, you naughty little slacker."
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
                self.text.text = f"Sending \"{self.messageList[message_index-1]}\" to PHONENUMBER!!!\nHow many steps did you take today?" 
                self.getInput.text = ""
                self.getInput.unbind(on_text_validate=self.getMessageIndex)
                self.getInput.bind(on_text_validate=self.checkStepCount)


            else:
                self.text.text = "Invalid message index. Choose a valid index."
                self.getInput.text = ""
        except ValueError:
            self.text.text = "You gotta enter a number, you goofwad."
            self.getInput.text = ""



    
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