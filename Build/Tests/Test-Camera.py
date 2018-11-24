# -*- coding: utf-8 -*-

#Checking if the camera can capture images

from picamera import PiCamera

camera = PiCamera()
camera.start_preview()
#camera.capture(‘/snapshot.jpg’, resize=(640, 480))
camera.capture(‘/snapshot.jpg’)
camera.stop_preview()

#camera.resolution = (800, 600)
