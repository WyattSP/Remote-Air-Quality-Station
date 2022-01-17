#functions to control sense HAT LEDs
from sense_hat import SenseHat
import time

sense = SenseHat()

def exit_program():
    sense.clear()
    sense.show_letter(str('E'))
    time.sleep(3)
    sense.clear()
    return

#color codes
O = (0,0,0)
G = (0,128,0)
B = (0,0,225)
R = (255,0,0)
Y = (225,225,0)
W = (225,225,225)

def start_up():
    sense.clear()

    signal = [
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, G, G, O, O, O,
    O, O, O, G, G, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    ]
    sense.set_pixels(signal)
    time.sleep(3)
    sense.clear()
    return

def start_collection():
    sense.clear()

    signal = [
    O, O, O, G, G, O, O, O,
    O, O, O, G, G, O, O, O,
    O, O, O, G, G, O, O, O,
    G, G, G, G, G, G, G, G,
    G, G, G, G, G, G, G, G,
    O, O, O, G, G, O, O, O,
    O, O, O, G, G, O, O, O,
    O, O, O, G, G, O, O, O,
    ]
    sense.set_pixels(signal)
    time.sleep(3)
    sense.clear()
    return
