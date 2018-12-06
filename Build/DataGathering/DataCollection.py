"""
This piece of code is meant to be run during the data collection phase .

It captures images with the timestamp and the direction to label the files.
"""
from time import sleep
import time
import picamera
from PinRead import Direction
import datetime as dt
camera = picamera.PiCamera()

def CaptureForTraining():
    i=0
    #250 millisecond delay between images
    #120,000 ms total runtime ( 2 minutes for training)
    #480 images, with names stamped with both the timestamp and the direction of the car.
    while(i<120000):
        dir = Direction()
        start_time = time.clock()
        camera.capture("%s" %dir +  "%s"  %i + ".jpg", resize=(640, 480))
        #camera.capture(dir + ".jpg", resize=(640, 480))
        i+=250
        #Sleeping for 250ms
        sleep(0.25)
        print time.clock() - start_time, "seconds"

    camera.resolution = (800, 600)

CaptureForTraining()
