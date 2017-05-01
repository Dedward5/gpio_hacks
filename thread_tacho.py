
import time
import threading
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.IN)



global last_pulse
last_pulse = time.time()
global pulse_gap
pulse_gap = 99

def get_pulse_gap ():
	global pulse_gap
	global last_pulse
	while True:
		GPIO.wait_for_edge(18, GPIO.RISING)
		print ("pulse")
		time_now = time.time()
		pulse_gap = last_pulse - time_now
		last_pulse = time_now
	

gap_thread = threading.Thread (target=get_pulse_gap, args=())
gap_thread.start()


# get_pulse_gap()


while True:
	global pulse_gap
	# print (pulse_gap)
	rpm = 0.5 /pulse_gap
	print("RPM ",int(rpm*60))
	# print("nothing")

    

