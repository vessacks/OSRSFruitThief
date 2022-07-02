#sandbox
from re import X
import pyautogui
import time
import numpy as np
from pyHM import mouse

input("start?")
start = mouse.get_current_position()

input("fin?")
fin = mouse.get_current_position()

for i in range(2):
    mouse.move(start[0],start[1], multiplier=1.5)
    mouse.move(fin[0],fin[1])
