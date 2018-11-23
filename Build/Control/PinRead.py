import RPi.GPIO as GPIO

def Direction()
    left = GPIO.input(21):
    right = GPIO.input(22):
    forward = GPIO.input(23):

    if(left== True and right== False and foward==True)
        direction = 'FL'
    if(left== False and right== True and foward==True)
        direction = 'FR'
    if(left== False and right== False and foward==True)
        direction = 'FF'
    if(left== False and right== False and foward==False)
        direction = 'NN'
    return direction
