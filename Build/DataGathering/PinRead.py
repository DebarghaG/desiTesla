"""
We're creating a hardware short to interface the signals from the Blynk app to the brain of the car.

Pin 23 --> Left --> Shorted with Pin 38
Pin 24 --> Right --> Shorted with Pin 37
Pin 13 --> Forward --> Shorted with Pin 15

By reading the state of the pins, the car brain can understand how the user is controlling the car.
"""

import RPi.GPIO as GPIO

def Direction():
    left = GPIO.input(38)
    right = GPIO.input(37)
    forward = GPIO.input(15)

    if(left== True and right== False and foward==True):
        direction = 'FL'
    if(left== False and right== True and foward==True):
        direction = 'FR'
    if(left== False and right== False and foward==True):
        direction = 'FF'
    if(left== False and right== False and foward==False):
        direction = 'NN'
    return direction
