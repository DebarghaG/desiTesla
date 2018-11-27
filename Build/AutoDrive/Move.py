"""
Utility library to create move in any directionself.

Call Move.direction(x) from the CarBrain to control the movement of the carself.
"""

import sys
import time
import RPi.GPIO as GPIO

mode=GPIO.getmode()
GPIO.cleanup()

Forward=26
Backward=20
Right = 25
Left = 19

sleeptime=1

GPIO.setmode(GPIO.BOARD)
GPIO.setup(Forward, GPIO.OUT)
GPIO.setup(Backward, GPIO.OUT)
GPIO.setup(Right, GPIO.OUT)
GPIO.setup(Left, GPIO.OUT)

def forward(x):
    GPIO.output(Forward, GPIO.HIGH)
    print("Moving Forward")
    time.sleep(x)
    GPIO.output(Forward, GPIO.LOW)

def right(x):
    GPIO.output(Forward, GPIO.HIGH)
    GPIO.output(Right, GPIO.HIGH)
    print("Moving Right")
    time.sleep(x)
    GPIO.output(Forward, GPIO.LOW)
    GPIO.output(Right, GPIO.LOW)

def left(x):
    GPIO.output(Forward, GPIO.HIGH)
    GPIO.output(Left, GPIO.HIGH)
    print("Moving Left")
    time.sleep(x)
    GPIO.output(Forward, GPIO.LOW)
    GPIO.output(Left, GPIO.LOW)

def stop(x):
    GPIO.output(Forward, GPIO.LOW)
    GPIO.output(Left, GPIO.LOW)
    print("Coming to a stop.")
    time.sleep(x)
    GPIO.output(Forward, GPIO.LOW)
    GPIO.output(Left, GPIO.LOW)

GPIO.cleanup()
