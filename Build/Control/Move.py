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

def forward(x):
    GPIO.output(Forward, GPIO.HIGH)
    print("Moving Forward")
    time.sleep(x)
    GPIO.output(Forward, GPIO.LOW)

def reverse(x):
    GPIO.output(Backward, GPIO.HIGH)
    print("Moving Backward")
    time.sleep(x)
    GPIO.output(Backward, GPIO.LOW)

def right(x):
    GPIO.output(Forward, GPIO.HIGH)
    GPIO.output(Right, GPIO.HIGH)
    print("Moving Right")
    time.sleep(x)
    GPIO.output(Forward, GPIO.LOW)
    GPIO.output(Right, GPIO.LOW)

def left(x):
    GPIO.output(Forward, GPIO.HIGH)
    GPIO.output(Low, GPIO.HIGH)
    print("Moving Left")
    time.sleep(x)
    GPIO.output(Forward, GPIO.LOW)
    GPIO.output(Low, GPIO.LOW)

GPIO.cleanup()
