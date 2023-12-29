# Brain afk while codind xdd
import pydirectinput
import time
from pynput.keyboard import Key, Listener

pydirectinput.mouseUp()

def bst(b:int):
    pydirectinput.moveTo(708, 740)

    pydirectinput.mouseDown()

    for a in range(11):
        pydirectinput.move(None ,-b, 0.001)
        pydirectinput.move(51, None, 0.001)
        pydirectinput.move(None, b, 0.001)

    for a in range(2):
        pydirectinput.move(-45, None, 0.001)
 
def show(key):
   
    if key == Key.alt_gr:
        bst(450)

    if key == Key.tab: 
        return False
 
with Listener(on_press = show) as listener:
    listener.join()
