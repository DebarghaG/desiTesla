"""
Utility library to create move in any directionself.

Call Move.direction(x) from the CarBrain to control the movement of the carself.
"""

import sys
import time
import RPi.GPIO as GPIO

from gpiozero import OutputDevice

#mode=GPIO.getmode()

Forward=13
Backward=12
Right = 24
Left = 23

forward_motor = OutputDevice(Forward)
backward_motor = OutputDevice(Backward)
right_motor = OutputDevice(Right)
left_motor = OutputDevice(Left)

sleeptime=1

"""
GPIO.setmode(GPIO.BOARD)
GPIO.setup(Forward, GPIO.OUT)
GPIO.setup(Backward, GPIO.OUT)
GPIO.setup(Right, GPIO.OUT)
GPIO.setup(Left, GPIO.OUT)
"""

def forward(x):
    #GPIO.output(Forward, GPIO.HIGH)
    forward_motor.on()
    print("Moving Forward")
    time.sleep(x)
    forward_motor.off()
    #GPIO.output(Forward, GPIO.LOW)

def stop(x):
    #GPIO.output(Backward, GPIO.HIGH)
    #Do nothing
    print("Moving Backward")
    time.sleep(x)
    #GPIO.output(Backward, GPIO.LOW)

def right(x):
    #GPIO.output(Forward, GPIO.HIGH)
    #GPIO.output(Right, GPIO.HIGH)
    forward_motor.on()
    right_motor.on()
    print("Moving Right")
    time.sleep(x)
    #GPIO.output(Forward, GPIO.LOW)
    #GPIO.output(Right, GPIO.LOW)
    forward_motor.off()
    right_motor.off()

def left(x):
    #GPIO.output(Forward, GPIO.HIGH)
    #GPIO.output(Left, GPIO.HIGH)
    forward_motor.on()
    left_motor.on()
    print("Moving Left")
    time.sleep(x)
    forward_motor.off()
    left_motor.off()
    #GPIO.output(Forward, GPIO.LOW)
    #GPIO.output(Left, GPIO.LOW)


GPIO.cleanup()
