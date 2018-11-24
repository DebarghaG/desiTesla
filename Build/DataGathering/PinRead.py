"""
We're creating a hardware short to interface the signals from the Blynk app to the brain of the car.

Pin 24 --> Left --> Shorted with Pin 21
Pin 25 --> Right --> Shorted with Pin 22
Pin 26 --> Forward --> Shorted with Pin 23.

By reading the state of the pins, the car brain can understand how the user is controlling the car. 
"""

import RPi.GPIO as GPIO

def Direction():
    left = GPIO.input(21)
    right = GPIO.input(22)
    forward = GPIO.input(23)

    if(left== True and right== False and foward==True):
        direction = 'FL'
    if(left== False and right== True and foward==True):
        direction = 'FR'
    if(left== False and right== False and foward==True):
        direction = 'FF'
    if(left== False and right== False and foward==False):
        direction = 'NN'
    return direction
