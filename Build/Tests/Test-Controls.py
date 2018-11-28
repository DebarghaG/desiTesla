import sys
import time
import RPi.GPIO as GPIO

mode=GPIO.getmode()

Forward=13
Backward=12
Right = 24
Left = 23

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
    GPIO.output(Left, GPIO.HIGH)
    print("Moving Left")
    time.sleep(x)
    GPIO.output(Forward, GPIO.LOW)
    GPIO.output(Left, GPIO.LOW)

start_time = time.clock()
forward(5)
reverse(5)
left(10)
right(10)
print time.clock() - start_time, "seconds"
GPIO.cleanup()
