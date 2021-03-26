import RPi.GPIO as GPIO
import time
from time import sleep
from picamera import PiCamera
from datetime import datetime
import os
import sys


sensorPin = 18
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(sensorPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
camera = PiCamera()
camera.resolution(2592,1944) 


def capture_still(): 
       camera.capture(filename) 

print("setup done")
try:

    while True: # Run forever
        filename = "{0:%m}-{0:%d}-{0:%H}-{0:%M}-{0:%S}.jpg".format(datetime.now())
        if GPIO.input(sensorPin) == GPIO.HIGH:
            
            print("motion detected")
            sleep(0.1)
            capture_still()
            sleep(1)
            os.system('mv /home/pi/*.jpg /home/pi/motionimages/')
except (KeyboardInterrupt, SystemExit):
    print ('\n! Received keyboard interrupt, quitting\n')
sys.exit()
