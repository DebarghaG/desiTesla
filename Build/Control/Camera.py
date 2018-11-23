import picamera
from PinRead import Direction
import datetime as dt
camera = picamera.PiCamera()

def CaptureForTraining():
    i=0
    #250 millisecond delay between images
    #120,000 ms total runtime ( 2 minutes for training)
    while(i<120000):
        timeinms=int((dt.datetime.utcnow() - dt.datetime(1970,1,1)).total_seconds() * 1000)
        dir = Direction()
        camera.capture(str(timeinms) + dir + ".jpg", resize=(640, 480))
        i+=250
        #Sleeping for 250ms
        sleep(250)
        

    camera.resolution = (800, 600)
