#!/usr/bin/python

RED_PIN   = 17
GREEN_PIN = 22
BLUE_PIN  = 24

import subprocess
import os
import time
import sys
import termios
import tty
import pigpio
import time
import serial
from thread import start_new_thread

bright = 255
r = 255.0
g = 0.0
b = 0.0

pi = pigpio.pi()


def setLights(pin, brightness):
	realBrightness = int(int(brightness) * (float(bright) / 255.0))
	pi.set_PWM_dutycycle(pin, realBrightness)



tmp = os.popen("sudo /opt/vc/bin/tvservice -s").read()
if tmp.find("off") == -1:
	print "monitor is on"
	setLights(RED_PIN,0)
	setLights(GREEN_PIN,0)
	setLights(BLUE_PIN,0)
	os.system("tvservice -o")
	##ser = serial.Serial('/dev/ttyACM0',9600)
	##time.sleep(2)
	##ser.write('0')
	##ser.close()
else:
	print "monitor is off"
	os.system("tvservice -p")
	setLights(RED_PIN,sys.argv[1])
	setLights(GREEN_PIN,sys.argv[1])
	setLights(BLUE_PIN,sys.argv[1])
	##ser = serial.Serial('/dev/ttyACM0',9600)
	##time.sleep(2)
	##ser.write('1') ##tell arduino to to check for gestures
	##ser.close()
pi.stop()
