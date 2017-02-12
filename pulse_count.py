# Scrit to initiate GPIO and count how many times a button is pressed per min
# 20th Feb 2017


##### Import libraries #####

import RPi.GPIO as GPIO
from time import sleep #enables sleep which is used later on


##### Setup GPIO on the PI #####

GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.IN) #set up pin 17 for input (button)

##### Setup variable ######
pulses = 0

##### Functions and callbacks #####
def tacho_pulse (channel): # a callback thats called when GPIO Pin 17 rises
	global pulses
	print ("Pulse")
	pulses +=1 

##### Create callback for puse detection #####

GPIO.add_event_detect(17, GPIO.RISING, callback=tacho_pulse) #call callback whe$


##### Main program ######


while pulses < 15:

	print(pulses)


GPIO.cleanup() # cleanup the GPIO on exit

  

