# Scrit to initiate GPIO and count how many times a button is pressed per min
# 20th Feb 2017


##### Import libraries #####
# from __future__ import division
import RPi.GPIO as GPIO
import time


##### Setup GPIO on the PI #####

GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.IN) #set up pin 17 for input (button)

##### Setup variable ######
pulses = 0
last_pulse = time.time ()
pulse_gap = 1
rpm = 0

##### Functions and callbacks #####
def tacho_pulse (channel): # a callback thats called when GPIO Pin 17 rises
	global pulses
	global last_pulse
	global pulse_gap
	global rpm
	pulse_gap = time.time() - last_pulse	
	last_pulse = time.time ()
	pulses +=1 
	rpm = 60.0 / pulse_gap 

##### Create callback for puse detection #####

GPIO.add_event_detect(17, GPIO.RISING, callback=tacho_pulse) #call callback whe$


##### Main program ######


while pulses <20:

	print("Pulses",pulses)
	print("Pulse Gap",pulse_gap)
	print("RPM",rpm)



GPIO.cleanup() # cleanup the GPIO on exit

  

