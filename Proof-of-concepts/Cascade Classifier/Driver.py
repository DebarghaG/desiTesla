import sys
import threading
import numpy as np
import cv2


cap = cv2.VideoCapture(0)

stop_cascade = cv2.CascadeClassifier("/home/debargha/Documents/Desi Tesla/Proof-of-concepts/Cascade Classifier/stop_sign.xml")
light_cascade = cv2.CascadeClassifier("/home/debargha/Documents/Desi Tesla/Proof-of-concepts/Cascade Classifier/traffic_light.xml")

while True:
    ret, frames = cap.read()

    gray= cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)

    stop = stop_cascade.detectMultiScale(gray, 1.1, 5)
    light = light_cascade.detectMultiScale(gray, 1.1, 5)


    for (x,y,w,h) in stop:
        cv2.rectangle(frames,(x,y),(x+w,y+h),(0,0,255),2)

    for (x,y,w,h) in light:
        cv2.rectangle(frames,(x,y),(x+w,y+h),(0,0,255),2)

    cv2.imshow('video2', frames)

    if cv2.waitKey(33) == 27:
        break

    cv2.destroyAllWindows()
