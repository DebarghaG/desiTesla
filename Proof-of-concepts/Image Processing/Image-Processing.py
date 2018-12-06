import cv2
import numpy as np

img = cv2.imread('/home/debargha//home/debargha/Documents/Desi Tesla/Proof-of-concepts/Image Processing/FF0.jpg')
cv2.imshow('Original image',img)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray image', gray)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow('HSV image', hsv)

lower_red = np.array([30,150,50])
upper_red = np.array([255,255,180])
mask = cv2.inRange(hsv, lower_red, upper_red)
res = cv2.bitwise_and(img,img, mask= mask)

# Apply edge detection method on the image
edges = cv2.Canny(gray,50,150,apertureSize = 3)

# This returns an array of r and theta values
lines = cv2.HoughLines(edges,1,np.pi/180, 200)

if lines.all()!=None:

    # The below for loop runs till r and theta values
    # are in the range of the 2d array
    for r,theta in lines[0]:

        # Stores the value of cos(theta) in a
        a = np.cos(theta)

        # Stores the value of sin(theta) in b
        b = np.sin(theta)

        # x0 stores the value rcos(theta)
        x0 = a*r

        # y0 stores the value rsin(theta)
        y0 = b*r

        # x1 stores the rounded off value of (rcos(theta)-1000sin(theta))
        x1 = int(x0 + 1000*(-b))

        # y1 stores the rounded off value of (rsin(theta)+1000cos(theta))
        y1 = int(y0 + 1000*(a))

        # x2 stores the rounded off value of (rcos(theta)+1000sin(theta))
        x2 = int(x0 - 1000*(-b))

        # y2 stores the rounded off value of (rsin(theta)-1000cos(theta))
        y2 = int(y0 - 1000*(a))

        # cv2.line draws a line in img from the point(x1,y1) to (x2,y2).
        # (0,0,255) denotes the colour of the line to be
        #drawn. In this case, it is red.
        cv2.line(img,(x1,y1), (x2,y2), (0,0,255),2)

    # All the changes made in the input image are finally
    # written on a new image houghlines.jpg

    cv2.imshow('houghlines3.jpg',img)

"""
th1 = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
th2 = cv2.threshold(gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
blur = cv2.GaussianBlur(gray,(5,5),0)
th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
"""
blur = cv2.GaussianBlur(gray,(5,5),0)

thresholded_imagewoblur = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,11,2)

thresholded_imagewblur = cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,11,2)

cv2.imshow('Adaptive Gaussian Filtering w Blur',thresholded_imagewblur)
cv2.imshow('Adaptive Gaussian Filtering w/o Blur', thresholded_imagewoblur)
#cv2.imshow('Thresholded Binary', th1)


cv2.waitKey(0)
cv2.destroyAllWindows()
