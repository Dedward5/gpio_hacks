# Scrit to initiate GPIO and see if a bitton is pressed
# See https://www.cl.cam.ac.uk/projects/raspberrypi/tutorials/robot/buttons_and_switches/

import RPI.GPIO as GPO
GPIO.setmode(GPIO.BCM)

GPIO.setup(17,GPIO.IN) #set up pin 17 for input

while True:
  if (GPIO.input(17)):
    print("Button Pressed")
    

