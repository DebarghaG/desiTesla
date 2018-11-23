import RPi.GPIO as GPIO

def Direction()
    left = GPIO.input(21):
    right = GPIO.input(22):
    forward = GPIO.input(23):

    if(left== True && right== False && foward==True)
        direction = 'FL'
    if(left== False && right== True && foward==True)
        direction = 'FR'
    if(left== False && right== False && foward==True)
        direction = 'FF'
    if(left== False && right== False && foward==False)
        direction = 'NN'
    return direction
