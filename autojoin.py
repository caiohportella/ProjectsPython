import time 
import pyautogui
import webbrowser as wb
from pynput.keyboard import Controller, Key
from datetime import datetime 

list = [
    ['https://teams.microsoft.com/l/meetup-join/19%3ae8233a338f404fdb82be1819280339b7%40thread.tacv2/1633124071812?context=%7b%22Tid%22%3a%228eb29201-a27d-4302-8473-c982eb5be935%22%2c%22Oid%22%3a%2248799efa-5d79-4dcb-9cab-22ec879dd93d%22%7d',
    '11:21','12:30']
]

keyboard = Controller()

class_started = False

for lecture  in list:
    while True :
        if class_started==False:
            if (datetime.now().hour == int(lecture[1].split(':')[0]) and 
                datetime.now().minute == int(lecture[1].split(':')[1])):
                wb.open(lecture[0])
                class_started = True
                time.sleep(20)
                pyautogui.press('right')
                time.sleep(1)
                pyautogui.press('enter')
                time.sleep(5)
                pyautogui.hotkey('ctrl','shift','m')
                time.sleep(15)
                pyautogui.click(1357, 691)
                time.sleep(10)
        elif   (datetime.now().hour == int(lecture[2].split(':')[0]) and
                datetime.now().minute == int(lecture[2].split(':')[1])):
                class_started = False
                pyautogui.hotkey('ctrl','shift','b')
                time.sleep(3)
                pyautogui.hotkey('alt','f4')
                time.sleep(3)
                pyautogui.hotkey('alt','f4')
                break