import RPi.GPIO as GPIO
import time
from time import sleep
from picamera import PiCamera
from datetime import datetime
import os
import sys

recordFlag = False

sensorDelay = 0 
lastTime = 0
thisTime = 0
sensorPin = 18
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(sensorPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
camera = PiCamera(resolution=(2592,1944), framerate=10)
# average out reading from motion sensor

print("setup done")
try:

   while True: # Run forever
        filename = "{0:%m}-{0:%d}-{0:%H}-{0:%M}-{0:%S}.h264".format(datetime.now())
        if GPIO.input(sensorPin) == GPIO.HIGH:
            recordFlag = True
	    print("motion detected")
            camera.start_recording(filename, format='h264', quality=23)
            lastTime = time.time()
            while recordFlag == True:
                if GPIO.input(sensorPin) == GPIO.LOW:
                    thisTime = int(time.time() - lastTime)
                    #print("!!! SENSOR IS OFF !!! current time limit is "), thisTime 
                    sleep(.1) # buffering time. video recording gets choppy without it
                    if thisTime > sensorDelay:
                        recordFlag = False
                else:
                    lastTime = time.time()
                    sleep(1)

            camera.stop_recording()
            #print("recording finished!")
            os.system('mv /home/pi/camCapture/*.h264 /media/usb/')
            print("!!!!!!!!!!!!!!!!  ALL DONE  !!!!!!!!!!!!!!!!!")
except (KeyboardInterrupt, SystemExit):
    print '\n! Received keyboard interrupt, quitting threads.\n'
    sys.exit()