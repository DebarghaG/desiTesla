import numpy as np
import cv2
import move
import time
import picamera
import multiprocessing
import datetime as dt
from Predict import predict
from Move import forward
from Move import reverse
from Move import right
from Move import left

camera = picamera.PiCamera()
start_time=time.clock()

"""
To be written :

- Loop
-- Sends the captured image to the model for prediction
-- Recieves the direction of movement and acts on it
-- Drive is logged.

--Tertiary control is added : Haar cascade classifiers for object detection and
ultrasonic sensor based driving interrupts
"""

def CaptureImage():
    image = camera.capture("%s" %time.clock() + "jpg", resize=(50,50))
    image = cv2.resize(image, (50,50))
    image = image.reshape(1, 50, 50, 3)
    print "Image captured on this process."
    return image

def PredictAndMove(image):
    result = predict(image)
    if result=1:
        forward(1)
    elif result=2
        left(1)
    elif result=3
        right(1)

while (True):
    image=CaptureImage()
    PredictAndMove(image)
