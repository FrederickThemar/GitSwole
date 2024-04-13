import smtplib
import pandas as pd
import random

def send_dumb_sms():
    content=get_random_msg()

    mail=smtplib.SMTP('smtp.gmail.com', 587)
    mail.ehlo()
    mail.starttls()
    sender='harryplotter631@gmail.com'
    recipient='dashastepanova0731@gmail.com'
    mail.login('harryplotter631@gmail.com','feob oycr eavg aogp')
    header='To:'+recipient+'\n'+'From:' \
    +sender+'\n'+'subject:testmail\n'
    content=header+content
    mail.sendmail(sender, recipient, content)
    mail.close()


def get_random_msg():
    file = pd.read_excel("bad_messages.xlsx")
    num = random.randint(0, len(file) - 1)
    random_msg = file.iloc[num, 0]
    return random_msg
