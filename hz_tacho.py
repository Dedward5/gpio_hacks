# Scrit to read Tacho signal form a Car EUC giving non linear HZ output.

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
hz = 0

##### Functions and callbacks #####
def tacho_pulse (channel): # a callback thats called when GPIO Pin 17 rises
	global pulses
	global last_pulse
	global pulse_gap
	global rpm
	global hz
	pulse_gap = time.time() - last_pulse	
	last_pulse = time.time ()
	pulses +=1 
	hz = 1/ pulse_gap
	rpm = hz * 60 * hz
	

##### Create callback for puse detection #####

GPIO.add_event_detect(17, GPIO.RISING, callback=tacho_pulse) #call callback whe$


##### Main program ######


while pulses <100:

	print("Pulses = ",pulses)
	print("Pulse Gap =",pulse_gap)
	print("Hz = ",hz)
	print("RPM = ",rpm)


GPIO.cleanup() # cleanup the GPIO on exit

  

