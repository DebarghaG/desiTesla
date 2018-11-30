import sys
import time
import RPi.GPIO as GPIO
from gpiozero import OutputDevice

#mode=GPIO.getmode()

Forward=13
Backward=12
Right = 15
Left = 16

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

def reverse(x):
    #GPIO.output(Backward, GPIO.HIGH)
    backward_motor.on()
    print("Moving Backward")
    time.sleep(x)
    backward_motor.off()
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

start_time = time.clock()
forward(5)
reverse(5)
left(10)
right(10)
print time.clock() - start_time, "seconds"
GPIO.cleanup()
