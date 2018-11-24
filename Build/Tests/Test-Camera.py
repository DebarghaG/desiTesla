# -*- coding: utf-8 -*-

#Checking if the camera can capture images

import picamera
camera = picamera.PiCamera()
camera.capture(‘snapshot.jpg’, resize=(640, 480))

camera.resolution = (800, 600)
