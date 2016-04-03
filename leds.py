#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
import os
import subprocess

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)

# setup pins as an output
GPIO.setup(22,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)

#turn on leds for 1 second
GPIO.output(22, True)
GPIO.output(23, True)
GPIO.output(24, False)
time.sleep(1)

#turn off leds
GPIO.output(22, False)
GPIO.output(23, False)
GPIO.output(24, True)

#loop
while 1 < 2:
    #KISMET led
    kismet = subprocess.Popen(['ps -ef | grep kismet | grep -v grep'], stdout=subprocess.PIPE, shell=True) 
    (output, error) = kismet.communicate()
    if 'kismet_server' in output:
        GPIO.output(22, True) #Turn on YELLOW LED
    else:
        GPIO.output(22, False) #Turn off YELLOW LED

    #GPS led
    gps = subprocess.Popen(['ps -ef | grep gpsd | grep -v grep'], stdout=subprocess.PIPE, shell=True) 
    (output, error) = gps.communicate()
    if 'gpsd' in output:
        GPIO.output(23, True) #Turn on RED LED
    else:
        GPIO.output(23, False) #Turn off RED LED

    time.sleep(5)
    GPIO.output(24, False)
    time.sleep(1)
    GPIO.output(24, True)

