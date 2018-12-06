import numpy as np
import cv2
import move
import time
import picamera
import multiprocessing
import datetime as dt

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
    camera.capture("%s" %time.clock() + "jpg", resize=(150,150))
    sleep(0.2)
    print "Image captured on this process."

def Predict():
    result = loaded_model.predict_classes(image)
    if result='FF':
        forward(5)
    elif result="FL"
        left(5)
    elif result='FR'
        right(5)

def Move()
    """
    Moves the vehicle according to what's required
    """
