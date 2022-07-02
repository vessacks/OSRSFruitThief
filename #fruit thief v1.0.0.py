#fruitthief 

#todo: 
#1. figure out how to implement windmouse. I think it's better and more customizable than pyHM mouse. 

from calendar import c
import pyautogui
import time
import numpy as np
from pyHM import mouse


def countdown(t): #generic countdown function
    while t>0:
        time.sleep(1)
        print(t)
        t -= 1
    print("Now!")

class InventorySlot(object): #an inventory slot
    def __init__(self):
        pass
    
    def getcoords(self):
        input("position your mouse at coord 1 and press enter")
        coord1 = pyautogui.position()
        print("recorded coord 1 as "+ str(coord1))
        input("position your mouse at coord 2 and press enter")
        coord2 = pyautogui.position()
        print("recorded coord 2 as "+ str(coord2))
        input("position your mouse at coord 3 and press enter")
        coord3 = pyautogui.position()
        print("recorded coord 3 as "+ str(coord3))    
        self.coords = [coord1, coord2, coord3] 

    def genclick(self): #random walk model away from coords
        coordpick = np.random.randint(1,4) #selects which of the coords to start with
        #print("coordpick is "+str(coordpick))
        if coordpick == 1:
            x,y = self.coords[0]
        elif coordpick == 2:
            x,y = self.coords[1]
        else:
            x,y = self.coords[2]
        
        #this part shifts the coord a random, linearly distributed amount from coord to widen central tendency
        x += np.random.randint(-7,8) #change these values to modify the size of the central tendency 
        y += np.random.randint(-7,8) #make sure these values are the same as the ones directly above

        #this part shifts the coord again using a random walk (binomial distro?) to conceal the linear distribution
        xshift = 0
        yshift = 0 #these are the amounts that the click will be shifted
        
        for i in range(300): # adds many random +1s and -1s to xshift and y shift. change this value to increase the amount of random walk
            xshift += np.random.randint(-1,2) #resolves randomly to -1 or 1
            yshift += np.random.randint(-1,2) #resolves ramdonly to -1 or 1
        #print("xshift is %s and yshift is %s" %(str(xshift), str(yshift)))
        
        x += xshift
        y += yshift

        #pyautogui.moveTo(x,y) #if the thing is working, ignore this line. 
        mouse.move(x,y, multiplier=1.5) #this moves the mouse to the final point
        time.sleep(.1)
        pyautogui.click()

       
class ClickableEntity(object): #same as inventory slot except the central tendency size and random walk count are modifiable
    def __init__(self, centralTendency,numberRandWalks):
        self.centralTendency = centralTendency #this is the radius in pixels of each coords central tendency. A good value for an inventory spot on my thinkpad is ~7
        self.numberRandWalks = numberRandWalks #this is the number of one pixel random walks a click will take. A good value for an inventory spot on my thinkpad is 300. 
    
    def getcoords(self):
        input("position your mouse at coord 1 and press enter")
        coord1 = pyautogui.position()
        print("recorded coord 1 as "+ str(coord1))
        input("position your mouse at coord 2 and press enter")
        coord2 = pyautogui.position()
        print("recorded coord 2 as "+ str(coord2))
        input("position your mouse at coord 3 and press enter")
        coord3 = pyautogui.position()
        print("recorded coord 3 as "+ str(coord3))    
        self.coords = [coord1, coord2, coord3] 

    def genclick(self): #randomizes a click location and clicks
        coordpick = np.random.randint(1,4) #selects which of the coords to start with
        #print("coordpick is "+str(coordpick))
        if coordpick == 1:
            x,y = self.coords[0]
        elif coordpick == 2:
            x,y = self.coords[1]
        else:
            x,y = self.coords[2]
        
        #this part shifts the coord a random, linearly distributed amount from coord to widen central tendency
        x += np.random.randint((self.centralTendency * -1), (self.centralTendency +1)) 
        y += np.random.randint((self.centralTendency * -1), (self.centralTendency +1)) 

        #this part shifts the coord again using a random walk (binomial distro?) to conceal the linear distribution
        xshift = 0
        yshift = 0 #these are the amounts that the click will be shifted
        
        for i in range(self.numberRandWalks): # adds numberRandWalks random +1s and -1s to xshift and y shift. change this value to increase the amount of random walk
            xshift += np.random.randint(-1,2) #resolves randomly to -1 or 1
            yshift += np.random.randint(-1,2) #resolves ramdonly to -1 or 1
        #print("xshift is %s and yshift is %s" %(str(xshift), str(yshift)))
        
        x += xshift
        y += yshift

        #pyautogui.moveTo(x,y) #this moves the mouse to the final point
        mouse.move(x,y, multiplier=1.5) #this moves the mouse to the final point
        time.sleep(.1)
        pyautogui.click()



slot1 = InventorySlot()
print("we will now take coords for inventory slot 1")
slot1.getcoords()

fruitStall = ClickableEntity(7,300)
print("we will now take coords for the fruit stall")
fruitStall.getcoords()



for i in range(200):
    wait1 = np.random.normal(loc=2,scale=.15)
    wait2 = np.random.normal(loc=1, scale=.08)
    
    fruitStall.genclick()
    time.sleep(wait1)

    slot1.genclick()
    time.sleep(wait2)

print("bubba")





