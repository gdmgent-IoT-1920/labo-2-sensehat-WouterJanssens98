from sense_hat import SenseHat
import sys
import time
import random


sense = SenseHat()

def characterOne():
    sense.clear()
    r = random.randrange(0,255)
    g = random.randrange(0,255)
    b = random.randrange(0,255)
    X = [r, g, b] 
    O = [0, 0, 0]

    char_one = [
    O, O, X, X, X, X, O, O,
    O, O, X, X, X, X, O, O,
    O, O, O, X, X, O, O, O,
    O, X, X, X, X, X, X, O,
    O, O, O, X, X, O, O, O,
    O, O, O, X, X, O, O, O,
    O, X, X, O, O, X, X, O,
    X, X, O, O, O, O, X, X
    ]

    sense.set_pixels(char_one)
    time.sleep(2)
    
def characterTwo():
    sense.clear()
    r = random.randrange(0,255)
    g = random.randrange(0,255)
    b = random.randrange(0,255)
    X = [r, g, b]  
    O = [0, 0, 0]

    char_two = [
    O, X, X, O, O, X, X, O,
    O, X, X, O, O, X, X, O,
    O, X, X, O, O, X, X, O,
    O, O, O, O, O, O, O, O,
    O, O, O, X, X, O, O, O,
    O, O, O, X, X, O, O, O,
    O, X, O, O, O, O, X, O,
    O, O, X, X, X, X, O, O
    ]

    sense.set_pixels(char_two)
    time.sleep(2)    

def characterThree():
    sense.clear()
    r = random.randrange(0,255)
    g = random.randrange(0,255)
    b = random.randrange(0,255)
    X = [r, g, b]  
    O = [0, 0, 0]

    char_three = [
    O, O, O, O, O, O, O, O,
    O, X, X, O, O, X, X, O,
    X, X, O, X, X, O, X, X,
    X, X, O, X, X, O, X, X,
    X, X, O, X, X, O, X, X,
    X, X, O, O, O, O, X, X,
    X, X, O, O, O, O, X, X,
    X, X, O, O, O, O, X, X
    ]

    sense.set_pixels(char_three)
    time.sleep(2)    
  
def renderCharacters():
    while True:
        characterOne()
        sense.clear()
        characterTwo()
        sense.clear()
        characterThree()
        sense.clear()

try:
    renderCharacters()
except (KeyboardInterrupt, SystemExit):
    print('Programma sluiten')
finally:
    print('Opkuisen van de matrix')
    sense.clear()
    sys.exit()
    