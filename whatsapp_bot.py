import mouse
import pyautogui as pt
import pyperclip as pc
from pynput.mouse import Controller, Button
from time import sleep
from whatsapp_responses import response

greendot=0
class WhatsApp:

    def __init__(self,speed=.5,click_speed=.3):
        self.speed=speed
        self.click_speed=click_speed
        self.message=''
        self.last_message=''



    def nav_green_dot(self):
            try:
                position=pt.locateOnScreen('greendot.png',confidence=.76)
                pt.moveTo(position[0:2], duration=self.speed)
                pt.moveRel(-100, 0, duration=self.speed)
                pt.doubleClick(interval=self.click_speed)
            except Exception as e:
                global greendot
                greendot=1
                print('Exception (nav_green_dot): ', e)

    def nav_input_box(self):
        try:
            position = pt.locateOnScreen('paperclip.png', confidence=.76)
            pt.moveTo(position[0:2], duration=self.speed)
            pt.moveRel(100, 12, duration=self.speed)
            pt.doubleClick(interval=self.click_speed)
        except Exception as e:
            print('Exception (nav_input_box): ', e)

    def nav_message(self):
        try:
            position = pt.locateOnScreen('paperclip.png', confidence=.76)
            pt.moveTo(position[0:2], duration=self.speed)

        except Exception as e:
            print('Exception (nav_message): ', e)



    def get_message(self):
            pt.moveRel(10, -60, duration=self.speed)
            pt.tripleClick(interval=self.click_speed)
            sleep(self.speed)
            pt.rightClick(interval=self.click_speed)
            sleep(self.speed)
            pt.moveRel(40,-280, duration=self.speed)
            pt.doubleClick(interval=self.click_speed)
            sleep(1)

            self.message=pc.paste()
            print('User Says: ',self.message)

    def send_message(self):
        try:
            if self.message != self.last_message:
                bot_response =response(self.message)
                print('You say:',bot_response)
                pt.typewrite(bot_response, interval=.1)
                pt.typewrite('\n')

                self.last_message =self.message
            else:
                print("No New messages")

        except Exception as e:
            print('Exception (nav_message):',e)


wa_bot = WhatsApp(speed=.5, click_speed=.4)
sleep(2)

while True:
     wa_bot.nav_green_dot()
     if greendot==1:
        greendot=0
        continue

     wa_bot.nav_input_box()
     wa_bot.nav_message()
     wa_bot.get_message()
     wa_bot.send_message()
     sleep(10)

