import RPi.GPIO as GPIO
import time
from time import sleep
from picamera import PiCamera
from datetime import datetime
import os
import sys


sensorPin = 18
GPIO.setwarnings(True)
GPIO.setmode(GPIO.BCM)
GPIO.setup(sensorPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while True: #
    if GPIO.input(sensorPin) == GPIO.HIGH:
        print ("motion detected")
        sleep (1)
    else:
        print ("motion  NOT detected")
        sleep (1)
        
        