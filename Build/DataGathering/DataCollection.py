"""
This piece of code is meant to be run during the data collection phase .

It captures images with the timestamp and the direction to label the files.
"""

from time import sleep
import picamera
#from PinRead import Direction
import datetime as dt
camera = picamera.PiCamera()

def CaptureForTraining():
    i=0
    #250 millisecond delay between images
    #120,000 ms total runtime ( 2 minutes for training)
    #480 images, with names stamped with both the timestamp and the direction of the car.
    while(i<120000):
        timeinms=int((dt.datetime.utcnow() - dt.datetime(1970,1,1)).total_seconds() * 1000)
        #dir = Direction()
        camera.capture("""dir+ """ "%s"  %timeinms + ".jpg", resize=(640, 480))
        #camera.capture(dir + ".jpg", resize=(640, 480))
        i+=250
        #Sleeping for 250ms
        sleep(0.25)

    camera.resolution = (800, 600)

CaptureForTraining()
