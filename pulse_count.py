# Scrit to initiate GPIO and count how many times a button is pressed per min
# See https://www.cl.cam.ac.uk/projects/raspberrypi/tutorials/robot/buttons_and_switches/

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

GPIO.setup(17,GPIO.IN) #set up pin 17 for input

while True:
  if GPIO.input(17): # if PIN 17 is HIGH which ==1 then
    print ("No input")
  else: 
    print("Button Pressed")
    

