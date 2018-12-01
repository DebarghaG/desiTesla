"""
We're creating a hardware short to interface the signals from the Blynk app to the brain of the car.

Pin 23 --> Left --> Shorted with Pin 38
Pin 24 --> Right --> Shorted with Pin 37
Pin 13 --> Forward --> Shorted with Pin 16

By reading the state of the pins, the car brain can understand how the user is controlling the car.
"""

import RPi.GPIO as GPIO
from gpiozero import Button

def Direction():
    """

    Code using the GPIO library.

   # GPIO.setmode(GPIO.BOARD)
   # GPIO.setup(38, GPIO.IN)
   # GPIO.setup(37, GPIO.IN)
   # GPIO.setup(16, GPIO.IN)
   # left = GPIO.input(38)
   # right = GPIO.input(37)
   # forward = GPIO.input(16)

    #if(left== True and right== False and forward==True):
       # direction = 'FL'
   # if(left== False and right== True and forward==True):
    #    direction = 'FR'
   # if(forward==True):
    #    direction = 'FF'
   # if(left== False and right== False and forward==False):
    #    direction = 'NN'
    """

    forwardbutton = Button(13)
    leftbutton = Button(24)
    rightbutton = Button(26)
    if forwardbutton.is_pressed:
	direction='FF'
    elif leftbutton.is_pressed:
        direction='FL'
    elif rightbutton.is_pressed:
        direction='FR'
    else:
        direction='NN'
    
    return direction
